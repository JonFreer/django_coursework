
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Course,Skills, Languages

#from .models import Tools, ALevel, GCSE

def cv_main(request):
    
    year1 = Course.objects.filter(year="year1")
    year2 = Course.objects.filter(year="year2")
    year3 = Course.objects.filter(year="year3")
    year4 = Course.objects.filter(year="year4")
    skills = Skills.objects.all()
    languages = Languages.objects.all()

    return render(request, 'cv/cv_main.html', {"year1":year1,
    "year2":year2,
    "year3":year3,
    "year4":year4,
     "skills":skills,
     "languages":languages})