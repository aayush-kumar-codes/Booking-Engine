# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import models
from . import serializers
from django.db.models import Q



'''API View for find all avaliable rooms'''
class AvailableRoomsView(APIView):
    def get(self,request):
        '''
        get keywords for filter 
        '''
        data = request.query_params
        max_price=data.get("max_price")
        check_in=data.get("check_in")
        check_out=data.get("check_out")
        
        '''
        count block days
        '''
        room_object=models.MakeReservations.objects.filter(
                        Q(check_in__gte=check_in,check_out__lte=check_out)|
                        Q(check_in__lte=check_in,check_out__gte=check_in)|
                        Q(check_in__lte=check_out,check_out__gte=check_out)
                        ).values_list('booking',flat=True)
        '''
        Find all avaliable hotel/Apartment
        '''
        hotel_object=models.BookingInfo.objects.all().filter(~Q(pk__in=room_object)).filter(
           price__lte=max_price).order_by('price')
        serializer=serializers.AvailableRoomsSerializers(hotel_object,many=True).data
        '''
        if no hotel/Apartment avaliable
        '''
        if len(serializer)==0:
            return Response("ROOM NOT FOUND",status=status.HTTP_200_OK)
        return Response({"List":serializer},status=status.HTTP_200_OK)
                        
   
