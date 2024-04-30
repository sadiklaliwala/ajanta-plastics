from unicodedata import category
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from adminsite.models import *

def home(request):
    cid=request.session.get('cid')
    user=Customer.objects.filter(customer_id=cid).first()
    el=Product.objects.all()
    el=Product.objects.all()
    if request.GET.get('search'):
        el=Product.objects.filter(product_name__icontains=request.GET.get('search'))
    params={'el':el,'user':user}
    return render(request, 'app/home.html' ,params)
# ss
def product_detail(request,pk):
 cid=request.session.get('cid')
 user=Customer.objects.filter(customer_id=cid).first()
 product=Product.objects.get(product_id=pk)
 product=Product.objects.get(product_id=pk)
 su=product.product_price*product.offer.p_discount/100
 d_price=product.product_price-su
 
 print(d_price)
 params={'product':product,'discount':d_price,'user':user}
 return render(request, 'app/productdetail.html', params)

#add in cart
def add_to_cart(request):
 if request.session.has_key('cid'):
        pass
 else:
        return redirect('login')
 if request.GET.get('pro_id'):
    product=Product.objects.get(product_id=request.GET.get('pro_id'))
    su=product.product_price*product.offer.p_discount/100
    d_price=product.product_price-su
    print(su)
    
    
    cart=Cart.objects.create(
       p_id=request.GET.get('pro_id'),
       cus_id=request.session.get('cid'),
       u_price=d_price
    )
    # Order1(d_price=Cart.u_price)
    return redirect('/scart')
 return redirect('/scart')

# add plus or minus 
def scart(request):
    if request.session.has_key('cid'):
        pass
    else:
        return redirect('login')
    cid=request.session.get('cid')
    user=Customer.objects.filter(customer_id=cid)
    if user:
      c=Cart.objects.filter(cus_id=cid)
      pr=[p for p in c]
      price=[]
      for i in pr:
          price.append(i.u_price)
      s=sum(price)
    if request.GET.get('m'):
      cart=Cart.objects.get(c_id=request.GET.get('m'))
      pprice=cart.p.product_price
      cart.quantity=cart.quantity - 1
      cart.save()
      cart.u_price=pprice * cart.quantity
      cart.save()
      return redirect('/scart')
    if request.GET.get('p'):
      cart=Cart.objects.get(c_id=request.GET.get('p'))
      pprice=cart.p.product_price
      cart.quantity=cart.quantity + 1
      cart.save()
      cart.u_price=pprice * cart.quantity
      cart.save()
      return redirect('/scart')
    cid=request.session.get('cid')
    user=Customer.objects.filter(customer_id=cid)
    context={'c':c,'s':s,'user':user}
    return render(request, 'app/scart.html',context)
    
 
#remove cart item
def rcart(request,pk):
    if request.session.has_key('cid'):
        pass
    else:
        return redirect('login')
    cart=Cart.objects.get(c_id=pk)
    cart.delete()
    return redirect('/scart')

def buy_now(request,pid):
  if request.session.has_key('cid'):
        pass
  else:
        return redirect('login')
  cid=request.session.get('cid')
  user=Customer.objects.filter(customer_id=cid).first();
  if user:
      p=Product.objects.get(product_id=pid)
      su=p.product_price*p.offer.p_discount/100
      d_price=p.product_price-su
      context={'p':p ,'u':d_price,'user':user}
  return render(request, 'app/buynow.html',context)

def profile(request):
 if request.session.has_key('cid'):
    pass
 else:
     return redirect('login')
 return render(request, 'app/profile.html')

def address(request):
 if request.session.has_key('cid'):
    pass
 else:
     return redirect('login')
 return render(request, 'app/address.html')

#show orders
def orders(request):
 if request.session.has_key('cid'):
    pass
 else:
     return redirect('login')
 cid=request.session.get('cid')
 user=Customer.objects.get(customer_id=cid)
 op=Order1.objects.filter(customer=user.customer_id)
 params={'orders':op,'user':user}
 
 return render(request, 'app/orders.html',params)

def change_password(request):
    # if request.session.has_key('cid'):
    #     pass
    # else:
    #     return redirect('login')
    # if request.method=="POST":
    #     email=request.POST.get('email');
    #     if (Customer.objects.filter(customer_email=email).exists):
    #             s=Customer.objects.get(customer_email=email)
    #             passw=request.POST.get('pass'),
    #             cpassw=request.POST.get('cpass'),
    #             if(passw==cpassw):
    #                     s.customer_password=passw
    #                     s.save();
    #             else:
    #                 er="both Password not same ";
    #                 context={'er':er}   
    #                 return redirect("changepassword");
    #     else:
    #             er="Email Id is wrong  ";
    #             context={'er':er}
    #             return HttpResponse("email is wrong ")
    # context={}
    # return render(request, 'app/changepassword.html',context)
    pass
