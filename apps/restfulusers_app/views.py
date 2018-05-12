from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"restfulusers_app/index.html")

def new(request):
    return render(request,"restfulusers_app/new.html")

def edit(request,user):
    return render(request,"restfulusers_app/edit.html")

def show(request,user):
    return render(request,"restfulusers_app/show.html")

def create(request):
    return redirect("/users/1")

def destroy(request,user):
    return redirect("/users")

def update(request):
    return redirect("/users/4")


