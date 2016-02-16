from django.shortcuts import render, redirect

# -- Views

def index(request):

    return redirect("http://www.google.com")