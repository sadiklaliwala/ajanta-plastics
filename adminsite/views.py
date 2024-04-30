from ast import Del
from email.contentmanager import raw_data_manager
from msilib import add_tables
from statistics import quantiles
from urllib import request
from django.shortcuts import render,HttpResponse ,redirect
from django.http import HttpResponseRedirect
from .models import Admin ,Work ,Purchase ,Supplier,Billing,Category
from .models import Customer,Delivery,Employee,Feedback,Offer
from .models import Order1,Product,Production,RawMaterial,Recycling,Sales,Stock
from .forms import adminform
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.core.serializers import serialize

# admin_login

# def admin_login(request):  
#     if request.method=="POST":
#         name=request.POST.get("username")
#         password=request.POST.get("password")
    
#         if Admin.objects.filter(admin_name=name).exists():
#             if Admin.objects.filter(admin_name=name).exists():
                
#                 admins=Admin.objects.filter(admin_name=name,password=password)
#                 i=0
#                 for ad in admins:
#                     i=i+1
#                     request.session['adminn']=ad.admin_name
#                     return redirect('adminpanel')
#             else:
                
#                 messages.info(request,'Invalid admin', extra_tags='info')
#                 return redirect('admin_login')
            

#         elif Employee.objects.filter(emp_name=name).exists() and  Employee.objects.filter(emp_password=password).exists():
#           print("check")
#           emp=Employee.objects.filter(emp_name=name,emp_password=password)
#           i=0
#           for ad in emp:
#                 i=i+1
#                 request.session['empinn']=ad.emp_name
#                 return redirect('employeepanel')
#           else:
#             messages.info(request,'Invalid password', extra_tags='info')
#             return redirect('admin_login')
#         else:
                
#                 messages.info(request,'Invalid Username', extra_tags='info')
#                 return redirect('admin_login')
#     return render(request,"admin_panel/admin_login.html")


def emp_login(request):
    if request.method=="POST":
        name=request.POST.get("username")
        password=request.POST.get("password")
        if Employee.objects.filter(emp_name=name).exists() and Employee.objects.filter(emp_name=name).exists():
            emp=Employee.objects.filter(emp_name=name,emp_password=password)
            i=0
            for ad in emp:
                i=i+1
                request.session['empinn']=ad.emp_name
                return redirect('employeepanel')
        else:
            messages.info(request,'Invalid Credentials', extra_tags='info')
            return redirect('emp_login')
    return render(request,"employee_panel/admin_login.html")

def admin_login(request):
    if request.method=="POST":
        name=request.POST.get("username")
        password=request.POST.get("password")
        if Admin.objects.filter(admin_name=name).exists() and Admin.objects.filter(admin_name=name).exists():
            admins=Admin.objects.filter(admin_name=name,password=password)
            i=0
            for ad in admins:
                i=i+1
                request.session['adminn']=ad.admin_name
                return redirect('adminpanel')
        else:
            messages.info(request,'Invalid Credentials', extra_tags='info')
            return redirect('admin_login')
    return render(request,"admin_panel/admin_login.html")

def admin_logout(request):
    # request.session.clear()
    logout(request)
    request.session.flush()
    request.session['adminn'] = None
    
    del request.session['adminn']
    return redirect('/')
    # return redirect("admin_login")

#def signin(request):
    # user = Customer.objects.all()

    # if request.method=='POST':
    #     email=request.POST['email']
    #     pass1=request.POST['pass']

    #     if Customer.objects.filter(cust_email=email).exists():

    #         if Customer.objects.filter(cust_password=pass1).exists():

    #             data = Customer.objects.get(cust_email=email)

    #              if data.cust_password == pass1 and data.cust_email == email:
    #                  request.session['cid']=data.cust_id
    #                  return redirect('webcourse')
    #             else:
    #                 messages.info(request, 'Invalid Credentials')
    #                 return redirect('signin')
    #         else:
    #             messages.info(request,'Invalid Password')
    #             return redirect('signin')
    #     else:
    #         messages.info(request,'Invalid Email', extra_tags='info')
    #         # messages.success(request,'Success from login', extra_tags='success')
    #         return redirect('signin')
    # else :
    #     return render(request,'webpages/login.html')


