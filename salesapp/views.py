from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from .models import CustomUser
from app.models import Customer
from salesapp.models import Seller
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import SellerRegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SellerProfileForm
from app.models import Product




class SellerRegistrationView(View):
    def get(self,request):
        form=SellerRegistrationForm()
        return render(request,'sellerregistration.html',{'form':form})
    def post(self,request):
        form=SellerRegistrationForm(request.POST)
        if form.is_valid():
           
            get_form=form.save(commit=False)
            get_form.is_seller=True
            get_form.save()
            messages.success(request,'Congratulations!! Registered Successfully')
        
        return render(request,'sellerregistration.html',{'form':form ,})






# def sellerregistration(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['pswd1']
        
#         # password2=request.POST.get('pswd2'),
        
#         a=CustomUser(
#         username=username,
#         email=email,
#         password=password,
#         is_seller=True

#         )
#         a.save()
#         return redirect('sellerlogin')
#     else:
#         return render(request,'sellerregistration.html')

def sellerlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pswd']
        # is_seller=request.POST['usertype']
        a=CustomUser.objects.filter(is_seller=True)
        if a:
            user=authenticate(username=username,password=password)
            print(user)
            if user.is_seller==True:
                if user is not None:

                    login(request, user)
                    return render(request,'sellerhome.html')
                else:
                    return redirect('sellerlogin')
            else:
                return redirect('sellerlogin')
        
    else:
       
       return render(request,'sellerlogin.html')

       
def upload_products(request):
    if request.method=='GET':
        return render(request,'upload_product.html')

        
    
    else:     
        seller=Seller.objects.get(user=request.user)
        # for i in seller:
        # print('***********************')
        # print(seller)
        # seller_name=seller.id
        # print(seller_name)
        # Product(seller=seller_name).save()
        title=request.POST['title']
        selling_price=request.POST['selling_price']
        discounted_price=request.POST['discounted_price']
        description=request.POST['description']
        brand=request.POST['brand']
        category=request.POST.get("category", False)
        # print(category)
        product_image=request.POST.get('product_image')
        
        a=Product(
            seller=seller,
            
            title=title,
            selling_price=selling_price,
            discounted_price=discounted_price,
            description=description,
            brands=brand,
            category=category,
            product_image=product_image)
        
        a.save()
        return redirect('sellerhome')

        
        
        
    
         

@method_decorator(login_required,name='dispatch')
class SellerProfileView(View):
    def get(self,request):
        form = SellerProfileForm()
        return render(request,'Sellerprofile.html',{'form':form,'active':'btn-primary' })
    def post(self,request):
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            seller_name = form.cleaned_data['seller_name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            Seller(user=user,seller_name=seller_name,locality=locality,city=city,zipcode=zipcode,state=state).save()
            messages.success(request,'Congratulations!! Profile Updated Successfully')
        return render(request,'Sellerprofile.html',{'form':form,'active':'btn-primary' })
def sellerhome(request):
    
    return render(request,'sellerhome.html')
    