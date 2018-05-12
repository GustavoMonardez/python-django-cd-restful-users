from django.shortcuts import render, HttpResponse, redirect
from .models import User
from time import strftime
import datetime
from django.core import serializers

def index(request):
    #context = {"users": serializers.serialize('json', User.objects.all().values())}
    context = {"users": User.objects.all().values()}
    return render(request,"restfulusers_app/index.html", context)

def new(request):
    return render(request,"restfulusers_app/new.html")

def create(request):
    # capture data
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    # validate data

    #insert data
    user = User.objects.create(first_name=first_name,last_name=last_name,email=email)
    # redirect to user profile page
    page = "/users/" + str(user.id)   
    return redirect(page)

def edit(request,user):
    user = {"user":User.objects.get(id=user)}
    return render(request,"restfulusers_app/edit.html",user)

def show(request,user):
    user = {"user":User.objects.get(id=user)}
    return render(request,"restfulusers_app/show.html",user)

def destroy(request,user):
    user = User.objects.get(id=user)
    user.delete()
    return redirect("/users")

def update(request):
    # capture data
    id = request.POST["id"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    updated_at = datetime.datetime.now().strftime("%b %d %Y")
    # validate data

    # update data
    user = User.objects.get(id=id)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.updated_at = updated_at
    user.save()
    # update sessions
    
    users = serializers.serialize('json', User.objects.all())
    request.session["users"] = users
    #redirect
    page = "/users/" + str(id)
    return redirect(page)

def go_back(request):
    return redirect("/users")


