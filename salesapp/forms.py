from django.contrib.auth.forms import  UserCreationForm
from authentication.models import CustomUser
from salesapp.models import Seller
from django.db import transaction
from django import forms 



class SellerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        
        model = CustomUser
        
        # fields = "__all__"
        fields = ['username','email','password1','password2',]
        labels = {'email': 'Email',}
        # widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['seller_name','locality','city','state','zipcode']
        widget = {'seller_name' : forms.TextInput(attrs={'class' : 'form-control'}),'locality' : forms.TextInput(attrs={'class' : 'form-control'}),'city' : forms.TextInput(attrs={'class' : 'form-control'}),'state' : forms.Select(attrs={'class' : 'form-control'}),'zipcode' : forms.NumberInput(attrs={'class' : 'form-control'})}
