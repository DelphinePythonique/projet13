from django.contrib import admin

# Register your models here.
from .models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