# add_tables
def billing_add(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    if request.method=='POST':
        vcustomer=request.POST.get("customer")
        fvcustomer=Customer.objects.get(customer_id=vcustomer)
        order_id=request.POST.get('order')
        vorder=Order1.objects.get(order_id=order_id)
        vshipping_charges=request.POST.get("shippingcharges")
        vorder_date=request.POST.get("orderdate")
        vtotal=request.POST.get("totalamount")
        vbilling=Billing(customer=fvcustomer,order=vorder,shipping_charges=vshipping_charges,order_date=vorder_date,total=vtotal)
        vbilling.save()
        return render(request , "add_data/billing.html")
    params={'customers_object':Customer.objects.all(),'product_object':Product.objects.all(),'order_object':Order1.objects.all()}
    return render (request ,'add_data/billing.html',params)    

def admin_add(request):
    if request.method == "POST" :
        vadminname=request.POST.get('admin_name')
        vpassword=request.POST.get('password')
        vadmin=Admin(admin_name=vadminname,password=vpassword)
        vadmin.save()
        params={'msg':'massage successfully '}
        return render (request , "add_data/admin_add.html",params)
    return render (request , "add_data/admin_add.html")

def customer_add(request): 
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
        return render (request , "add_data/customer_add.html",params)
    return render (request , "add_data/customer_add.html")

def delivery_add(request):
    if request.method=="POST":
        vcustome=request.POST.get('customer')
        fvcustomer=Customer.objects.get(customer_id=vcustome)
        vaddress =request.POST.get("address")
        vproduct =request.POST.get("product")
        fvproduct =Product.objects.get(product_id=vproduct)
        vd_date =request.POST.get("deliverydate")
        vemp =request.POST.get("employee")
        fvemp=Employee.objects.get(emp_id=vemp)
        vquantity =request.POST.get("quantity")
        vdelivery=Delivery(customer=fvcustomer,address=vaddress,product=fvproduct,d_date=vd_date,emp=fvemp,quantity=vquantity)
        vdelivery.save()
        return redirect('del1')
    params={'customer':Customer.objects.all(),"employee":Employee.objects.all(),'product':Product.objects.all()}
    return render (request , "add_data/delivery_add.html",params)   

def purchase_add(request):
    if request.method =="POST":
        supplier_id=request.POST.get('supplier')
        vsupplier=Supplier.objects.get(sup_id=supplier_id)
        material_name=request.POST.get('materialname')
        vquantity=request.POST.get('quantity')
        vamount=request.POST.get('amount')
        vpur=Purchase(sup=vsupplier,material=material_name,quantity=vquantity,amount=vamount)
        vpur.save()
        supplier_object=Supplier.objects.all()
        params={'suppliers':supplier_object ,'msg':'massage successfully '}
        return redirect('pur')
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'suppliers':Supplier.objects.all()}
    return render (request ,'add_data/purchase_add.html',params)

def work_add(request):
    n=''
    if request.method =="POST":
        vworkname=request.POST.get('workname')
        worksave=Work(work_name = vworkname)
        worksave.save()
        return redirect('workshow')
    params={'n':n}
    return render (request , "add_data/work_add.html", params)

def sup_add(request):
    if request.method=="POST":    
        vsup_name=request.POST.get("s_name")
        vcontact_number=request.POST.get("s_con")
        vsup_address=request.POST.get("s_add")
        vsup_email=request.POST.get("s_email")
        vsupplier=Supplier(sup_name=vsup_name,contact_number=vcontact_number,sup_address=vsup_address,sup_email=vsup_email)
        vsupplier.save()
        return redirect('suppliershow')
    return render(request , "add_data//sup_add.html")

def category_add(request):
    if request.method=="POST":
        vcategory_name=request.POST.get("categoryname")
        vcategory=Category(category_name=vcategory_name)
        vcategory.save()
        return redirect('categoryhow')
    return render (request , "add_data/category_add.html")

def product_add(request):
    if request.method=="POST":
        pr=Product.objects.all()
        fvcategory=request.POST.get("category")
        vcategory=Category.objects.get(category_id=fvcategory)
        vproduct_name=request.POST.get("productname")
        vmaterial=request.POST.get("material")
        vimage=request.FILES.get("image") 
        vproduct_price=request.POST.get("productprice")
        vproduct_weight=request.POST.get("productweight")
        vproduct_quantity=request.POST.get("productquantity")
        vproduct_color=request.POST.get("productcolor")
        vooferid=request.POST.get("Offerid")
        vof=Offer.objects.get(offer_id=vooferid)
        vproduct=Product(category=vcategory,product_name=vproduct_name,material=vmaterial,image=vimage,product_price=vproduct_price,product_weight=vproduct_weight,product_quantity=vproduct_quantity,product_color=vproduct_color,offer=vof)
        vproduct.save()
        params={'category_object':Category.objects.all(),'msg':'massage successfully '}
        return redirect("productshow")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'category':Category.objects.all()}
    return render (request ,'add_data/product_add.html',params)    

def recycling_add(request):
    if request.method=="POST":
        vr_date=request.POST.get("recyclingdate")
        vquantity=request.POST.get("quantity")
        recycling=Recycling(r_date=vr_date,quantity=vquantity)
        recycling.save()
        return redirect('recy')  
    return render(request , "add_data/recycling_add.html")  

def production_add(request):
    if request.method=="POST":
        fproduct=request.POST.get("product")
        vproduct=Product.objects.get(product_id=fproduct)
        vquantity=request.POST.get("quantity")
        vproduction_cost=request.POST.get("productioncost")
        vproduction_date=request.POST.get("productiondate")
        vpolymer=request.POST.get("polymer")
        pquantity=request.POST.get("pquantity")
        ometerial=request.POST.get("ometerial")
        mquantity=request.POST.get("mquantity")
        vproduction=Production(product=vproduct,quantity=vquantity,production_cost=vproduction_cost,production_date=vproduction_date,
        polymer=vpolymer,
        p_quantity=pquantity,
        other_material=ometerial,
        m_quantity=mquantity
        )
        vproduction.save()
        params={'product_object':Product.objects.all(),'msg':'massage successfully '}
        if request.session.has_key('adminn'):
            return redirect("productionshow")        
        else:
            return redirect("temp1")
    params={'product_object':Product.objects.all()}
    return render (request ,'add_data/production_add.html',params)    

