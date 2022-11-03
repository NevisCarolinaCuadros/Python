t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
print (t)
print (len(t))
#establecer variable t y la longitud de la variable que si es 5

print ('=====================================')
print (t[0])#imprimir casilla 0
print (t[3])#imprimir casilla 3
print (t[1:3])#imprimir el indice 1 al 3 para t
print (t[3][1])#imprimir 1
#

print ('====================================')
print (t[3])#imprimir casilla 3
t[3].append('lorito')#poner variable al final
print (t)#imprimir toda la variable

print ('====================================')
for elemento in t:
    print (elemento)
    #imprimir variable sobre cada una

print ('====================================')
for index in range(0,len(t)):
    print (t[index])
    #imprimir sobre casilla de 0 a la longitud completa de la casilla t
print ('====================================')
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")
    #arreglo imprimir ("El elemento 'a' esta en la tupla")

print ('====================================')
lista=list(t)
lista[1]='A'
print (lista)
#agregar a la lista 1 "A"
tupla=tuple(lista)
print (tupla)
#imprimir variable tupla

print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for x, y in l:
    print (x, ':', y)
    #imprimir un arreglo sobre cada una de las variables 