"""Difine the index page."""
from django.shortcuts import render

def index(request):
    """Learning logs home page."""
    return render(request, 'learning_logs/index.html')