def employee_add(request):
    if request.method=="POST":
        fvwork=request.POST.get("work")
        vwork=Work.objects.get(work_id=fvwork)
        vemp_name=request.POST.get("employeename")
        vemp_dob=request.POST.get("employeedob")
        vcontact_number=request.POST.get("contact")
        vemp_salary=request.POST.get("salary")
        vwork_experience=request.POST.get("experience")
        vemp_joindate=request.POST.get("joiningdate")
        vemp_leavedate=request.POST.get("leavedate")
        vqualification=request.POST.get("qualification")
        vemployee=Employee(work=vwork,emp_name=vemp_name,emp_dob=vemp_dob,contact_number=vcontact_number,emp_salary=vemp_salary,work_experience=vwork_experience,emp_joindate=vemp_joindate,emp_leavedate=vemp_leavedate,qualification=vqualification)
        vemployee.save()
        params={'work_object':Work.objects.all(),'msg':'massage successfully '}
        return redirect("employeeshow")
    params={'work_object':Work.objects.all()}
    return render (request ,'add_data/employee.html',params)    

def rawmaterial_add(request):
    if request.method=="POST":
        vsup=request.POST.get("supplier")
        fvsup=Supplier.objects.get(sup_id=vsup)
        vraw_name=request.POST.get("rawmaterialname")
        vraw_quantity=request.POST.get("quantity")
        rawmaterial=RawMaterial(sup=fvsup,raw_name=vraw_name,raw_quantity=vraw_quantity)
        rawmaterial.save()
        return redirect('rwm')
    params={'supplier_object': Supplier.objects.all}
    return render(request , "add_data/rawmaterial_add.html",params)

def order_add(request):
    if request.method=="POST":
        fvcustomer=request.POST.get("customer")
        vcustomer=Customer.objects.get(customer_id=fvcustomer)
        vorder_date=request.POST.get("orderdate")
        vproduct=request.POST.get("product")
        fvproduct=Product.objects.get(product_id=vproduct)
        vorder_quantity=request.POST.get("order_quantity")
        vpayment=request.POST.get("payment")
        vorder1=Order1(customer=vcustomer,order_date=vorder_date,product=fvproduct,order_quantity=vorder_quantity,payment=vpayment)
        vorder1.save()
        customer_object=Customer.objects.all()
        product_object=Product.objects.all()
        params={'customer_object':Customer.objects.all(),'product_object':Product.objects.all(),'msg':'massage successfully '}
        return redirect("ord")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'customer_object':Customer.objects.all(),'product_object':Product.objects.all()}
    return render (request ,'add_data/order.html',params)

def feedback_add(request):
    if request.method == "POST" : 
        vf_date=request.POST.get("f_date") 
        vfeedback=request.POST.get("feedback") 
        vcustomer=request.POST.get("customer")
        fvcustomer=Customer.objects.get(customer_id=vcustomer)
        customer_object=Customer.objects.all()
        feedback=Feedback(f_date=vf_date,feedback=vfeedback,customer=fvcustomer)
        feedback.save()
        params={'msg':'massage successfully ','customer_object':Customer.objects.all()}
        return render (request , "add_data/feedback_add.html",params)
    params={'msg':'massage successfully ','customer_object':Customer.objects.all()}
    return render (request , "add_data/feedback_add.html")

def offer_add(request):
    if request.method == "POST" :
        vstart_date=request.POST.get("sdate")
        vend_date=request.POST.get("edate")
        vdescription=request.POST.get("description")
        offer=Offer(start_date=vstart_date,end_date=vend_date,description=vdescription)
        offer.save()
        params={'msg':'massage successfully '}
        return redirect("offershow")
    return render (request , "add_data/offer_add.html")

def sales_add(request):
    if request.method=="POST":
        vsales_date=request.POST.get("salesdate")
        vproduct=request.POST.get("product")
        fvproduct=Product.objects.get(product_id=vproduct)
        vquantity=request.POST.get("quantity")
        vsales=Sales(sales_date=vsales_date,product=fvproduct,quantity=vquantity)
        vsales.save()
        params={'product_object':Product.objects.all(),'msg':'massage successfully '}
        return redirect ("sa")
    params={'product_object':Product.objects.all()}
    return render (request ,'add_data/sales.html',params)

def stock_add(request):
    if request.method =="POST":
        vproduct=request.POST.get("product")
        fvproduct=Product.objects.get(product_id=vproduct)
        vr_id=request.POST.get("rawmaterial_id")
        # fvr_id=RawMaterial.objects.get(raw_id=vr_id)
        vquantity=request.POST.get("quantity")
        vmaterial_quantity=request.POST.get("materialquantity")
        stock=Stock(product=fvproduct,r_id=vr_id,quantity=vquantity,material_quantity=vmaterial_quantity)
        stock.save()
        # return redirect("stockshow")
        params={'rawMaterial_object':RawMaterial.objects.all(),'product_object':Product.objects.all()}
        return redirect('sto')
    params={'rawmaterial_object':RawMaterial.objects.all(),'product_object':Product.objects.all()}
    return render (request ,'add_data/stock.html',params)
