from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help= 'it will insert data to the database'


    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no': 102,'name':'ahmad', 'age':22},
            {'roll_no': 101,'name':'khan', 'age':21},
            {'roll_no': 100,'name':'king', 'age':20},  
            {'roll_no': 100,'name':'jhon', 'age':21},  
            {'roll_no': 102,'name':'ahmad', 'age':22},  

        ]

        for data in dataset:
            # validation =(data['roll_no'], data['name'],data['age'])
            # roll_no=data['roll_no']
            existing_Record = Student.objects.filter(roll_no=data['roll_no'], name=data['name'], age=data['age']).exists()
            if not existing_Record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])  

            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no= {data['roll_no']}  name= {data['name']} , age = {data['age']} already exists'))
                

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))

