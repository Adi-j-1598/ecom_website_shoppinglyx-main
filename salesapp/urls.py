
from django.urls import path
from salesapp import views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('sellerregistration/', views.SellerRegistrationView.as_view(),name='sellerregistration'),
    path('sellerlogin',views.sellerlogin,name='sellerlogin'),
    path('upload_products',views.upload_products,name='upload_products'),
    path('SellerProfile',views.SellerProfileView.as_view(),name='SellerProfile'),
    path('sellerhome',views.sellerhome,name='sellerhome')
    # path('sellerregistration',views.SellerregistrationView.as_view(),name='sellerregistration')
]