#update
def work_update(request,pk):
    if request.method=="POST":
        # s=Work.objects.get(work_id=pk)
        vworkname=request.POST.get("workname")
        worksave=Work(work_id=pk,work_name = vworkname)
        worksave.save()
        return redirect ("workshow")
    params={'work_object':Work.objects.get(work_id=pk)}
    return render (request , "update_data/work_update.html",params)

def update_supplier(request,pk):
    if request.method=="POST":
        # s=Work.objects.get(work_id=pk)
        vsup_name=request.POST.get("s_name")
        vcontact_number=request.POST.get("s_con")
        vsup_address=request.POST.get("s_add")
        vsup_email=request.POST.get("s_email")
        vsupplier=Supplier(sup_id=pk,sup_name=vsup_name,contact_number=vcontact_number,sup_address=vsup_address,sup_email=vsup_email)
        vsupplier.save()
        return redirect ("suppliershow")
    params={'supplier_object':Supplier.objects.get(sup_id=pk)}
    return render (request , "update_data/update_supplier.html",params)

def update_stock(request,pk):
    if request.method =="POST":
        s=Stock.objects.get(stock_id=pk)
        vproduct=request.POST.get("product1")
        s.product=Product.objects.get(product_id=vproduct)
        s.quantity=request.POST.get("quantity")
        s.r_id=request.POST.get("raw_id")
        # s.r_id=RawMaterial.objects.get(raw_id=vraw_id)
        s.material_quantity=request.POST.get("materialquantity")
        # stock=Stock( stock_id=pk,product=fvproduct,quantity=vquantity,material_quantity=vmaterial_quantity)
        # stock.save()
        s.save()
        params={'rawMaterial_object':RawMaterial.objects.all(),'product_object':Product.objects.all()}
        return redirect('sto')
    params={'rawMaterial_object':RawMaterial.objects.all(),'product_object':Product.objects.all(),"stock_object": Stock.objects.get(stock_id=pk)}
    return render (request ,"update_data/update_stock.html",params)

def update_sales(request,pk):
    if request.method=="POST":
        s=Sales.objects.get(sales_id=pk)
        vproduct=request.POST.get("product")
        s.product=Product.objects.get(product_id=vproduct)
        s.quantity=request.POST.get("quantity")
        s.save()
        params={'product_object':Product.objects.all(),'msg':'massage successfully '}
        return redirect("sa")
    params={'product_object':Product.objects.all(),'sales_object':Sales.objects.get(sales_id=pk)}
    return render (request ,'update_data/update_sales.html',params)

def update_rawmaterial(request,pk):
    if request.method=="POST":
        s=RawMaterial.objects.get(raw_id=pk)
        vsup=request.POST.get("supplier")   
        s.sup=Supplier.objects.get(sup_id=vsup)
        s.raw_name=request.POST.get("rawmaterialname")
        s.raw_quantity=request.POST.get("quantity1")
        print(s.raw_quantity)
        print(s.sup)
        # rawmaterial=RawMaterial(raw_id=pk,sup=fvsup,raw_name=vraw_name,raw_quantity=vraw_quantity)
        # rawmaterial.save()
        s.save()
        return redirect('rwm')
    params={'supplier_object': Supplier.objects.all,'rawmaterial_object':RawMaterial.objects.get(raw_id=pk)}
    return render(request , "update_data/update_rawmaterial.html",params)


def update_purchase(request,pk):
    if request.method =="POST":
        s=Purchase.objects.get(purchase_id=pk)
        supplier_id=request.POST.get('supplier')
        s.sup=Supplier.objects.get(sup_id=supplier_id)
        s.material=request.POST.get('materialname')
        s.quantity=request.POST.get('quantity')
        s.amount=request.POST.get('amount')
        # vpur=Purchase(purchase_id=pk,sup=vsupplier,material=material_name,quantity=vquantity,amount=vamount)
        # vpur.save()
        s.save()
        supplier_object=Supplier.objects.all()
        params={'suppliers':supplier_object ,'msg':'massage successfully '}
        return redirect("pur")
    params={'suppliers':Supplier.objects.all(),'purchase_object':Purchase.objects.get(purchase_id=pk)}
    return render (request ,'update_data/update_purchase.html',params)

def update_billing(request,pk):
    if request.method =="POST":
        customer=request.POST.get('customer')
        vcustomer=Customer.objects.get(customer_id=customer)
        order_id=request.POST.get('order')
        vorder=Order1.objects.get(order_id=order_id)
        scharges=request.POST.get('shippingcharges')
        odate=request.POST.get('orderdate')
        tamount=request.POST.get('totalamount')
        vpur=Billing(bill_id=pk,customer=vcustomer,order=vorder,shipping_charges=scharges,order_date=odate,total=tamount)
        vpur.save()
        customer_object=Customer.objects.all()
        return redirect("billingshow")
        params={'customerss':customer_object ,'msg':'massage successfully '}
    params={'customers_object':Customer.objects.all(),'order_object':Order1.objects.all(), 'billing_object':Billing.objects.get(bill_id=pk)}
    return render (request ,'update_data/update_billing.html',params)

