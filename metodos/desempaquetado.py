#DESEMPAQUETADO DE VARIABLES
# creamos una lista
datos=["roony", "roldan",18]

#desempaquetando los elementos, guardandolos en variableseee
nombre,apellido,edad= datos
#imprimiendo en pantalla las variables
print(nombre+" "+apellido+" "+str(edad))

#desempaquetasdo una tupla
datos_tupla=tuple(datos)
nombre,apellido,edad=datos_tupla
print(nombre+apellido+str(edad))

#desempaquetando conjunto

datos_conjunto=set(datos)
nombre,apellido,edad=datos_conjunto
print(f"{nombre} {apellido} {edad}")

#desempaquetando un diccionario





#
numeros=[1,3,4,2,5,6]

for i,numero in enumerate(numeros):
    print(f"Indice{i}, Contenido: {numero}")