from django.shortcuts import render
from . forms import loanmodelForm
from . forms import newform
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import loanmodel
from . serializers import loanmodelSerializers
import pickle

from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

# Create your views here.
class LoanModelView(viewsets.ModelViewSet):
	queryset = loanmodel.objects.all()
	serializer_class = loanmodelSerializers

@api_view(["POST"])
def returnobj(request):
	try:
		mydata=request.data
		firstname=mydata["firstname"]
		rdata=loanmodel.objects.filter(firstname=firstname)
		djason=loanmodelSerializers(rdata,many=True).data
		serializer_class = loanmodelSerializers
		return JsonResponse(djason, safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)	



def cxcontact(request):
	if request.method=='POST':
		form=loanmodelForm(request.POST)
		print(request)
		print("post method running")
	# if form.is_valid():
	form=loanmodelForm()
	return render(request, 'myform/cxform.html',{'form':form})
#Made only for testing, scratched the idea as form will be made by the frontend react
def cxcontact2(request):
	if request.method=='POST':
		form=newform(request.POST)
		if form.is_valid():
			Firstname = form.cleaned_data['firstname']
			queryset=loanmodel.objects.filter(firstname=Firstname)
			serializer_class = loanmodelSerializers
			print(queryset)
			infolist=list(queryset)
			print(infolist)
	form=newform()
	return render(request,'myform/cxform2.html',{'form':form})