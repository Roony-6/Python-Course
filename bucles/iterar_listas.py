
animales=["perro","gato","iguana","loro"]
nombres=["pedrito","azul","juan","pepe"]

# BUCLE FOR IN

for animal in animales:#iteramos la lista animales guardando su contenido en la varible animal 
    print(f"El animal es: {animal}")

#ZIP (itera 2 o más listas)

for animal,nombre in zip(animales,nombres):
    print(f"Animal: {animal}, Nombre: {nombre}") 

#RANGE 

for numero in range(10):#itera desde el numero 0 al numero que le pasemos como parametro 
    print(f"el numero es: {numero}")

for numero in range(5,10):#itera en un rango de numero que le pasemos como parametro 
    print(f"el numero es: {numero}")



#FORMA OPTIMA DE ITERAR UNA LISTA OBTENIENDO SU INDICE
numeros=[1,3,4,2,5,6]

for i,numero in enumerate(numeros):
    print(f"Indice: {i}, Contenido: {numero}")

#FORMA NO OPTIMA usando RANGE

for numero in range(len(numeros)):
    print(numeros[numero])


    
    