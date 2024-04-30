# This is an auto-generated Django model module.                                                                                                           
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(db_column='Admin_id', primary_key=True)  # Field name made lowercase.
    admin_name = models.CharField(db_column='Admin_name', max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Billing(models.Model):
    bill_id = models.AutoField(db_column='Bill_id', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey('Order1', models.DO_NOTHING, db_column='Order_id', blank=True, null=True)  # Field name made lowercase.
    shipping_charges = models.FloatField()
    order_date = models.DateField(db_column='Order_date')  # Field name made lowercase.
    total = models.FloatField(db_column='Total')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billing'

class Cart(models.Model):
    c_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    cus_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    u_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    category_id = models.AutoField(db_column='Category_id', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_name', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_id', primary_key=True)  # Field name made lowercase.
    customer_fname = models.CharField(db_column='Customer_fname', max_length=15)  # Field name made lowercase.
    customer_lname = models.CharField(db_column='Customer_lname', max_length=15)  # Field name made lowercase.
    contact_number = models.IntegerField()
    customer_gender = models.CharField(db_column='Customer_gender', max_length=6)  # Field name made lowercase.
    customer_dob = models.DateField(db_column='Customer_dob')  # Field name made lowercase.
    customer_email = models.CharField(db_column='Customer_email', max_length=30)  # Field name made lowercase.
    customer_password = models.IntegerField(db_column='Customer_password')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    customer_pincode = models.IntegerField(db_column='Customer_pincode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Delivery(models.Model):
    d_id = models.AutoField(db_column='D_id', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    d_date = models.DateField(db_column='D_date')  # Field name made lowercase.
    emp = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    emp_id = models.AutoField(db_column='Emp_id', primary_key=True)  # Field name made lowercase.
    work = models.ForeignKey('Work', models.DO_NOTHING, db_column='Work_id', blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=30)  # Field name made lowercase.
    emp_dob = models.DateField(db_column='Emp_dob')  # Field name made lowercase.
    contact_number = models.IntegerField(db_column='Contact_number')  # Field name made lowercase.
    emp_salary = models.IntegerField(db_column='Emp_salary')  # Field name made lowercase.
    work_experience = models.CharField(db_column='Work_experience', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emp_joindate = models.DateField(db_column='Emp_joindate')  # Field name made lowercase.
    emp_leavedate = models.DateField(db_column='Emp_leavedate', blank=True, null=True)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emp_un = models.CharField(max_length=30, blank=True, null=True)
    emp_password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Feedback(models.Model):
    f_id = models.AutoField(db_column='F_id', primary_key=True)  # Field name made lowercase.
    f_date = models.DateField(db_column='F_date', blank=True, null=True)  # Field name made lowercase.
    feedback = models.CharField(db_column='Feedback', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Offer(models.Model):
    offer_id = models.AutoField(db_column='Offer_id', primary_key=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_date')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    #product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    p_discount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'



class Order1(models.Model):
    order_id = models.AutoField(db_column='Order_id', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_id', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateField(db_column='Order_date',auto_now=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    order_quantity = models.IntegerField(db_column='Order_quantity')  # Field name made lowercase.
    payment = models.CharField(max_length=10)
    o_state = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order1'

class Product(models.Model):
    product_id = models.AutoField(db_column='Product_id', primary_key=True)  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='Category_id', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=30)  # Field name made lowercase.
    material = models.CharField(max_length=20)
    image = models.ImageField(upload_to="productimg/",default=" ")
    product_price = models.IntegerField(db_column='Product_price')  # Field name made lowercase.
    product_weight = models.CharField(db_column='Product_weight', max_length=10)  # Field name made lowercase.
    product_quantity = models.CharField(db_column='Product_quantity', max_length=10)  # Field name made lowercase.
    product_color = models.CharField(db_column='Product_color', max_length=10)  # Field name made lowercase.
    offer = models.ForeignKey(Offer, models.DO_NOTHING, db_column='Offer_id', blank=True, null=True)  # Field name made lowercase.

    dc_price = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'product'


class Production(models.Model):
    production_id = models.AutoField(db_column='Production_id', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    production_cost = models.FloatField(db_column='Production_cost')  # Field name made lowercase.
    production_date = models.DateField(db_column='Production_date')  # Field name made lowercase.
    polymer = models.CharField(db_column='Polymer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_quantity = models.CharField(db_column='P_quantity', max_length=10, blank=True, null=True)  # Field name made lowercase.
    other_material = models.CharField(db_column='Other_material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_quantity = models.CharField(db_column='M_quantity', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'production'


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    sup = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    material = models.CharField(max_length=30)
    quantity = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True,auto_now=True, null=True)  # Field name made lowercase.

    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase'


class RawMaterial(models.Model):
    raw_id = models.AutoField(db_column='Raw_id', primary_key=True)  # Field name made lowercase.
    sup = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Sup_id', blank=True, null=True)  # Field name made lowercase.
    raw_name = models.CharField(db_column='Raw_name', max_length=20)  # Field name made lowercase.
    raw_quantity = models.CharField(db_column='Raw_quantity', max_length=20)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'raw_material'


class Recycling(models.Model):
    r_id = models.AutoField(db_column='R_id', primary_key=True)  # Field name made lowercase.
    r_date = models.DateField(db_column='R_date')  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recycling'


class Sales(models.Model):
    sales_id = models.AutoField(db_column='Sales_id', primary_key=True)  # Field name made lowercase.
    sales_date = models.DateField(db_column='Sales_date')  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales'

class Stock(models.Model):
    stock_id = models.AutoField(db_column='Stock_id', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_id', blank=True, null=True)  # Field name made lowercase.
    r_id = models.IntegerField(db_column='R_id', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    material_quantity = models.CharField(db_column='Material_Quantity', max_length=10)  # Field name made lowercase.
    s_date = models.DateField(blank=True, null=True,auto_now=True)
    class Meta:
        managed = False
        db_table = 'stock'


class Supplier(models.Model):
    sup_id = models.AutoField(db_column='Sup_id', primary_key=True)  # Field name made lowercase.
    sup_name = models.CharField(db_column='Sup_name', max_length=30)  # Field name made lowercase.
    contact_number = models.IntegerField(db_column='Contact_number')  # Field name made lowercase.
    sup_address = models.CharField(db_column='Sup_address', max_length=100)  # Field name made lowercase.
    sup_email = models.CharField(db_column='Sup_email', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class Work(models.Model):
    work_id = models.AutoField(db_column='Work_id', primary_key=True)  # Field name made lowercase.
    work_name = models.CharField(db_column='Work_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'work'

class Cart(models.Model):
    c_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    cus_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=1)
    u_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'
        
