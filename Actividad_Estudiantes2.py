#print('Ingrese 4 estudiantes: ')
estudiantes={1:'Juan Rojas', 2:'Oscar Lopez', 3: 'Laura Cardenas', 4: 'Maria Valencia'}

print('Ingrese 3 notas para los 4 estudiantes:')
calificaciones1= float(input()), float(input()), float(input())
calificaciones2= float(input()), float(input()), float(input())
calificaciones3= float(input()), float(input()), float(input())
calificaciones4= float(input()), float(input()), float(input())


if calificaciones1>calificaciones2:
    print(str(calificaciones1) +" es el mayor" + str(calificaciones2) +"es el menor")
elif calificaciones1>calificaciones3:
    print(str(calificaciones1) +" es el mayor" + str(calificaciones3) +"es el menor")
elif calificaciones1>calificaciones4:
    print(str(calificaciones1)  +" es el mayor" + str(calificaciones4) +"es el menor")
elif calificaciones2>calificaciones1:
    print(str(calificaciones2)  +" es el mayor" + str(calificaciones1) +"es el menor")
elif calificaciones2>calificaciones3:
    print(str(calificaciones2)  +" es el mayor" + str(calificaciones3) +"es el menor")
elif calificaciones2>calificaciones4:
    print(str(calificaciones2)  +" es el mayor" + str(calificaciones4) +"es el menor")
elif calificaciones3>calificaciones1:
    print(str(calificaciones3)  +" es el mayor" + str(calificaciones1) +"es el menor")
elif calificaciones3>calificaciones2:
    print(str(calificaciones3)  +" es el mayor" + str(calificaciones2) +"es el menor")
elif calificaciones3>calificaciones4:
    print(str(calificaciones3)  +" es el mayor" + str(calificaciones4) +"es el menor")
elif calificaciones4>calificaciones1:
    print(str(calificaciones4)  +" es el mayor" + str(calificaciones1) +"es el menor")
elif calificaciones4>calificaciones2:
    print(str(calificaciones4)  +" es el mayor" + str(calificaciones2) +"es el menor")
elif calificaciones4>calificaciones3:
    print(str(calificaciones4)  +" es el mayor" + str(calificaciones3) +"es el menor")
else:
    print(str(calificaciones1) + " , " + str(calificaciones2)+ " , " + str(calificaciones3) + " , " + str(calificaciones4)+ " son iguales")

print (estudiantes)
print (estudiantes.items())
print (estudiantes.keys())
for key in estudiantes:
    print (key)

print (estudiantes.values())
for key in estudiantes:
    print (estudiantes[key])
print()

for notas in estudiantes:
    print (notas,':',estudiantes[notas])
print()
for notas,estudiante in estudiantes.items():
    print (notas,':',estudiantes[key])
for indice, key in enumerate(estudiantes):
    print (indice+1,key,estudiantes[key])
print()

print (estudiantes[1])
print (estudiantes.get(1))
print ('====================================')
print (estudiantes[2])
print (estudiantes.get(2))
print ('====================================')
print (estudiantes[3])
print (estudiantes.get(3))
print ('====================================')
print (estudiantes[4])
print (estudiantes.get(4))
print ('====================================')

estudiantes[1]='Juan Rojas'
estudiantes[2]='Oscar Lopez'
estudiantes[3]='Laura Cardenas'
estudiantes[4]='Maria Valencia'

for estudiante in estudiantes.items():
    print (notas,':',estudiante)
print()

print ('====================================')

del estudiantes[1]
estudiantes.pop(4)
print(estudiantes)
print ('====================================')