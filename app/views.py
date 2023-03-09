from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from .models import Customer,Product,Cart,OrderPlaced,CustomUser
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages 
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login,authenticate

class ProductView(View):
    def get(self,request):
        totalitem=0
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        product=Product.objects.all()
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles,'totalitem':totalitem,'product':product})

# def home(request):
#  return render(request, 'app/home.html')

# def product_detail(request):
#  return render(request, 'app/productdetail.html')\

class ProductDetailView(View):
    def get(self,request,pk):
        totalitem=0

        
        product=Product.objects.get(pk=pk)
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()

        return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem})
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    print(product)
    Cart(user=user,product=product).save()
    return redirect('showcart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        amount=0.0
        shipping_amount=70.0
        totalitem=0
        totalitem = len(Cart.objects.filter(user=request.user))
        
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        # print(cart_product)
        cart=Cart.objects.filter(user=user)
        # print(cart)
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount=amount+shipping_amount

    
            return render(request, 'app/addtocart.html',{'carts':cart, 'totalamount':totalamount,'amount':amount,'totalitem':totalitem})
        else:
            return render(request,'app/emptycart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')
@login_required
def address(request):
    add =Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html' ,{'add':add, 'active':'btn-primary'})
@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data =='samsung' or data=='apple':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data=='above':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def topwear(request,data=None):
    if data==None:
        topwear=Product.objects.filter(category='TW')
    elif data=='roadster' or data=='lee':
        topwear=Product.objects.filter(category='TW').filter(brand=data)
    elif data=='below':
        topwear=Product.objects.filter(category='TW').filter(discounted_price__lt=10000)
    elif data=='above':
        topwear=Product.objects.filter(category='TW').filter(discounted_price__gt=10000)
    return render(request,'app/Topwear.html',{'topwear':topwear})


def bottomwear(request,data=None):
    if data==None:
        bottomwear=Product.objects.filter(category='BW')
    elif data=='nostrum' or data=='lee':
        bottomwear=Product.objects.filter(category='BW').filter(brand=data)
    elif data=='below':
        bottomwear=Product.objects.filter(category='BW').filter(discounted_price__lt=10000)
    elif data=='above':
        bottomwear=Product.objects.filter(category='BW').filter(discounted_price__gt=10000)
    return render(request,'app/bottomwear.html',{'bottomwear':bottomwear})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.is_buyer = True
            get_form.save()
            messages.success(request,'Congratulations!! Registered Successfully')
        
        return render(request,'app/customerregistration.html',{'form':form ,})
    # model=CustomUser
    # form_class=CustomerRegistrationForm
    # template_name='app/customerregistration.html'
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type']='customuser'
    #     return super().get_context_data(**kwargs)

    # def form_valid(self, form):
    #     user=form.save()
    #     login(self.request,user)

    #     return redirect('home')

@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount=70.0
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]
    if cart_product:
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount
        totalamount= amount + shipping_amount
    return render(request, 'app/checkout.html', {'add':add,'totalamount': totalamount,'cart_items':cart_items})

@login_required
def payment_done(request):
    user= request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()

    c.delete()
    return redirect('orders')

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form , 'active':'btn-primary'})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            Customer(user=user,name=name,locality=locality,city=city,zipcode=zipcode,state=state).save()
            messages.success(request,'Congratulations!! Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form , 'active':'btn-primary'})



def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount
            
        data={

            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount
            
        data={
            
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        print(prod_id)
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        
        
        c.delete()
        amount=0.0
        shipping_amount=70.0
        tempamount=0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price)
                amount+=tempamount
            
        data={
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)

def customerlogin(request):
    if request.method=='POST':
        print(request.method)
        username=request.POST['username']
        password=request.POST['pswd']
        # is_seller=request.POST['usertype']
       
        user=authenticate(username=username,password=password)
        print(user)
        if user.is_buyer==True:
            if user is not None:
                login(request,user)
                return render(request,'app/profile.html')
            else:
                return redirect('login')
        else:
                return redirect('login') 
        
    else:
        return render(request,'app/login.html')

