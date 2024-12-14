from django.core.management.base import BaseCommand
from Availsync.models import User, Institution, Staff
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with seed data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Creating Users
        self.stdout.write(self.style.SUCCESS('Creating Users...'))
        for _ in range(15):  # Change the range to the number of users you want to create
            User.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username=fake.email(),
                password='password123',  
                phone=fake.phone_number(),
                profile_image=fake.image_url(),
                role='User', 
            )
        
        # Creating Institutions
        self.stdout.write(self.style.SUCCESS('Creating Institutions...'))
        for _ in range(5):  # Number of institutions to create
            Institution.objects.create(
                name=fake.company(),
                address=fake.address(),
                username=fake.company_email(),
                phone=fake.phone_number(),
                totalstuffs=random.randint(5, 100),  # Random staff count
                bio=fake.text(max_nb_chars=200),
                working_days="Monday to Friday",
                working_hours="9AM - 5PM",
            )

        # Creating Staff
        # self.stdout.write(self.style.SUCCESS('Creating Staff...'))
        # for _ in range(15):  # Number of staff to create
            institution = random.choice(Institution.objects.all())  # Randomly assign to an institution
            Staff.objects.create(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                username=fake.email(),
                password='password123',  # You can hash passwords if needed
                phone=fake.phone_number(),
                profile_image=fake.image_url(),
                role='Staff',
                workdescription=fake.job(),
                institution=institution,
                status='Active',
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
