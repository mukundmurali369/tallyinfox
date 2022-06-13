
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def load_create_groups(request):
    return render(request,'load_create_groups.html')
    
def load_create_ledgers(request):
    return render(request,'load_create_ledgers.html')