from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, UserFormStyled

def index(request):
    userform = UserFormStyled()
    return render(request, "index.html", {"form": userform})

def postuser(request):
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)

    return HttpResponse(f"<h2>Name: {name} Age: {age}</h2> <br/> {dict(request.POST)}")