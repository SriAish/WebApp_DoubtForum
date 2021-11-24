from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    pass


class DoubtSessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)
admin.site.register(DoubtSession, DoubtSessionAdmin)
