from .models import Location
from faker import Faker
fake = Faker()

def seed_db(n):
    for i in range(0,n):
        Location.objects.create(
            location = fake.location()
        )

