from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
   
    return render (request, 'index.html')


def state_list(request):
    states = State.objects.all()
    return render(request, 'state_list.html', {'states': states})




def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})

def search_people(request):
    query = request.GET.get('q')
    people = Person.objects.none()
    
    if query:
        people = Person.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    
    return render(request, 'search_results.html', {'people': people})
