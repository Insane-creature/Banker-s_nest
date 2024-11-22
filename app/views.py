from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializers import *
from rest_framework.response import response

# Create your views here.
class ReactView(APIView):
    def 