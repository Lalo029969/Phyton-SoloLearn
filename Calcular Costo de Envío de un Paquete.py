"""
Imagina que necesitas calcular el costo de envío para los pedidos de los clientes basado en el peso de los paquetes. El costo por kilogramo es de $5.

"""

print("Ingrese el Peso del Paquete que deseas Enviar: ")

#tomar el peso como entrada
weight = int(input())

#completar la función
def shipping_cost(weight):
  costo = weight * 5
  return costo

#Imprimir Mensaje Detallado:

print("El Costo de Envío de tu Paquete es de:")


#llamar a la función

print (shipping_cost(weight))