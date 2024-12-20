from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_student', 'is_instructor']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_student', 'is_instructor', 'bio', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Type', {'fields': ('is_student', 'is_instructor', 'bio', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
