from django import forms
from django.contrib.auth.models import User

from .models import *

sexchoices = [('1','Male'),('0','female')]
fbschoices = [('1','True'),('0','False')]
rerchoices = [('0','0'),('1','1'),('2','2')]
eiachoices = [('1','Yes'),('0','No')]
slopechoices = [('1','1'),('2','2'),('3','3')]
thalchoices = [('3','3'),('6','6'),('7','7')]
adschoices = [('0','0'),('1','1')]
cpchoices = [('1','1'),('2','2'),('3','3'),('4','4')]
cachoices = [('0','0'),('1','1'),('2','2'),('3','3')]

class UserForm(forms.Form):
    name = forms.CharField(label = 'Name')
    age = forms.IntegerField(label = 'Age')
    fields  = ['name','age']


class InsertForm(forms.Form):
    fullname = forms.CharField(max_length = 250,label = 'Full Name')
    age = forms.IntegerField(label= 'Age')
    sex = forms.ChoiceField(label = 'Sex', choices=sexchoices, widget=forms.RadioSelect())
    cp_type = forms.ChoiceField(label = 'Chest Pain Type', choices=cpchoices, widget=forms.RadioSelect())
    trest_bps = forms.IntegerField(label = 'Trestbps')
    chol = forms.IntegerField(label = 'Cholesterol')
    fbs = forms.ChoiceField(label = 'Fasting Blood Sugar', choices=fbschoices, widget=forms.RadioSelect())
    rer = forms.ChoiceField(label = 'Resting Electrocardiographic Results',choices=rerchoices, widget=forms.RadioSelect())
    thalch = forms.IntegerField(label = 'Thalch')
    eia = forms.ChoiceField(label = 'Exercise Induced Angina',choices=eiachoices, widget=forms.RadioSelect())
    oldpeak = forms.FloatField(label = 'Oldpeak')
    slope = forms.ChoiceField(label = 'Slope',choices=slopechoices, widget=forms.RadioSelect())
    ca = forms.ChoiceField(label = 'CA', choices=cachoices, widget=forms.RadioSelect())
    thal = forms.ChoiceField(label = 'Thal',choices=thalchoices, widget=forms.RadioSelect())


    fields  = ['fullname','age','sex','cp_type','trest_bps','chol','fbs','rer','thalch','eia','oldpeak','slope','ca','thal']
