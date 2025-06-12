#!/usr/bin/env python3
from random import choice
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():
    # Delete all existing pets
    Pet.query.delete()
    
    # Initialize faker
    fake = Faker()
    
    # Possible species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    
    # Create 10 random pets
    pets = []
    for _ in range(10):
        pet = Pet(
            name=fake.first_name(),
            species=choice(species)
        )
        pets.append(pet)
    
    # Add to database and commit
    db.session.add_all(pets)
    db.session.commit()
    print("Database seeded with 10 pets!")