def update_employee(request,pk):
    if request.method=="POST":
        s=Employee.objects.get(emp_id=pk)
        # fvwork=request.POST.get("work")
        s.work=Work.objects.get(work_id=request.POST['work'])
        s.emp_name=request.POST["employeename"]
        s.contact_number=request.POST["contact"]
        s.emp_salary=request.POST["salary"]
        s.work_experience=request.POST["experience"]
        
        s.qualification=request.POST["qualification"]
        s.save()
        params={'work_object':Work.objects.all(),'msg':'massage successfully '}
        return redirect("employeeshow")
    params={'work_object':Work.objects.all(),'employee_object':Employee.objects.get(emp_id=pk)}
    return render (request ,'update_data/update_employee.html',params)    



def update_admin(request,pk):
    if request.method=="POST":
        vadminname=request.POST.get("admin_name")
        vadimnpassword=request.POST.get("password")
        adminsave=Admin(admin_id=pk,admin_name=vadminname,password=vadimnpassword)
        adminsave.save()
        return redirect("adminpanel")
    params={'admn_object':Admin.objects.get(admin_id=pk)}
    return render (request , "update_data/update_admin.html",params)


def update_customer(request,pk):
    if request.method=="POST":
        s=Customer.objects.get(customer_id=pk)
        s.customer_fname=request.POST.get("customerfname")
        s.customer_lname=request.POST.get("customerlname")
        s.contact_number=request.POST.get("number")
        s.customer_email=request.POST.get("emailid")
        s.customer_gender=request.POST.get("gender")
        s.customer_dob=request.POST.get("customerdob")
        s.customer_password=request.POST.get("password")
        s.address=request.POST.get("address")
        s.customer_pincode=request.POST.get("pincode")
        # vcustomer=Customer(customer_id=pk,customer_fname=vcust_fname,customer_lname=vcust_lname,contact_number=vcustno,customer_email=vcust_email,customer_gender=vcust_gender,customer_dob=vdob,customer_password=vpassword,address=vaddress,customer_pincode=vpincode)
        # vcustomer.save()
        s.save();
        return redirect ("customershow")
    params={'customer_object':Customer.objects.get(customer_id=pk)}
    return render (request , "update_data/update_customer.html",params)

'''def update_offer(request,pk):
    if request.method=="POST":
        sadte=request.POST.get("start_date")
        edate=request.POST.get("end_date")
        descr=request.POST.get("description")
        ofer=Offer(offer_id=pk,start_date=sdate,end_date=edate,description=descr)
        ofer.save()'''

def update_category(request,pk):
    if request.method=="POST":
        vcategoryname=request.POST.get("categoryname")
        catsave=Category(category_id=pk,category_name = vcategoryname)
        catsave.save()
        return redirect ("categoryhow")
    params={'category_object':Category.objects.get(category_id=pk)}
    return render (request , "update_data/update_category.html",params)

def update_offer(request,pk):
    if request.method=="POST":
        offersdate=request.POST.get("start_date")
        offeredate=request.POST.get("end_date")
        offerdescription=request.POST.get("description")
        catsave=Offer(offer_id=pk,start_date=offersdate,end_date=offeredate,description=offerdescription)
        catsave.save()
        return redirect ("offershow")
    params={'offer_object':Offer.objects.get(offer_id=pk)}
    return render (request , "update_data/update_offer.html",params)


def update_recycle(request,pk):
    if request.method=="POST":
        s=Recycling.objects.get(r_id=pk)
        s.quantity=request.POST.get("quantity")
        s.save()
        return redirect ("recy")
    params={'recycling_object':Recycling.objects.get(r_id=pk)}
    return render (request , "update_data/update_recycle.html",params)

def update_product(request,pk):
    if request.method=="POST":
        s=Product.objects.get(product_id=pk)
        category_id=request.POST.get("category")
        s.category=Category.objects.get(category_id=category_id)
        s.product_name=request.POST.get("productname")
        s.material=request.POST.get("material")
        vimage=request.FILES.get("image")
        if vimage:
            s.image=vimage
        s.product_price=request.POST.get("productprice")
        s.product_weight=request.POST.get("productweight")
        s.product_quantity=request.POST.get("productquantity")
        s.product_color=request.POST.get("productcolor")
        # vroduct=Product(product_id=pk,category=vwork,product_name=vname,material=vmaterial,image=vimage,product_price=vprice,product_weight=vweight,product_quantity=vquantity,product_color=vcolor)
        # vroduct.save()
        s.save()
        return redirect ("productshow")
    params={'Category':Category.objects.all(),'product_object':Product.objects.get(product_id=pk)}
    return render (request , "update_data/update_product.html",params)

'''def update_recycling(request,pk):
    if request.method=="POST":
        rdate=request.POST.get("recyclingdate")
        rquantity=request.POST.get("quantity")
        rsave=Category(r_id=pk,r_date=rdate,quantity=rquantity)
        rsave.save()
        return redirect ("recycleshow")
    params={'recycling_object':Recycling.objects.get(r_id=pk)}
    return render (request , "update_data/update_recycle.html",params)'''

