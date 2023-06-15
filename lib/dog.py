#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog():
    def __init__(self, name = "Maki", breed = "Mastiff"):
        if isinstance(name, str) and (1<=len(name) <=25):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

        if isinstance(breed,str) and breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, new_name):
            self._name = new_name

        @property
        def breed(self):
            return self._breed
        
        @breed.setter
        def breed(self, new_breed):
            self._breed = new_breed