from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.set.models import *
from apps.set.serializers import *

from django.db.models import ProtectedError
from django.db.models import Q


# Create your views here.


class GetChipsetList(APIView): 
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Chipset.objects.all()
        serializer = ChipsetSerializer(lista, many=True)
        #print('serielizer 0 ',serializer.data[0]['statuspreotn']['date_i'])
        #registros=len(serializer.data)
        for indice in range(len(serializer.data)):
            idstatus=serializer.data[indice]['statuspreotn']['id']
            getdays=StatusPreotn.objects.raw=('SELECT DATEDIFF(now(),(select date_i from ono.set_statuspreotn where id =%s)) as days',[idstatus])
            day=getdays[0]
            print('days ',day)
        #chipset_data={}
        return Response(serializer.data) 


    def post(self, request, format=None):
        serializer = ChipsetSerializerPost(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChipsetDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Chipset.objects.get(pk=pk)
        except Chipset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chipset = self.get_object(pk)
        serializer = ChipsetSerializer(chipset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chipset = self.get_object(pk)
        serializer = ChipsetSerializerPost(chipset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chipset = self.get_object(pk)
        try:
            chipset.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)   


class GetHistList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = HistVersion.objects.all()
        serializer = HistSerializer(lista, many=True)
        return Response(serializer.data) 


    def post(self, request, format=None):

        serializer2 = HistSerializerPost(data=request.data)
       
       # print(chipset)
        if serializer2.is_valid():
            serializer2.save()
            chipset = request.data['chipset']           

            max_id = Firmware.objects.raw('select A.id, A.firmware, A.firmware_number  '
            'from ono.set_firmware A,ono.set_histversion B '
            'where  B.chipset_id=%s  and B.firmware_set_id = A.id and '
            'A.firmware_number =  (select max(A.firmware_number) AS firmware_number '
            'from ono.set_firmware A,ono.set_histversion B '
            'where  B.chipset_id=%s  and B.firmware_set_id = A.id '
            'and B.firmware_set_id = A.id  )',[chipset,chipset])
            serializer3  = FirmwareSerializer(max_id,many=True)           
            dato=serializer3.data[0] 
            idhist= serializer2.data['id']
            lista = HistVersion.objects.all().filter(id=idhist)
            serializer = HistSerializer(lista, many=True)            
            Chipset.objects.filter(id=chipset).update(firmware_set=dato['id'])  #actualiza tabla chipset con ultima version        
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VersionHistorico(APIView): 
  
    def get_object(self, pk):
        try:
            return HistVersion.objects.get(pk=pk)
        except HistVersion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        historico = HistVersion.objects.all().filter(chipset=pk)
        serializer = HistSerializer(historico, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        firmware=request.data['firmware_set']
        chipset= request.data['chipset']       

        request.data['firmware_set'] = firmware['id']
        request.data['chipset'] = chipset['id']
        print(request.data)
        historico = self.get_object(pk)               
        serializer = HistSerializerPost(historico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        historico = self.get_object(pk)
        try:
            historico.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)         


class GetFirmwareList(APIView): 
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Firmware.objects.all()
        serializer = FirmwareSerializer(lista, many=True)
        return Response(serializer.data) 


    def post(self, request, format=None):

        serializer = FirmwareSerializer(data=request.data)  
        firmware=request.data['firmware'] 
        firmware_number=request.data['firmware_number']       
        if serializer.is_valid():
            a = Firmware.objects.filter(firmware=firmware, firmware_number=firmware_number)
            if a:
                 return Response('Already existing this firmware', status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                serializer.save()
       
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetFirmwareDetalle(APIView):
  
    def get_object(self, pk):
        #print(pk)
        try:
            return Firmware.objects.get(pk=pk)
        except Firmware.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        firmware = self.get_object(pk)
        serializer = FirmwareSerializer(firmware)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        firmware = self.get_object(pk)
        serializer = FirmwareSerializer(firmware, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        firmware = self.get_object(pk)
        try:
            firmware.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)    


class SetTimePREOTN(APIView): 
      
    def get_object(self, pk):       
        try:
            return Chipset.objects.get(pk=pk)
        except Chipset.DoesNotExist:
            raise Http404

    def get_object2(self, pk):
        try:
            return StatusPreotn.objects.get(pk=pk)
        except StatusPreotn.DoesNotExist:
            raise Http404        

    def get(self, request, pk, format=None):
        firmware = self.get_object(pk)
        serializer = FirmwareSerializer(firmware)
        return Response(serializer.data)

    def put(self, request, pk, format=None):         
        chipset = self.get_object(pk) 
        
        try:
            statuspreotn_id= request.data['chipset']['statuspreotn']['id']
        except:
            statuspreotn_id = 0
        #status = StatusPreotn.objects.get()
        status = StatusPreotn.objects.filter(Q(status = 1)  | Q(status = 2)  | Q(status = 3) ,id=statuspreotn_id)        
        serializer4  = StatusPreotnSerializer(status,many=True)
        try:
            date_i=serializer4.data[0]['date_i']
            userid=serializer4.data[0]['user']
        except:
            date_i = date.today()           
        status_data={}
        
        if status:
            userRequest=request.data['iduser']
            if (userid == userRequest):
               
                status_data['id']= statuspreotn_id
                status_data['date_i']= date_i
                status_data['date_f']= date.today()
                status_data['status']='0'
                status_data['user']=request.data['iduser']
                 
                statusPreotn = self.get_object2(statuspreotn_id) 
                serializer3 = StatusPreotnSerializer(statusPreotn, data=status_data)
                if serializer3.is_valid():
                    serializer3.save()
                    print('statusPPPREOTN ',statusPreotn)  
                    message='PRE-OTN Completed'

            else :
                message='impossible! to finish test, because another user initiated it'
            return Response(message)       

        else:
            status_data['id']=''
            status_data['date_i']= date.today()
            status_data['date_f']= date.today()
            status_data['status']='1'
            status_data['user']=request.data['iduser']
            serializer = StatusPreotnSerializer(data=status_data)
            if serializer.is_valid():
                serializer.save()
                #print('serielizer ',serializer.data)
                request.data['chipset']['statuspreotn']=serializer.data['id']             

                request.data['chipset']['firmware_set']=1
                #print('request dataaa ',request.data)
                serializer2 = ChipsetSerializerPost(chipset,data=request.data['chipset'])
                if serializer2.is_valid():
                    serializer2.save()
                    message='PRE-OTN started'
                    return Response(message)

        return Response('serializer.errors', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        firmware = self.get_object(pk)
        try:
            firmware.delete()        
        except ProtectedError:
            error_message = "This object can't be deleted!!"
            return Response(error_message,status=status.HTTP_424_FAILED_DEPENDENCY)   
        return Response(status=status.HTTP_204_NO_CONTENT)    