def update_delivery(request,pk):
    if request.method=="POST":
        s=Delivery.objects.get(d_id=pk)
        customer_id=request.POST.get("customer")
        s.customer=Customer.objects.get(customer_id=customer_id)
        s.address=request.POST.get("address")
        vproduct_id=request.POST.get("product")
        vp=Product.objects.get(product_id=vproduct_id)
        s.product=vp
        s.d_date=request.POST.get("d_date")
        emp_id=request.POST.get("employee")
        ve=Employee.objects.get(emp_id=emp_id)
        s.emp=ve
        s.quantity=request.POST.get("quantity")
        s.save()
        return redirect("del1")
    params={'customer':Customer.objects.all(),'product':Product.objects.all(),'employee':Employee.objects.all(),'delivery_object':Delivery.objects.get(d_id=pk)}
    return render (request , "update_data/update_delivery.html",params)

def update_order(request,pk):
    if request.method=="POST":
        customer_id=request.POST.get("customer")
        cust=Customer.objects.get(customer_id=customer_id)
        odate=request.POST.get("orderdate")
        product_id=request.POST.get("product")
        prod=Product.objects.get(product_id=product_id)
        quantity=request.POST.get("order_quantity")
        payment=request.POST.get("payment")
        order=Order1(order_id=pk,customer=cust,order_date=odate,product=prod,order_quantity=quantity,payment=payment)
        order.save()
        return redirect("ord")
    params={'customer_object':Customer.objects.all(),'product_object':Product.objects.all(),'order_object':Order1.objects.get(order_id=pk)}
    return render (request , "update_data/update_order.html",params)

def update_production(request,pk):
    if request.method=="POST":
        product_id=request.POST.get("product")
        prod=Product.objects.get(product_id=product_id)
        pquantity=request.POST.get("quantity")
        cost=request.POST.get("production_cost")
        date=request.POST.get("production_date")
        production=Production(production_id=pk,product=prod,quantity=pquantity,production_cost=cost,production_date=date)
        production.save()
        return redirect("productionshoh")
    params={'product_object':Product.objects.all(),'production_object':Production.objects.get(production_id=pk)}
    return render (request , "update_data/update_production.html",params)

def admindasheboard(request ):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    user_seassion=request.session.get('adminn')
    admin_user=Admin.objects.filter(admin_name=user_seassion).first()
    params={'admin_user':admin_user}
    return render (request , "admin_panel/admin_deshboard.html",params)

def adminbase(request ):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    n=request.session.get('cid')
    print(n)
    return render (request , "basepage.html")

def adminshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    # if request.method == "GET":
    #     st = request.GET.get('search')
    #     if st is not None:
    #         result = Admin.objects.filter(admin_name=st)

    admin=Admin.objects.all()
    params ={'admin_object':admin}
    return render (request , "show_data/adminshow.html",params)

def billingshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    billing=Billing.objects.all()
    params ={'billing':billing}
    return render (request , "show_data/billshow.html",params)

def categoryhow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    category=Category.objects.all()
    if request.GET.get('search'):
        category=Category.objects.filter(category_name__icontains=request.GET.get('search'))
    params ={'category':category}
    return render (request , "show_data/categoryshow.html",params)

def customershow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    user_seassion=request.session.get('adminn')
    admin_user=Admin.objects.filter(admin_name=user_seassion).first()
    customer=Customer.objects.all()
    if request.GET.get('search'):
        customer=Customer.objects.filter(customer_fname__icontains=request.GET.get('search'))
    # if request.method == "GET":
    #     st = request.GET.get('search')
    #     if st is not None:
    #         customer = Customer.objects.filter(customer_fname=st)
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     # If the request is an AJAX request, return JSON response
    #     data = serialize('json', customer)
    #     return JsonResponse(data, safe=False)
    params ={'customer':customer ,'admin_user':admin_user}
    return render (request , "show_data/customershow.html",params)

def deliveryshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    delivery=Delivery.objects.all()
    params ={'delivery':delivery}
    return render (request , "show_data/deliveryshow.html",params)

def employeeshow(request):
    employee=Employee.objects.all()
    if request.GET.get('search'):
        employee=Employee.objects.filter(emp_name__icontains=request.GET.get('search'))
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    params ={'employee':employee}
    return render (request , "show_data/employeeshow.html",params)

def order1show(request):
    order1=Order1.objects.all()
    if request.GET.get('search'):
        order1=Order1.objects.filter(order_id__icontains=request.GET.get('search'))
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    
    params ={'order1':order1}
    return render (request , "show_data/ordershow.html",params)

def productshow(request):
    ss=Product.objects.all()
    if request.GET.get('search'):
        ss=Product.objects.filter(product_name__icontains=request.GET.get('search'))
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    params ={'product':ss}
    return render (request , "show_data/productshow.html",params)

def productionshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    production=Production.objects.all()
    prod1=Production.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    prod2=Production.objects.aggregate(Sum('production_cost')).get('production_cost__sum',0.00)
    
    params ={'production':production,'prod1':prod1,'prod2':prod2}
    return render (request , "show_data/productionshow.html",params)
        
def stockshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    stock=Stock.objects.all()
    params ={'stock':stock}
    return render (request , "show_data/stockshow.html",params)

def salesshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    sales=Sales.objects.all()
    sal=Sales.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    params ={'sales':sales,'sales_count':sal}
    return render (request , "show_data/salesshow.html",params)

def suppliershow(request):
    supplier=Supplier.objects.all()
    if request.GET.get('search'):
        supplier=Supplier.objects.filter(sup_name__icontains=request.GET.get('search'))
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    params ={'supplier':supplier}
    return render (request , "show_data/suppliershow.html",params)

def workshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    works =Work.objects.all()
    if request.GET.get('search'):
        works=Work.objects.filter(work_name__icontains=request.GET.get('search'))
    params ={'works':works}
    return render (request , "show_data/workshow.html",params)

def purchaseshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    vpurchase =Purchase.objects.all()
    purc1 =Purchase.objects.aggregate(Sum('amount')).get('amount__sum',0.00)
    params ={'vpurchase':Purchase.objects.all(),'purc1':purc1}
    return render (request , "show_data/purchaseshow.html",params)

def rawmaterialshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    rawMaterial=RawMaterial.objects.all()
    raw12=RawMaterial.objects.aggregate(Sum('raw_quantity')).get('raw_quantity__sum')
    if request.GET.get('search'):
        rawMaterial=RawMaterial.objects.filter(raw_name__icontains=request.GET.get('search'))
    params ={'rawmaterial':rawMaterial,'raw12':raw12}
    return render (request , "show_data/rawmaterialshow.html",params)

def recyclingshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    recycling=Recycling.objects.all()
    recycle1=Recycling.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    params ={'recycling':recycling,'recycle1':recycle1}
    return render (request , "show_data/recyclingshow.html",params)

def feedbackshow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    feedback=Feedback.objects.all()
    params ={'feedback':feedback}
    return render (request , "show_data/feedbackshow.html",params)

