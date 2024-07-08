# METODOS DE DICCIONARIOS

diccionario= {
    'nombre':"Roony",
    'apellido':"Roldan",
    'edad':18,
    'estatura':1.78
}

#KEYS
print(diccionario.keys())

# (getter) obtenemos el valor de la clave que le pasemos, tambien se puede iterar con las keys
print(diccionario.get("nombre"))

#CLEAR vacia el diccionario
#diccionario.clear()

#POP elimina los elementos pasandole la clave como parametro
diccionario.pop("edad","estatura")
print(diccionario)

#ITEMS
