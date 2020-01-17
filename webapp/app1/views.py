from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.views import APIView
# Create your views here.

@api_view(["POST","GET"])
def apiview(request):
    print(request.user)
    print(request.auth)
    if request.method == "POST":
     try:
        return Response(data="API is hit by POST and you are getting response")
     except:
        return json.Response("error")
    elif request.method == "GET":
        return Response(data="API hit by Get request And You are getting response back")

class classapiview(APIView):
    def get(self,request):
        return Response("Class API is hit by get request and you are getting response")
    def post(self,request):
        return Response(data="Class API hit by POST request And You are getting response back")
