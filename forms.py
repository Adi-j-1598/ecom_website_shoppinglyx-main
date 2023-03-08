from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from authentication.models import CustomUser
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer
from django.db import transaction




class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        
        model = CustomUser
        
        # fields = "__all__"
        fields = ['username','email','password1','password2']
        labels = {'email': 'Email',}
        # widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
        # @transaction.atomic
        # def save(self):
        #     user=super().save(commit=False)
        #     # user.email=self.cleaned_data.get('email')
        #     user.is_buyer=True
        #     user.save()
        #     customuser=Customer.objects.create(user=user)
           
            # return user
        

# class LoginForm(AuthenticationForm):
    # username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True ,'class':'form-control'}))
    # password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=('Old_Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 =forms.CharField(label=('Confirm New Password'), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
     email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email" ,'class':'form-control'}),
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']
        widget = {'name' : forms.TextInput(attrs={'class' : 'form-control'}),'locality' : forms.TextInput(attrs={'class' : 'form-control'}),'city' : forms.TextInput(attrs={'class' : 'form-control'}),'state' : forms.Select(attrs={'class' : 'form-control'}),'zipcode' : forms.NumberInput(attrs={'class' : 'form-control'})}



    