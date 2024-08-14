from django.shortcuts import render
from rest_framework import viewsets
from apii.models import Company
from apii.serializer import CompanySerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
