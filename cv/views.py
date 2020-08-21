
from django.shortcuts import render, get_object_or_404


# Create your views here.
def cv_main(request):
    return render(request, 'cv/cv_main.html', {})