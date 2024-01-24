from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("Hello World") #httpview
    return render(request, "home.html")  # render


def about(request):
    return render(request, "about.html")  # render


def contact(request):
    return HttpResponse("Hello Contact Page")


def details(request):
    return HttpResponse("Whole Details")


def thanks(request):
    return HttpResponse("Thank You")


def arithematicoperations(request):
    return render(request, "operations.html")  # render


def addition(request):
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    plus = number1 + number2
    sub = number1 - number2
    div = number1 / number2
    multi = number1 * number2
    return render(request, "operations.html",
                  {
                            'num1': number1,
                            'num2': number2,
                            'addition': plus,
                            'subtraction': sub,
                            'division': div,
                            'multiplication': multi,
                          }
                  )
