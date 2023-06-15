#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person():
    def __init__(self, name = "Maky", job = "Engineer"):
        if isinstance(name, str) and (1<=len(name)<=25):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
        
        if isinstance(job, str) and job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")
        

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, new_name):
            self._name = new_name
        
        @property
        def job(self):
            return self._job
        
        @job.setter
        def job(self, new_job):
            self._job = new_job
