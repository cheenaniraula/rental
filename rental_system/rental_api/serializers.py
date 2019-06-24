from rest_framework import serializers
from .models import VehicleCategory, Vehicle, Vehicle_Type, City, City_Place, Customer, Customer_Selection,Document


class VehicleCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = '__all__'


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class Vehicle_TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Type
        fields = '__all__'


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class City_PlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = City_Place
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class CustomerSelectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer_Selection
        fields = '__all__'

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'
     

#     def to_representation(self, value):
#         temp = super().to_representation(value)
#         v_id = temp['vehicle_id']
#         c_id = temp['city_id']
#         v = Vehicle.objects.get(id=v_id)
#         c = City_Place.objects.get(id=c_id)
#         cc = City.objects.get(name=c.city)
#         # temp['vehicle_name'] = v.name
#         temp['vehicle_model'] = v.model
#         temp['city_place'] = c.place
#         temp['city_name'] = cc.name
#         return temp
