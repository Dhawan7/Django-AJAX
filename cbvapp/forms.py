from django import forms
from django.contrib.auth.models import User
from cbvapp.models import signupModel

class userform(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')

class profileform(forms.ModelForm):
    class Meta():
        model = signupModel
        fields=('date_of_birth','pic')
        widgets= {
        "date_of_birth":forms.DateInput(attrs={'type':'date'})
        }
