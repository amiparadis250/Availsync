from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages

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

        # Authenticate with the custom user model
        user = authenticate(request, username=username, password=password)
        print(user,'----------------------------------------------------------------')
        
        if user is not None:
            # Successful login
            login(request, user)
            return redirect('home')  
        else:
            # Invalid credentials
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

# Register view (You can add registration logic here)
def Register(request):
    return render(request, 'register.html')
