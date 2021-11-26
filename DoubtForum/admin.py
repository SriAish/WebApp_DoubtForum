from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    pass


class DoubtSessionAdmin(admin.ModelAdmin):
    """Allows Staff and Superusers to create, edit and delete doubt sessions."""
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Allows Staff to only fill themselves as Creators of Doubt Session"""
        if db_field.name == "professor":
            kwargs["queryset"] = get_user_model().objects.filter(
                username=request.user.username
            )
        return super(DoubtSessionAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def get_queryset(self, request):
        """Allows Staff to only see and edit doubt sessions created by them"""
        qs = super(DoubtSessionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
                return qs
        print(request.user.username)
        return qs.filter(professor=request.user)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(DoubtSession, DoubtSessionAdmin)
