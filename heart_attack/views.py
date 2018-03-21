from django.shortcuts import render
from .models import storedata
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'heart_attack/index.html')
 

def insertuser(request):

	if request.method == 'POST':
	
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
    	ads = request.POST['ads']
    	

    	storedata.objects.create(
    		age = age,
			sex = sex,
			cp_type = cp_type,
			trest_bps =trest_bps,
			chol = chol,
			fbs = fbs,
    		rer = rer, 
    		thalch = thalch,
    		eia = eia,
    		oldpeak = oldpeak,
    		slope = slope,
    		ca = ca,
    		thal = thal,
    		ads = ads
    	)

    	return HttpResponse('')
		
   	
   	
   
