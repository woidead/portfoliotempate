from django.contrib import admin
from .models import Skill, Message, Project

# Register your models here.
admin.site.register(Skill)
admin.site.register(Message)
admin.site.register(Project)