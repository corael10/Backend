import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.producto.models import *
from apps.producto.serializers import *
from django.db.models import Max, Min, Avg

# Create your views here.
class GetMarca(APIView):

    def get(self, request, format=None):
       # lista = Marca.objects.values('marca').annotate(Min('id'), Max('id'), Avg('id'))
        lista =  Marca.objects.all()
        serializer = ProductoSerializerMarca(lista, many=True)
        return Response(serializer.data)  

    def post(self, request, format=None):
        print(request.data)
        serializer = ProductoSerializerMarcaPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class getProv_Select(APIView):
  
    def get(self, request, pk, format=None):
        marcas = Marca.objects.all().filter(proveedor=pk)
        serializer = ProductoSerializerMarca(marcas, many=True)
        return Response(serializer.data)


class GetMarca_detalle(APIView):
  
    def get_object(self, pk):
        try:
            return Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        marca = Marca.objects.all().filter(marca=pk)
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        print(request.data)
        marca = self.get_object(pk)
        print('marcaaaa ',marca)
        #request.data['proveedor']=request.data['proveedor']['id']
        serializer = ProductoSerializerMarcaPost(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        marca = self.get_object(pk)
        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetProductoList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Producto.objects.all()
        serializer = ProductoSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print(request.data)
        serializer = ProductoSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        
        producto_data = {
                    "id":request.data['id'],
                    "codigo":request.data['codigo'].upper(),
                    "nombre":request.data['nombre'],
                    "marca":request.data['marca'],  
                    "familia":request.data['familia'],                    
                    "unidades":request.data['unidades'],
                    "precio_1":request.data['precio_1'],
                    "precio_2":request.data['precio_2'],
                    "precio_3":request.data['precio_3'],
                    "descripcion":request.data['descripcion'],
                    "precio_proveedor":request.data['precio_proveedor']
                    
                }
        print('producto data: ',producto_data)

        serializer = ProductoSerializerPost(producto, data=producto_data)
        if serializer.is_valid():
            serializer.save()
            print('guardo ',serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdatePromo(APIView):
  
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = Producto.objects.all().filter(marca=pk)
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        print('promo ',request.data)
        if request.data['quitar'] == False:
            producto = Producto.objects.get(id=pk)        
            producto.precio_promo = request.data['precio']
            producto.save()
            familia = Familia.objects.get(id=producto.familia_id)
            familia.promoactiva= True
            familia.save()
            producto.precio_promo = request.data['precio']
            producto.save()
            producto = self.get_object(pk)
            serializer = ProductoSerializer(producto)
            return Response(serializer.data)

        else:
            print('quitar promo')
            queryset = Producto.objects.filter(familia_id = pk).update(precio_promo=0)
            familia = Familia.objects.filter(id=pk).update(promoactiva=False)
            #queryset.save()  

            return Response('serializer')  
        


        

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetFamilia_Promocion(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Familia.objects.all().filter(promoactiva = 1)
        print(lista)
        serializer = ProductoSerializerFamilia(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print(request.data)
        serializer = ProductoSerializerFamilia(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class getMarc_Select(APIView):
  
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = Producto.objects.all().filter(familia=pk)
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializerPost(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class getFamilia_Select(APIView):
  
    def get_object(self, pk):
        try:
            return Familia.objects.get(pk=pk)
        except Familia.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        familia = Familia.objects.all().filter(marca=pk)
        serializer = ProductoSerializerFamilia(familia, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializerPost(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetFamilia(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Familia.objects.all()
        serializer = ProductoSerializerFamilia(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print(request.data)
        serializer = ProductoSerializerFamilia(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    