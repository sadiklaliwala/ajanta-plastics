from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name="home"),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('scart/',views.scart,name="sc"),
    path('rcart/<int:pk>/',views.rcart,name="rcart"),
    path('buy/<int:pid>/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('cat/', views.cat, name='cat'),
    path('cat/<int:id>', views.readcat, name='readcat'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.customerregistration, name='customerregistration1'),
    path('checkout/', views.checkout, name='checkout'),
    path('bcheckout/<int:pid>', views.bcheckout, name='bcheckout'),
    path('payment_done/', views.payment_done, name='paymentdone'),
    path('payment_done/<int:pid>', views.bpayment_done, name='bpaymentdone'),
]