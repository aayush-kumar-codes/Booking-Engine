from rest_framework import serializers
from . import models


class AvailableRoomsSerializers(serializers.ModelSerializer):
    listing_type= serializers.SerializerMethodField()
    title= serializers.SerializerMethodField()
    country= serializers.SerializerMethodField()
    city= serializers.SerializerMethodField()
    # price=serializers.SerializerMethodField()
   
    class Meta:
        model = models.BookingInfo
        fields =[
            "id",
            "listing_type",
            "title",
            "country",
            "city",
            "price"
            ]
    def get_listing_type(self,obj):
        try:
            return obj.listing.listing_type
        except:
            try:
                return obj.hotel_room_type.hotel.listing_type
            except:
                return '-'
    def get_title(self,obj):
        try:
            return obj.listing.title
        except: 
            try:
                return obj.hotel_room_type.hotel.title
            except:
                return "-"
    def get_country(self,obj):
        try:
            return obj.listing.country
        except:
            try:
                return obj.hotel_room_type.hotel.country
            except:
                return "-"
    def get_city(self,obj):
        try:
            return obj.listing.city
        except:
            try:
                return obj.hotel_room_type.hotel.city
            except:
                return "-"

       
        