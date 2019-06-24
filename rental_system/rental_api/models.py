from django.db import models as M
# from django.contrib.auth.models import AbstractUser

# Create your models here.


class Customer(M.Model):
    name = M.CharField(max_length=30)
    email = M.EmailField()
    phone_number = M.CharField(max_length=15)
    password = M.CharField(max_length=20)
    re_enter = M.CharField(max_length=30)
   
   
    def __str__(self):
        return self.phone_number


class Document(M.Model):
    
    image = M.ImageField(upload_to='images/')
    front_citizenship = M.ImageField(upload_to='frontcitizenship/')
    back_citizenship = M.ImageField(upload_to='backcitizenship/')
    front_licence = M.ImageField(upload_to='frontlicence/')
    
    back_licence = M.ImageField(upload_to='backlicence/')
    customer = M.ForeignKey(Customer ,on_delete = M.CASCADE)

    def __str__(self):
        return self.customer.email


class VehicleCategory(M.Model):
    name = M.CharField(max_length=30)
    image = M.ImageField(upload_to='vehic_cat/', null=True, blank=True)




    def __str__(self):
        return self.name


class Vehicle(M.Model):
    VehicleCategory = M.ForeignKey(
        VehicleCategory, related_name='vehicle', on_delete=M.CASCADE)
    name = M.CharField(max_length=30)
    model = M.CharField(max_length=30)
    number_plate = M.CharField(max_length=30)
   
    def __str__(self):
        return self.model


class City(M.Model):
    name = M.CharField(max_length=30)
    city_image = M.ImageField(upload_to='city/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Vehicle_Type(M.Model):
    vehicle_status = (('A', 'AVAILABLE'), ('U', 'UNABAILABLE'))
    vehicle = M.ForeignKey(Vehicle, related_name='fules', on_delete=M.CASCADE)
    consumption= M.CharField(max_length=40)
    address = M.ForeignKey(City, on_delete=M.CASCADE, default=0)
    status = M.CharField(max_length=2, choices=vehicle_status, default='A')
    perHrPrice = M.IntegerField()
    image = M.ImageField(upload_to='vehicle/')
    
    def __str__(self):
        return self.vehicle.name


class City_Place(M.Model):

    city = M.ForeignKey(City, related_name='cities', on_delete=M.CASCADE)
    place = M.CharField(max_length=30)
    
    def __str__(self):
        return self.place


# class Customer(AbstractUser):
#     name = M.CharField(max_length=30)
#     address = M.CharField(max_length=30)
#     phone_number = M.CharField(max_length=15)
#     # email = M.EmailField()
#     image = M.ImageField(upload_to='images/')
#     citizenship = M.ImageField(upload_to='citizenship/')
#     licence = M.ImageField(upload_to='licence/')

#     def __str__(self):
#         return self.email



class Customer_Selection(M.Model):  
    customer_id = M.ForeignKey(Customer,related_name='customers', on_delete=M.CASCADE)
    vehicle_category_id = M.ForeignKey(Customer,related_name='vehical_category', on_delete=M.CASCADE)
    vehicle_id = M.ForeignKey(Customer,related_name='vehicles', on_delete=M.CASCADE)
    city_id = M.ForeignKey(Customer,related_name='_cities', on_delete=M.CASCADE)
    vehicle_type_id = M.ForeignKey(Customer,related_name='_vehicle_types', on_delete=M.CASCADE)
    city_place_id = M.ForeignKey(Customer, related_name='_city_place',on_delete=M.CASCADE)
    pick_up_location = M.CharField(max_length = 40)
    drop_up_location = M.CharField(max_length = 40)
    pick_up_date_and_time = M.DateField()
    drop_of_date_and_time = M.DateField()
