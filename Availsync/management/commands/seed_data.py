from django.core.management.base import BaseCommand
from Availsync.models import User, Institution, Staff
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with seed data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Step 1: Create Users
        self.stdout.write(self.style.SUCCESS('Creating Users...'))
        user_list = []  # Store created users for later use in Staff

        for _ in range(15):  # Adjust number of users here
            user = User.objects.create_user(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username=fake.email(),
                password='password123',  # Password hashing happens automatically
                phone=fake.phone_number(),
                profile_image=fake.image_url(),
                role=random.choice(['Admin', 'Staff', 'User']),  # Assign random roles to users
            )
            user_list.append(user)

        self.stdout.write(self.style.SUCCESS(f'{len(user_list)} Users created successfully!'))

        # Step 2: Create Institutions
        self.stdout.write(self.style.SUCCESS('Creating Institutions...'))
        institution_list = []  # Store created institutions for Staff association

        for _ in range(5):  # Adjust number of institutions here
            institution = Institution.objects.create(
                name=fake.company(),
                address=fake.address(),
                username=fake.company_email(),
                phone=fake.phone_number(),
                totalstuffs=random.randint(5, 100),  # Random staff count
                bio=fake.text(max_nb_chars=200),
                working_days="Monday to Friday",
                working_hours="9AM - 5PM",
            )
            institution_list.append(institution)

        self.stdout.write(self.style.SUCCESS(f'{len(institution_list)} Institutions created successfully!'))

        # Step 3: Create Staff
        self.stdout.write(self.style.SUCCESS('Creating Staff...'))

        for user in user_list:  # Create staff for some users
            institution = random.choice(institution_list)
         
            Staff.objects.create(
                user_account=user,
                institution=institution,
                workdescription=fake.job(),
                status=random.choice(['Active', 'Inactive']),
                profile_image=None,  # Replace with a valid path if necessary
                 # Assign the same role as the user
            )

        self.stdout.write(self.style.SUCCESS('Staff created successfully!'))
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
