import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.producto.models import *
from apps.inventario.models import *
from apps.proveedor.models import *
from apps.inventario.serializers import *
from apps.producto.serializers import *
from django.db.models import Max, Min, Avg

# Create your views here.



class InventarioDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Inventario_entrada.objects.get(pk=pk)
        except Inventario_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('request ')
        inventario = Inventario_entrada.objects.all().filter(proveedor=pk).order_by('-id')
        serializer = InventarioSerializer(inventario, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        print(request.data)
        inventario = self.get_object(pk)
        try:
            request.data['proveedor']=request.data['proveedor']['id']
        except:
            request.data['proveedor']=request.data['proveedor']

        serializer = InventarioSerializerPost(inventario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        inventario = self.get_object(pk)
        folio = inventario.folio
        productos = Productos_inventario_entrada.objects.all().filter(folio=folio)
        serializer = Productos_inventario_entradaSerializer(productos, many=True)
        for i in range(len(serializer.data)):
            #print('unidades actual ', serializer.data[i]['unidades'])
            #print('id actual ', serializer.data[i]['producto']['id'])
            idproducto = Producto.objects.get(id=serializer.data[i]['producto']['id'])
           # print('unidades totales inventario ',idproducto.unidades)
            idproducto.unidades = idproducto.unidades - serializer.data[i]['unidades']
            idproducto.save()
            productos.delete()
        
        inventario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetInventarioList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Inventario_entrada.objects.all().order_by('-id')
        serializer = InventarioSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        #print(request.data)
        inventario_data = { #crea objeto para guardar en la tabla de inventario el encabezado del folio
                "folio":request.data['folio'],
                "fecha":request.data['fecha'],
                "fecha_proveedor":request.data['fecha_proveedor'],
                "proveedor":request.data['proveedor'],
                "total":request.data['total'],
            }       
        serializer = InventarioSerializerPost(data=inventario_data)
        if serializer.is_valid():
            serializer.save() #Guarda el objeto creando nuevo registro en la tabla 
            updateProveedor = Proveedor.objects.get(id= inventario_data['proveedor']) # Actualizamos el saldo en la tabla de proveedores
            updateProveedor.saldo = updateProveedor.saldo + inventario_data['total']
            updateProveedor.save() #Guardamos la actualizacion con el nuevo saldo
          
            array=request.data['productos'] #creamos un array para parsear todos los productos
            for i in range(len(array)):               
                producto_inventario_data = { # creamos objeto por cada producto para insertarlo en la tabla de producto_inventario
                    "producto_id":array[i]['id'],
                    "folio":request.data['folio'],                    
                    "unidades":array[i]['unidades'],
                    "precio_proveedor":array[i]['precio_proveedor'],
                    "inventario_entrada_id":serializer.data['id'],
                    "total":array[i]['total']
                }
                inventario = Productos_inventario_entrada.objects.create(**producto_inventario_data) # Creamos nuevo registro por cada producto
                idprod=array[i]['id'] #obtenemos el id de cada producto para afectarlo en la tabla de productos
                unidades=array[i]['unidades']
                producto = Producto.objects.get(id=idprod) #obtenemos el producto para actualizar el total de sus unidades existentes
                producto.unidades=  producto.unidades + unidades # sumamos las unidades existentes con las nuevas entrantes
                producto.precio_proveedor = array[i]['precio_proveedor']
                producto.save() # Guardamos el objeto 
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetInvSelect(APIView):
  
    def get_object(self, pk):
        try:
            return Productos_inventario_entrada.objects.get(pk=pk)
        except Productos_inventario_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        #print("pkkkkkkkk ",pk)
        inventario = Productos_inventario_entrada.objects.all().filter(inventario_entrada=pk)
        serializer = Productos_inventario_entradaSerializer(inventario, many=True)
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


  
class GetDetalleSelect(APIView):
  
    def get_object(self, pk):
        try:
            return Productos_inventario_entrada.objects.get(pk=pk)
        except Productos_inventario_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inventario = Productos_inventario_entrada.objects.all().filter(inventario_entrada=pk).order_by('-id')
        serializer = Productos_inventario_entradaSerializer(inventario, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        
        producto = self.get_object(pk)        
        idprod = request.data['producto']['id'] # Obtenemos el id del producto
        idproductos = Producto.objects.get(id=idprod) # obtenemos el objeto producto de la tabla productos
        idproductos.unidades = idproductos.unidades - producto.unidades # quitamos las unidades del objeto a actualizar de la tabla producto para despues ponerlas con el nuevo valos
        idproductos.save() #guardamos el producto      
        
        producto.precio_proveedor = request.data['precio_proveedor'] # le asignamos el nuevo valor al objeto a actualizar
        producto.unidades = request.data['unidades']
        producto.total = request.data['total']
        id_inventario= request.data['inventario_entrada']['id']
        producto.save() # Guardamos los nuevos valores

        total = 0
        prod_inventario = Productos_inventario_entrada.objects.all().filter(inventario_entrada=id_inventario) # Obtenemos el 
        serializer = Productos_inventario_entradaSerializer(prod_inventario, many=True)
        #print(serializer.data)
        for i in range(len(serializer.data)):
           total= total+ serializer.data[i]['total']    #obtenemos la suma de cada registro que haya con el mismo folio

        inventario = Inventario_entrada.objects.get(id=id_inventario)   #obtenemos el objeto en inventario para actualizar su total
        print('update proveedor ',inventario.proveedor_id)
        updateProveedor = Proveedor.objects.get(id= inventario.proveedor_id) # Obtenemos el objeto proveedor de la tabala proveedor
        print('update saldo ',updateProveedor.saldo)
        updateProveedor.saldo = updateProveedor.saldo - inventario.total # restamos el saldo anterior para despues poner el nuevo
        updateProveedor.save()
        #print('inventario ', inventario)
        inventario.total=total
        inventario.save() #actualizamos el objeto inventario
    
        idproductos.unidades =  int(producto.unidades) + int(idproductos.unidades) # Actualizamos las unidades en tabla productos
        idproductos.save()
        
        #updateProveedor = Proveedor.objects.get(id= inventario.proveedor) # Actualizamos el saldo en la tabla de proveedores
        updateProveedor.saldo = updateProveedor.saldo + inventario.total
        updateProveedor.save() #Guardamos la suma de la actualizacion en el folio

        serializer = Productos_inventario_entradaSerializer(producto)
        return Response(serializer.data)
       
        

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)

        idprod= producto.producto_id
        #print(producto.total)
        idproductos = Producto.objects.get(id=idprod)
        id_inventario=producto.inventario_entrada_id
        idproductos.unidades = idproductos.unidades - producto.unidades
        inventario = Inventario_entrada.objects.get(id=id_inventario)   
        inventario.total = inventario.total -producto.total
        updateProveedor = Proveedor.objects.get(id= inventario.proveedor_id) # Obtenemos el objeto proveedor de la tabala proveedor
        updateProveedor.saldo =  updateProveedor.saldo - producto.total
        updateProveedor.save()
        #print('total unidades ',idproductos.unidades)
        producto.delete()
        idproductos.save()
        inventario.save()


        return Response(status=status.HTTP_204_NO_CONTENT)      

class getMarc_Select(APIView):
  
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