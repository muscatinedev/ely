from django.contrib import admin
from .models import Personnel, Role, Presence

admin.site.register(Role)
admin.site.register(Personnel)
admin.site.register(Presence)
