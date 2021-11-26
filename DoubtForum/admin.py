from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    pass


class DoubtSessionAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "professor":
            kwargs["queryset"] = get_user_model().objects.filter(
                username=request.user.username
            )
        return super(DoubtSessionAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def get_queryset(self, request):
        qs = super(DoubtSessionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
                return qs
        print(request.user.username)
        return qs.filter(professor=request.user)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(DoubtSession, DoubtSessionAdmin)
