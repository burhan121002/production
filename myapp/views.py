from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
<<<<<<< Updated upstream
    return HttpResponse("Hello, World! 9A Done Completed Bye")
=======
    return HttpResponse("Hello, World! 9A Done Bye")
>>>>>>> Stashed changes
