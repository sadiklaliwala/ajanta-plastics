"""
URL configuration for apd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from adminsite import views
from employee import urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('employee',include('employee.urls')),
    path('',include('customer.urls')),
    # path('',views.home,name='home'),
    # path('admin/', admin.site.urls),
    path('admindasheboard/', views.admindasheboard,name="admindasheboard"),
    # path('admin/',views.admin_panel, name ='admin_panel'),
    # Login 
    path("admin_login",views.admin_login,name="admin_login"),
    path("emp_login",views.emp_login,name="emp_login"),
    path("admin_logout",views.admin_logout,name="admin_logout"),
    
     #all data show 
    #   path('show/',views.show, name ="show"),f
      path('adminbase' ,views.adminbase , name= "adminbase"),
      path('bill_show',views.billingshow, name="billingshow"),
      path('admin_show', views.adminshow, name="adminshow"),
      path('category_show', views.categoryhow, name="categoryhow"),
      path('customer_show', views.customershow, name="customershow"),
      path('delivery_show', views.deliveryshow, name="deliveryshow"),
      path('employee_show', views.employeeshow, name="employeeshow"),
      path('feedback_show', views.feedbackshow, name="feedbackshow"),
      path('offer_show', views.offershow, name="offershow"),   
      path('order_show', views.order1show, name="ordershow"),
      path('production_show', views.productionshow, name="productionshow"),
      path('product_show', views.productshow, name="productshow"),
      path('purchase_show', views.purchaseshow, name="purchaseshow"),
      path('rawmaterial_show', views.rawmaterialshow, name="rawmaterialshow"),
      path('recycling_show', views.recyclingshow, name="recyclingshow"),
      path('sales_show', views.salesshow, name="salesshow"),
      path('stock_show', views.stockshow, name="stockshow"),
      path('supplier_show', views.suppliershow, name="suppliershow"),
      path('work_show', views.workshow, name="workshow"),

    #   add
      path('admin_add/',views.admin_add, name ="admin_add"),
      path('category_add', views.category_add ,name="category_add"),
      path('customer_add/',views.customer_add, name ="customer_add"),
      path('delivery_add', views.delivery_add ,name="delivery_add"),
      path('purchase_add/',views.purchase_add, name ='purchase_add'),
      path('sup_add/',views.sup_add, name ="sup_add"), 
      path('work_add/',views.work_add, name ='work_add'),
      path('employee_add' ,views.employee_add,name="employee"),
      path('order_add' ,views.order_add,name="order_add "),
      path('billing_add' ,views.billing_add,name="billing"),
      path('feedback_add' ,views.feedback_add,name="feedback_add"),
      path('offer_add' ,views.offer_add,name="offer_add"),
      path('rawmaterial_add',views.rawmaterial_add,name="rawmaterial_add"),
      path('recycling_add',views.recycling_add,name="recycling_add"),
      path('production_add',views.production_add,name="production_add"),
      path('product_add',views.product_add,name="product_add"),
      path('sales_add',views.sales_add,name="sales"),
      path("stock_add", views.stock_add, name="stock_add"),
      
    #  update   
      #path('work_update/<int:pk>',views.workform_update, name ='workform_update'),
      path('work_update/<int:pk>',views.work_update, name ='work_update'),
      path("update_supplier/<int:pk>" , views.update_supplier, name="update_supplier"),
      path("update_stock/<int:pk>" , views.update_stock, name="update_stock"),
      path("update_sales/<int:pk>" , views.update_sales, name="update_sales"),
      path("update_rawmaterial/<int:pk>" , views.update_rawmaterial, name="update_rawmaterial"),
      path("update_purchase/<int:pk>" , views.update_purchase, name="update_purchase"),
      path("update_billing/<int:pk>" , views.update_billing, name="update_billing"),
      path("update_customer/<int:pk>" , views.update_customer, name="update_customer"),
      path("update_employee/<int:pk>" , views.update_employee, name="update_employee"),
      path("update_offer/<int:pk>" , views.update_offer, name="update_offer"),
      path("update_recycle/<int:pk>" , views.update_recycle, name="update_recycle"),
      path("update_product/<int:pk>" , views.update_product, name="update_product"),
      path("update_admin/<int:pk>" , views.update_admin, name="update_admin"),
      path("update_category/<int:pk>" , views.update_category, name="update_category"),
      path("update_delivery/<int:pk>" , views.update_delivery, name="update_delivery"),
      path("update_order/<int:pk>" , views.update_order, name="update_order"),
      path("update_production/<int:pk>" , views.update_production, name="update_production"),
      
      

      #delete
      path('delete_admin/<int:admin_id>', views.delete_admin ,name="delete_admin"),
      path('delete_billing/<int:bill_id>', views.delete_billing ,name="delete_billing"),
      path('delete_category/<int:category_id>', views.delete_category ,name="delete_category"),
      path('delete_customer/<int:customer_id>', views.delete_customer ,name="delete_customer"),
      path('delete_delivery/<int:d_id>', views.delete_delivery ,name="delete_delivery"),
      path('delete_employee/<int:emp_id>', views.delete_employee ,name="delete_employee"),
      path('delete_feedback/<int:f_id>', views.delete_feedback ,name="delete_feedback"),
      path('delete_offer/<int:offer_id>', views.delete_offer ,name="delete_offer"),
      path('delete_order/<int:order_id>', views.delete_order ,name="delete_order"),
      path('delete_production/<int:production_id>', views.delete_production ,name="delete_production"),
      path('delete_product/<int:product_id>', views.delete_product ,name="delete_product"),
      path('delete_purchase/<int:purchase_id>', views.delete_purchase ,name="delete_purchase"),
      path('delete_rawmaterial/<int:raw_id>', views.delete_rawmaterial ,name="delete_rawmaterial"),
      path('delete_recycle/<int:r_id>', views.delete_recycle ,name="delete_recycle"),
      path('delete_sale/<int:sales_id>', views.delete_sale ,name="delete_sale"),
      path('delete_stock/<int:stock_id>', views.delete_stock ,name="stock"),
      path('delete_supplier/<int:sup_id>', views.delete_supplier ,name="delete_supplier"),
      path('delete_work/<int:work_id>', views.delete_work ,name="delete_work"),

    
      path('adminpanel',views.adminpanel,name="adminpanel"),
      path('emppanel',views.emppanel,name="employeepanel"),
      path('login',views.login,name="customerlogin"),
      path('elog',views.elog,name="elog"),
      path('registration',views.registration,name="customerregistration"),
      path('prod_show123' ,views.prodc , name= "temp1"),
      path('ord_show',views.ord, name='ord'),
      path('sal_show', views.sa, name="sa"),
      path('pur_show', views.pur, name="pur"),
      path('sto_show', views.sto, name="sto"),
      path('del_show', views.del1, name="del1"),
      path('rwm_show', views.rwm, name="rwm"),
      path('feed_show', views.feed, name="feed"),
      path('recy_show', views.recy, name="recy"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

