from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('states/', state_list, name='state_list'),
    path('people/', person_list, name='person_list'),
    path('search/', search_people, name='search_people'),
    # path('about/', about, name='about'),
    # path('contact/', contact, name='contact'),
    # path('bloglist/', blog_list, name='bloglist'),
]