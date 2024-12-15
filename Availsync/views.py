import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Staff
from .models import Institution
from datetime import timedelta
from django.db.models.functions import ExtractMonth
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import get_object_or_404


# Get the custom user model
User = get_user_model()

# Function to render the home page (example)
def hello(request):
    return render(request, 'index.html')

# Function to handle the login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Email as username
        password = request.POST.get('password')  # Password field

        # Authenticate the user with the custom user model
        user = authenticate(request, username=username, password=password)
        print(user, '----------------------------------------------------------------')

        if user is not None:
            # Successful login
            login(request, user)

            # Check the role of the user and redirect accordingly
            if user.role == 'Admin':  # If role is admin, redirect to admin dashboard
                return redirect('dashboard')  # Admin redirects to the admin dashboard
            elif user.role == 'Staff':  # If role is staff, redirect to the staff dashboard
                 return redirect('StaffDashboard', user_id=user.id)  # Staff redirects to their dashboard
            else:
                # If the role is not admin or staff, redirect to the home page
                return redirect('home')  # Redirect to home page for other roles

        else:
            # Invalid credentials
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

# Register view (You can add registration logic here)
def Register(request):
    return render(request, 'register.html')

def Checker(request):
    return render(request, 'availabilityChecker.html')

# Dashboard view with login required
@login_required
def Dashboard(request):
    total_users = User.objects.count()
    total_institutions = Institution.objects.count()
    total_staffs = Staff.objects.count()

    # Active Users (users who logged in within the last 30 days)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    active_users = User.objects.filter(last_login__gte=thirty_days_ago).count()

    # User Trends (number of users created per month)
    user_trends = User.objects.annotate(
        month=ExtractMonth('created_at')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')
    
    # Login Trends (number of logins per month)
    login_trends = User.objects.annotate(
        month=ExtractMonth('last_login')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    # Initialize counts for all months
    user_counts = {str(i): 0 for i in range(1, 13)}
    login_counts = {str(i): 0 for i in range(1, 13)}
    
    # Update with actual counts
    for trend in user_trends:
        user_counts[str(trend['month'])] = trend['count']
    for trend in login_trends:
        login_counts[str(trend['month'])] = trend['count']

    context = {
        'total_users': total_users,
        'total_institutions': total_institutions,
        'total_staffs': total_staffs,
        'active_users': active_users,
        'user_counts': json.dumps(user_counts),  # Pass the data as JSON
        'login_counts': json.dumps(login_counts),  # Pass login data as JSON
    }

    return render(request, 'dashboard.html', context)

@login_required
def admin_users(request):
    users = User.objects.all()  # Fetch all users

    context = {'users': users}
    
    return render(request, 'adminusers.html', context)
@login_required
def admin_Institutions(request):
    institutions = Institution.objects.all()  # Fetch all institutions

    context = {'institutions': institutions}
    
    return render(request, 'adminInstitutions.html', context)
@login_required
def admin_staffs(request):
    staffs = Staff.objects.select_related('institution', 'user_account').all()# Use select_related for optimization

    context = {'staffs': staffs}
    
    return render(request, 'adminstaff.html', context)   



def dashboard_staffs(request, user_id):
    # Use the user_id to fetch the user object
    user = get_object_or_404(User, id=user_id)

    # Add the user to the context
    context = {'user': user}

    return render(request, 'staffdashboard.html', context)
