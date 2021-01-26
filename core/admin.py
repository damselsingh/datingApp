from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('id', 'Bio', 'age', 'user')


admin.site.register(Profile, ProfileAdmin)