#first time category
def cat(request):
    cid=request.session.get('cid')
    user=Customer.objects.filter(customer_id=cid).first()
    cat=Category.objects.all()
    cproduct=Product.objects.all()
    if request.GET.get('search'):
        cproduct=Product.objects.filter(product_name__icontains=request.GET.get('search'))
    params={'cat':cat,'product':cproduct,'user':user}
    return render(request, 'app/cat_wise.html',params)

#category wise 
def readcat(request ,id):
    cid=request.session.get('cid')
    user=Customer.objects.filter(customer_id=cid).first();
    cat=Category.objects.all()
    cats=Category.objects.get(category_id=id)
    cproduct=Product.objects.filter(category=cats)
    params={'category':cat,'cat':cats,'product':cproduct,'user':user}
    return render(request, 'app/readcat.html',params)

def login(request):
 if request.method=='POST':
        email=request.POST['email']
        pass1=request.POST['password']

        if Customer.objects.filter(customer_email=email).exists():

            if Customer.objects.filter(customer_password=pass1).exists():

                data = Customer.objects.filter(customer_email=email,customer_password=pass1 )
    
                for data in data:
                    request.session['cid']=data.customer_id
                    return redirect('home')
                    
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('login')
            else:
                messages.info(request,'Invalid Password')
                return redirect('login')
        else:
            messages.info(request,'Invalid Email', extra_tags='info')
            # messages.success(request,'Success from login', extra_tags='success')
            return redirect('login')
    
 return render(request, 'app/login.html')

def customerregistration(request):
    if request.method=="POST":
        vcustomer=Customer(
            customer_fname=request.POST.get('customerfname'),
            customer_lname=request.POST.get('customerlname'),
            contact_number=request.POST.get('number'),
            customer_gender=request.POST.get('gender'),
            customer_dob=request.POST.get('customerdob'),
            customer_email=request.POST.get('emailid'),
            customer_password=request.POST.get('password'),
            address=request.POST.get('address'),
            customer_pincode=request.POST.get('pincode'))
        vcustomer.save()
        params={'customer':Customer.objects.all(),'msg':'massage successfully '}
        return redirect('login')
    params={'customer':Customer.objects.all(),'msg':'massage successfully '}
    return render(request, 'app/customerregistration (1).html',params)

#cart checkout button pressed
def checkout(request):
  if request.session.has_key('cid'):
    pass
  else:
     return redirect('login')
  cid=request.session.get('cid')
  user=Customer.objects.filter(customer_id=cid).first()
  cart=Cart.objects.filter(cus_id=cid)
#   print(cart)
  context={'c':cart,'user':user}
  return render(request, 'app/checkout.html',context)

# activate when place order of buy now  will be clicked
def bcheckout(request,pid):
  if request.session.has_key('cid'):
    pass
  else:
     return redirect('login')
  cid=request.session.get('cid')
  user=Customer.objects.filter(customer_id=cid).first()
  p=Product.objects.get(product_id=pid)
  su=p.product_price*p.offer.p_discount/100
  d_price=p.product_price-su
  context={'p':p,'u':d_price,'user':user}
  return render(request, 'app/bcheckout.html',context)

# cart orders add 
def payment_done(request):
    cid=request.session.get('cid')
    user=Customer.objects.get(customer_id=cid)
    cart=Cart.objects.filter(cus_id=user.customer_id)
    for i in cart:
       total=i.quantity*i.p.dc_price;
       print(total)
       Order1(customer=user,product=i.p,
             order_quantity=i.quantity,payment="COD",o_state=total).save()
       i.delete()
    return redirect("orders")

# buy now order add
def bpayment_done(request,pid):
    print(pid)
    cid=request.session.get('cid')
    user=Customer.objects.get(customer_id=cid)
    pid=Product.objects.get(product_id=pid)
    s=Order1(customer=user,product=pid,order_quantity=1,payment="COD")
    s.save();
    return redirect("orders")


def aboutus(request):
    cid=request.session.get('cid')
    user=Customer.objects.get(customer_id=cid)
    params={'user':user}
    return render (request,"app/aboutus.html",params);  

def logout(request):
    del request.session['cid']
    return redirect('/')