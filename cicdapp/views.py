from django.shortcuts import render
from .models import student
from .services import calculate_grade
from django.http import JsonResponse

# Create your views here.
def student_list(request):
    data=[]
    students=student.objects.all()
    for s in students:
        data.append({
            "name":s.name,
            "marks":s.marks,
            "grade":calculate_grade(s.marks)
        })
    return JsonResponse(data,safe=False)