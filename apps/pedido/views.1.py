import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from apps.producto.models import *
from apps.inventario.models import *
from apps.cliente.models import *
from apps.empleado.models import *
from apps.pedido.models import *

from apps.pedido.serializers import *
from apps.inventario.serializers import *
from apps.producto.serializers import *
from apps.cliente.serializers import *
from apps.empleado.serializers import *

from django.db.models import Max, Min, Avg

# Create your views here.



class PedidoDetalle(APIView):
  
    def get_object(self, pk):
        try:
            return Pedido_entrada.objects.get(pk=pk)
        except Pedido_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('request ')
        pedido = Pedido_entrada.objects.all().filter(cliente=pk).order_by('-id')
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        print(request.data)
        pedido = self.get_object(pk)
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
        pedido = self.get_object(pk)
        idpedido = pedido.id
        productos = Productos_pedido_entrada.objects.all().filter(pedido_entrada_id=idpedido)
        serializer = Productos_pedido_entradaSerializer(productos, many=True)
        for i in range(len(serializer.data)):           
            idproducto = Producto.objects.get(id=serializer.data[i]['producto']['id'])           
            idproducto.unidades = idproducto.unidades + serializer.data[i]['unidades']
            idproducto.save()
            
        updateCliente = Cliente.objects.get(id= pedido.cliente_id) # Obtenemos el objeto cliente de la tabala cliente
        print('update saldo ',updateCliente.saldo)
        updateCliente.saldo = updateCliente.saldo - pedido.total # restamos el saldo anterior para despues poner el nuevo
        updateCliente.save()
        updateEmpleado = Empleado.objects.get(id= pedido.empleado_id) # Obtenemos el objeto empleado de la tabala empleado
        print('update saldo ',updateEmpleado.saldo)
        updateEmpleado.saldo = updateEmpleado.saldo - pedido.total # restamos el saldo anterior para despues poner el nuevo
        updateEmpleado.save()

        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetpedidoList(APIView):
    #serializer = ClienteSerializer
   
    def get(self, request, format=None):
        lista = Pedido_entrada.objects.all().order_by('-id')
        serializer = PedidoSerializer(lista, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print(request.data)
        pedido_data = { #crea objeto para guardar en la tabla de pedidos el encabezado del pedido
                "cliente":request.data['cliente'],
                "fecha":request.data['fecha'],
                "empleado":request.data['empleado'],
                "total":request.data['total'],
            }       
        serializer = PedidoSerializerPost(data=pedido_data)
        if serializer.is_valid():
            serializer.save() #Guarda el objeto creando nuevo registro en la tabla 

            updateCliente = Cliente.objects.get(id= pedido_data['cliente']) # Actualizamos el saldo en la tabla de Cliente
            updateCliente.saldo = updateCliente.saldo + pedido_data['total']
            updateCliente.save() #Guardamos la actualizacion con el nuevo saldo

            updateEmpleado = Empleado.objects.get(id= pedido_data['empleado']) # Actualizamos el saldo en la tabla de Empleado
            updateEmpleado.saldo = updateEmpleado.saldo + pedido_data['total']
            updateEmpleado.save() #Guardamos la actualizacion con el nuevo saldo
          
            array=request.data['productos'] #creamos un array para parsear todos los productos
            for i in range(len(array)):               
                producto_pedido_data = { # creamos objeto por cada producto para insertarlo en la tabla de producto_pedido
                    "producto_id":array[i]['id'],                   
                    "unidades":array[i]['unidades'],
                    "precio":array[i]['precio'],
                    "pedido_entrada_id":serializer.data['id'],
                    "total":array[i]['total']
                }
                pedido = Productos_pedido_entrada.objects.create(**producto_pedido_data) # Creamos nuevo registro por cada producto
                idprod=array[i]['id'] #obtenemos el id de cada producto para afectarlo en la tabla de productos
                unidades=array[i]['unidades']
                producto = Producto.objects.get(id=idprod) #obtenemos el producto para actualizar el total de sus unidades existentes
                producto.unidades=  producto.unidades - unidades # restamos las unidades existentes con las del nuevo pedido
                producto.save() # Guardamos el objeto 

            
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPedSelect(APIView):
  
    def get_object(self, pk):
        try:
            return Productos_pedido_entrada.objects.get(pk=pk)
        except Productos_pedido_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        #print("pkkkkkkkk ",pk)
        pedido = Productos_pedido_entrada.objects.all().filter(pedido_entrada=pk)
        serializer = Productos_pedido_entradaSerializer(pedido, many=True)
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
            return Productos_pedido_entrada.objects.get(pk=pk)
        except Productos_pedido_entrada.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pedido = Productos_pedido_entrada.objects.all().filter(inventario_entrada=pk)
        serializer = Productos_pedido_entradaSerializer(pedido, many=True)
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        
        producto = self.get_object(pk)        
        idprod = request.data['producto']['id'] # Obtenemos el id del producto
        idproductos = Producto.objects.get(id=idprod) # obtenemos el objeto producto de la tabla productos
        idproductos.unidades = idproductos.unidades + producto.unidades # quitamos las unidades del objeto a actualizar de la tabla producto para despues ponerlas con el nuevo valos
        idproductos.save() #guardamos el producto      
        
        producto.precio = request.data['precio'] # le asignamos el nuevo valor al objeto a actualizar
        producto.unidades = request.data['unidades']
        producto.total = request.data['total']
        id_pedido= request.data['pedido_entrada']['id']
        producto.save() # Guardamos los nuevos valores

        total = 0
        prod_pedido = Productos_pedido_entrada.objects.all().filter(pedido_entrada=id_pedido) # Obtenemos el 
        serializer = Productos_pedido_entradaSerializer(prod_pedido, many=True)
        #print(serializer.data)
        for i in range(len(serializer.data)):
           total= total+ serializer.data[i]['total']    #obtenemos la suma de cada registro que haya con el mismo id de pedido

        pedido = Pedido_entrada.objects.get(id=id_pedido)   #obtenemos el objeto en inventario para actualizar su total
        print('update proveedor ',pedido.cliente_id)
        updateCliente = Cliente.objects.get(id= pedido.cliente_id) # Obtenemos el objeto cliente de la tabala cliente
        print('update saldo ',updateCliente.saldo)
        updateCliente.saldo = updateCliente.saldo - pedido.total # restamos el saldo anterior para despues poner el nuevo
        updateCliente.save()
        updateEmpleado = Empleado.objects.get(id= pedido.empleado_id) # Obtenemos el objeto empleado de la tabala empleado
        print('update saldo ',updateEmpleado.saldo)
        updateEmpleado.saldo = updateEmpleado.saldo - pedido.total # restamos el saldo anterior para despues poner el nuevo
        updateEmpleado.save()
       
        pedido.total=total
        pedido.save() #actualizamos el objeto pedido
    
        idproductos.unidades =  int(producto.unidades) - int(idproductos.unidades) # Actualizamos las unidades en tabla productos
        idproductos.save()
        
        #updateProveedor = Proveedor.objects.get(id= inventario.proveedor) # Actualizamos el saldo en la tabla de proveedores
        updateCliente.saldo = updateCliente.saldo + pedido.total
        updateCliente.save() #Guardamos la suma de la actualizacion en el folio del pedido
        updateEmpleado.saldo = updateEmpleado.saldo + pedido.total
        updateEmpleado.save() #Guardamos la suma de la actualizacion en el folio del pedido

        serializer = Productos_pedido_entradaSerializer(producto)
        return Response(serializer.data)
       
        

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)

        idprod= producto.producto_id
        #print(producto.total)
        idproductos = Producto.objects.get(id=idprod)
        id_pedido=producto.pedido_entrada_id
        idproductos.unidades = idproductos.unidades + producto.unidades
        pedido = Pedido_entrada.objects.get(id=id_pedido)   
        pedido.total = pedido.total - producto.total
        updateCliente = Cliente.objects.get(id= pedido.cliente_id) # Obtenemos el objeto cliente de la tabala cliente
        updateCliente.saldo =  updateCliente.saldo - producto.total
        updateCliente.save()

        updateEmpleado = Empleado.objects.get(id= pedido.empleado_id) # Obtenemos el objeto empleado de la tabala empleado
        updateEmpleado.saldo =  updateEmpleado.saldo - producto.total
        updateEmpleado.save()
        #print('total unidades ',idproductos.unidades)
        producto.delete()
        idproductos.save()
        pedido.save()


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