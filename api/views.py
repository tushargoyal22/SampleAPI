from django.shortcuts import render
# from django.http import HttpResponse
# import json

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers

class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# Create your views here.

@api_view()
def usersApi(request):

    student1 = Student("Tushar Goyal",1,100)
    student2 = Student("Ashutosh Sharma",2,99)
    student3 = Student("Anuj Goel",3,98)

    response = serializers.StudentSerializer([
            student1,
            student2,
            student3
        ] ,many=True)

    return Response(response.data)