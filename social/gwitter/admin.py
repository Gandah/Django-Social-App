#django-social/social/gwitter/admin.py

from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Gweet, Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile



class UserAdmin(admin.ModelAdmin):
    """
    This is the admin class for the User model. It allows us to see the username in the Django admin.
    @param model - the User model
    @param fields - the username we want to see in the admin page
    @param inlines - the profile we want to see in the admin page
    """
    model = User
    #only display username
    fields = ('username', 'password', 'email')
    inlines =[ProfileInline]

"""
    Unregister the default User model and register the User model with our custom UserAdmin.
"""
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Gweet)
# admin.site.register(Profile)
