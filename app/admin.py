# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from app.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(User, UserAdmin)
