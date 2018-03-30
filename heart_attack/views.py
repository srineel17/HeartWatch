from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
from numpy import genfromtxt
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA
from sklearn import cross_validation
from sklearn.svm import SVC
import csv

# Create your views here.
def index(request):
	form = InsertForm(request.POST or None)
	context = {
    	"form": form,
    }
	return render(request, 'heart_attack/index.html',context)


def insert_user(request):
	form = InsertForm(request.POST or None)

	if form.is_valid():
		fullname = request.POST['fullname']
		age = request.POST['age']
		sex = request.POST['sex']
		cp_type = request.POST['cp_type']
		trest_bps =request.POST['trest_bps']
		chol = request.POST['chol']
		fbs = request.POST['fbs']
		rer = request.POST['rer']
		thalch = request.POST['thalch']
		eia = request.POST['eia']
		oldpeak = request.POST['oldpeak']
		slope = request.POST['slope']
		ca = request.POST['ca']
		thal = request.POST['thal']

		fieldnames = [age,sex,cp_type,trest_bps,chol,fbs,rer,thalch,eia,oldpeak,slope,ca,thal]
    	with open('user_input.csv', 'w') as csvfile:
    		writer = csv.writer(csvfile)
    		writer.writerow(fieldnames)

		Storedata.objects.create(fullname = fullname,age=age,sex=sex,cp_type=cp_type,trest_bps=trest_bps,chol=chol,fbs=fbs,rer=rer,thalch=thalch,eia=eia,oldpeak=oldpeak,slope=slope,ca=ca,thal=thal)
		to_print = c_predict(fieldnames)
		context = {
	    	"to_print": int(to_print),
	    }
		return render(request, 'heart_attack/result.html',context)

	context = {
    	"form": form,
    }

	return render(request, 'heart_attack/index.html',context)


def result(request):
	return render(request, 'heart_attack/result.html')


def c_predict(a_list):
    dataset = genfromtxt('cleveland_data.csv',dtype = float, delimiter=',')

    X = dataset[:,0:13] #Feature Set
    y = dataset[:,13]   #Label Set
    value = list()
    f_list = list()

    for i in a_list:
    	 i = float(i)
    	 f_list.append(i)

    value.append(f_list)

    modelSVM = LinearSVC(C=0.001)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.001 ,train_size=0.999, random_state=0)
    modelSVM = modelSVM.fit(X_train, y_train)
    for i in modelSVM.predict(value):
        if i>1:
            i = i+1
        else:
            i = i

    return i
