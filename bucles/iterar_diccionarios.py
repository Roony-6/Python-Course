
#creando un diccionario
diccionario={
    'nombre': "Roony",
    'apellido':"Roldan",
    'edad':18
}

#se obtienen las claves del diccionario 
for key in diccionario:
    print(key)

#ITEMS (s)
for contenido in diccionario.items():
    clave= contenido[0]
    valor=contenido[1]
    print(f"La clave es: {clave}, El valor es: {valor}")

#Es lo mismo que lo anterior pero desempaquetando directamente la lista
for i,elemento in diccionario.items():
    print(f"La clave es: {i}, El valor es: {elemento}")
    
    

#otro ejemplo más

frutas= ["manzana","granada","mango","platano","sandia"]

for fruta in frutas:
    if fruta=="manzana": #si 'fruta' es igual aa 'manzana' continua con lo demás 
        continue
    print(f"Comer {fruta}")
    
for fruta in frutas:
    if fruta=="platano": #si 'fruta' es igual aa 'manzana' continua con lo demás 
        print("ya comiste demasiadas frutas, para")
        break#fianliza el bucle 
    print(f"Comer {fruta}")
