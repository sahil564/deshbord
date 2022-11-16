from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import TVS



# from .models import Order


# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
  
  
  
  
class TVS(forms.ModelForm):
	class Meta:
		model = TVS
		fields = ['username', 'password', 'email', 'machine_ID','machine_IDC','sensor','sensorname','phone']


