# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from users.models import User
from app.models import Topic, Entry
from rest_framework import viewsets
from app.serializers import UserSerializer, TopicSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows topics to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

