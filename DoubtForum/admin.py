from django.contrib import admin
from .models import *


class DoubtAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doubt, DoubtAdmin)
admin.site.register(Tag, TagAdmin)
