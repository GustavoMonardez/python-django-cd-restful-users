from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"/restfulusers_app/index.html")

def new(request):
    return render(request,"/restfulusers_app/new.html")

def edit(request):
    return render(request,"/restfulusers_app/edit.html")

def show(request):
    return render(request,"/restfulusers_app/show.html")

def create(request):
    return redirect("users/<id>")

def destroy(request):
    return redirect("users/")

def update(request):
    return redirect("users/<id>")


