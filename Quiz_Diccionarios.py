rios = {'Nilo': 'Egipto', 'Rio Misisipi': 'Estados Unidos', 'Ganges': 'India', 'Yellow River': 'China', 'Rio Obi': 'Russia'}

print ('============Punto 1========================')
for frase in rios:
    print ('El rio',frase,'corre a través de',rios[frase])
print()
print ('====================================')
for key in rios:
    print (key)
print ('====================================')
print (rios.values())
for key in rios:
    print (rios[key])
print()
for frase in rios:
    print (frase,':',rios[frase])
print()
print ('====================================')
print(rios)
print(rios.items())
print(rios.keys())
for key in rios:
    print(rios)

print ('============Punto 2========================')
frases = {'int', 'double', 'tuplas', 'metodos', 'arreglos'}
frase1 = {'int': '.'}
frase2 = {'double': '.'}
frase3 = {'tuplas': '.'}
frase4 = {'metodos': '.'}
frase5 = {'arreglos': '.'}

for fraseA in frase1:
    print (fraseA,'\n:Utilizado para nombrar diferentes números de tipo entero',frase1[fraseA])
print()
for fraseB in frase2:
    print (fraseB,'\n:Utilizado para nombrear diferentes números de tipo decimal',frase2[fraseB])
print()
for fraseC in frase3:
    print (fraseC,'\n:Un arreglo que organiza variables desordenandas',frase3[fraseC])
print()
for fraseD in frase4:
    print (fraseD,'\n:Utilizado para realizar tareas enfocadas principalmente a un objeto',frase4[fraseD])
print()
for fraseE in frase5:
    print (fraseE,'\n:Permite almacenar una serie de datos para un conjunto',frase5[fraseE])
print()
