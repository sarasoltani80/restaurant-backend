from django.contrib import admin
#import models of this directory
from .models import Todo

admin.site.register(Todo)
