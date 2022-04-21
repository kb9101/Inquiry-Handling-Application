from django.contrib import admin
from .models import User
from .models import Inquiry
# Register your models here.

admin.site.register(User)
admin.site.register(Inquiry)