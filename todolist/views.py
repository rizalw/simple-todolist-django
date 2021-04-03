from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages

# Create your views here.
def home_view(request):
    all_data = Todo.objects.all()
    context = {
        "data" : all_data
    }
    for all_data in context["data"]:
        print(all_data.id, all_data.title, all_data.description)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", context)

def create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "create.html")
    elif request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Todo.objects.create(title = title, description = description)
        messages.success(request, "Data has been added")
        return redirect("/")

def update_view(request, id):
    if request.method == "GET":
        data = {"data": Todo.objects.get(id=id)}
        return render(request, "update.html", data)
    elif request.method == "POST":
        data = Todo.objects.get(id=id)
        data.title = request.POST['title'] 
        data.description = request.POST['description'] 
        data.save()
        return redirect("/")

def delete_view(request, id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect("/")