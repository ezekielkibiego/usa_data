from django.contrib import admin
from .models import State, Person

class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'state_abbrev', 'region', 'division')
    search_fields = ('state_name', 'state_abbrev')
    list_filter = ('region', 'division')

admin.site.register(State, StateAdmin)



class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'state_code', 'shirt_or_hat', 'quiz_points', 'team', 'signup', 'age', 'company')

admin.site.register(Person, PersonAdmin)
