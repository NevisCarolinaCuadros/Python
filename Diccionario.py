huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}
#nombramos la variable huespedes con un número por cada uno

print (huespedes)
#imprimimos la variable
print (huespedes.items())
#nombramos los elementos dentro de la variable

print (huespedes.keys())
#tomamos (keys) para identificar la variable
for key in huespedes:
    print (key)
    #identificar el arreglo por huespedes


print (huespedes.values())
#toma los números dados a cada variable
for key in huespedes:
    print (huespedes[key])
print()
#impriir la variable del arreglo

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion])
print()
#arreglo para imprimir el nombre del huesped y la habitación
for habitacion,huesped in huespedes.items():
    print (habitacion,':',huespedes[key])
#arreglo por variable numerica
for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key])
print()
#arreglo para enumerar cada una de las variables desde 1

print (huespedes[105])
print (huespedes.get(105))
#imprimir el huesped (value) que se encuentra en 105

print ('====================================')

huespedes[102]='Fanny Lu'
huespedes[107]='Don Omar'
huespedes.setdefault('109','Luis Miguel')
#items de huespedes y el value de ('109','Luis Miguel') se convierte en un key

for huesped in huespedes.items():
    print (habitacion,':',huesped)
print()
#imprimir el número de habitación y el huesped

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
#números de ingresos día
huespedes.update(registroshoy)
#actualización de datos
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped)
print()
#imprimir items(values + keys) de las habitaciones y keys

print ('====================================')

huespedes[107]='Ricky Martin'
print (huespedes)
#imprimir huesped 107

print ('====================================')


del huespedes[102]
huespedes.pop(202)
print(huespedes)
#eliminar los huesped 102 y 202
print ('====================================')

copia1=huespedes.copy()
print ('copia1: ',copia1)
copia2={}
copia2.update(huespedes)
print ("copia2: ",copia2)
#se crea una copia por registro de habitación y huesped
print ('====================================')

lista=[2,5,7,1]
diccio=dict.fromkeys(lista,"xxx")
print(diccio)
#el valor por key de la lista es "xxx"

print ('====================================')
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)
inventario["cartera"].sort()
print(inventario)
inventario["cartera"].remove("Moneda")
print(inventario)
print(inventario.get("plata")[0])
#Imprimir los una cartera en donde se encuentran ciertos elementos, mecato y dias, a su vez donde se elimina uno de los elementos de la cartera