def offershow(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    offer=Offer.objects.all()
    params ={'offer':offer}
    return render (request , "show_data/offershow.html",params) 

def delete_admin(request,admin_id):
    
    deletestaff=Admin.objects.get(admin_id=admin_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("adminshow")

def delete_billing(request,bill_id):    
    deletestaff=Billing.objects.get(bill_id=bill_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("billingshow")

def delete_category(request,category_id):
    deletestaff=Category.objects.get(category_id=category_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("categoryhow")

def delete_customer(request,customer_id):
    deletestaff=Customer.objects.get(customer_id=customer_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("customershow")

def delete_delivery(request , d_id):
    deletestaff=Delivery.objects.get(d_id=d_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("del1")

def delete_employee(request , emp_id):
    deletestaff=Employee.objects.get(emp_id=emp_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("employeeshow")

def delete_feedback(request , f_id):
    deletestaff=Feedback.objects.get(f_id=f_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("feedbackshow")

def delete_offer(request , offer_id):
    deletestaff=Offer.objects.get(offer_id=offer_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("offershow")

def delete_order(request , order_id):
    deletestaff=Order1.objects.get(order_id=order_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("ord")

def delete_production(request , production_id):
    deletestaff=Production.objects.get(production_id=production_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("productionshow")

def delete_product(request , product_id):
    deletestaff=Product.objects.get(product_id=product_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("productshow")

def delete_purchase(request , purchase_id):
    deletestaff=Purchase.objects.get(purchase_id=purchase_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("pur")

def delete_rawmaterial(request , raw_id):
    deletestaff=RawMaterial.objects.get(raw_id=raw_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect('rwm')

def delete_recycle(request , r_id):
    deletestaff=Recycling.objects.get(r_id=r_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("recy")

def delete_sale(request , sales_id):
    deletestaff=Sales.objects.get(sales_id=sales_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("sa")

def delete_stock(request , stock_id):
    deletestaff=Stock.objects.get(stock_id=stock_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("stockshow")

def delete_supplier(request , sup_id):
    deletestaff=Supplier.objects.get(sup_id=sup_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("suppliershow")

def delete_work(request , work_id):
    deletestaff=Work.objects.get(work_id=work_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("workshow")

def adminpanel(request):
    if request.session.has_key('adminn'):
        pass
    else:
        return redirect('admin_login')
    adm=Admin.objects.all().count()
    bill=Billing.objects.all().count()
    cate=Category.objects.all().count()
    cust=Customer.objects.all().count()
    deliv=Delivery.objects.all().count()
    empl=Employee.objects.all().count()
    feed=Feedback.objects.all().count()
    off=Offer.objects.all().count()
    or1=Order1.objects.all().count()
    prd=Product.objects.all().count()
    prod=Production.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    purc =Purchase.objects.aggregate(Sum('amount')).get('amount__sum',0.00)
    raw=RawMaterial.objects.aggregate(Sum('raw_quantity')).get('raw_quantity__sum')
    recycle=Recycling.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    sal=Sales.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    stoc=Stock.objects.all().count()
    supp=Supplier.objects.all().count()
    work =Work.objects.all().count()
    user_seassion=request.session.get('adminn')
    admin_user=Admin.objects.filter(admin_name=user_seassion).first()
    # print(admin_user.admin_name)
    context={'admin_count':adm,'bill_count':bill,'category_count':cate,'customer_count':cust,'delivery_count':deliv,
    'employee_count':empl,'feedback_count':feed,'offer_count':off,'order_count':or1,'product_count':prd,
    'production_count':prod,'purchase_count':purc,'raw_count':raw,'recycle_count':recycle,
    'sales_count':sal,'stock_count':stoc,'supplier_count':supp,'work_count':work,'admin_user':admin_user}
    return render(request,"admin_panel/admin.html",context)

def emppanel(request):
    if request.session.has_key('empinn'):
        pass
    else:
        return redirect('admin_login')
    
    deliv=Delivery.objects.all().count()
    or1=Order1.objects.all().count()
    prod=Production.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    raw=RawMaterial.objects.aggregate(Sum('raw_quantity')).get('raw_quantity__sum')
    recycle=Recycling.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    sal=Sales.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    context={'delivery_count':deliv,'order_count':or1,'production_count':prod,'raw_count':raw,
    'recycle_count':recycle,'sales_count':sal,}
    return render(request,"employee_panel/employee_panel.html",context)

def login(request):
  return render (request , "customer_logreg/login.html" )

def registration(request):
    return render (request,"customer_logreg/registration.html")
  
def prodc(request):
    if request.session.has_key('empinn'):
        pass
    else:
        return redirect('emp_login')
    
    production1=Production.objects.all()
    prodtotal=Production.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    prodt=Production.objects.aggregate(Sum('production_cost')).get('production_cost__sum',0.00)
    params ={'production1':production1,'prodtotal':prodtotal,'prodt':prodt}
    return render (request,"emp/production1.html",params)

def ord(request):
    if request.session.has_key('empinn'):
        pass
    else:
        return redirect('emp_login')
    
    order2=Order1.objects.all()
    params ={'order2':order2}
    return render (request,"emp/order_show.html",params)

def pur(request):
    if request.session.has_key('empinn'):
        pass
    else:
        return redirect('emp_login')
    
    vpurchase1 =Purchase.objects.all()
    purctotal =Purchase.objects.aggregate(Sum('amount')).get('amount__sum',0.00)
    params ={'vpurchase1':vpurchase1,'purctotal':purctotal}
    return render (request , "emp/purchase_show.html",params)

def rwm(request):
    if request.session.has_key('empinn'):
        pass
    else:
        return redirect('emp_login')
    
    rawMaterial1=RawMaterial.objects.all()
    rawtotal=RawMaterial.objects.aggregate(Sum('raw_quantity')).get('raw_quantity__sum')
    if request.GET.get('search'):
        rawMaterial1=RawMaterial.objects.filter(raw_name__icontains=request.GET.get('search'))
    params ={'rawmaterial1':rawMaterial1,'rawtotal':rawtotal}
    return render (request , "emp/raw_show.html",params)

def recy(request):
    if request.session.has_key('empinn'):
        pass
    else:
        return redirect('emp_login')
    
    recycling1=Recycling.objects.all()
    recycletotal=Recycling.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    params ={'recycling1':recycling1,'recycletotal':recycletotal}
    return render (request , "emp/recycling_show.html",params)

def feed(request):
    feedback1=Feedback.objects.all()
    params ={'feedback1':feedback1}
    return render (request , "emp/feedback_show.html",params)

def sto(request):
    stock1=Stock.objects.all()
    params ={'stock1':stock1}
    return render (request , "emp/stock_show.html",params)

def sa(request):
    sales1=Sales.objects.all()
    saletotal=Sales.objects.aggregate(Sum('quantity')).get('quantity__sum',0.00)
    params ={'sales1':sales1,'saletotal':saletotal}
    return render (request , "emp/sales_show.html",params)

def del1(request):
    delivery1=Delivery.objects.all()
    params ={'delivery1':delivery1}
    return render (request , "emp/delivery_show.html",params)


def elog(request):
    del request.session['empinn']
    return redirect('/')


    # return render(request,'delete.html',{'Enrolled':ans})

    # return render (request , "delete.html" ,{'ans' : ans})

# add this in your html file
#      <p class ="table_cell">
#      <a href="/editcust/{{i.cust_id}}">
#      <span class="icon"><i class="fas fa-edit"></i></span>
#      </a>
                              
# //update query example 
# def auditionupdate(request,audition_id):
#     if request.session.has_key('adminn'):
#         pass
#     else:
#         return redirect('/adminlogin/')
    
#     ff=Audition.objects.all()
#     ff=Audition.objects.get(audition_id=audition_id)
#     ff.audition_type=request.POST['audition_type']
#     ff.cand_fname=request.POST['cand_fname']
#     ff.cand_height=request.POST['cand_height']
#     ff.cand_weight=request.POST['cand_weight']
#     ff.cand_qual=request.POST['cand_qual']
#     ff.mediafile=request.POST['mediafile']
    
#     ff.save()
