"""
Views configuration for the app.

Views are responsible for processing HTTP requests and returning responses
(HTML, JSON, redirects, etc.). For more information, see:
https://docs.djangoproject.com/en/6.0/topics/http/views/

How to write views:

1. Function-Based Views (FBVs)
  from django.http import HttpResponse

  def example_view(request):
    # Process the logic here
    return HttpResponse("Hello, world!")

2. Class-Based Views (CBVs)
  from django.views import View
  from django.http import HttpResponse

  class ExampleView(View):
    def get(self, request):
      # Handles GET requests
      return HttpResponse("GET response")

3. Rendering HTML Templates
  from django.shortcuts import render

  def home_page(request):
    context = {'title': 'Home Page'}
    return render(request, 'home.html', context)
"""
from django.shortcuts import render

# Create your views here.

def home_view(request):
  return render(request, "home.html")

def logged_in_view(request):
  request.session["user_data"] = {
    "user_reg": "0001",
    "name": "Test User",
    "email": "test@example.com",
  }

  return render(request, "logged_in.html")

def logged_out_view(request):
  request.session.flush()

  return render(request, "logged_out.html")
