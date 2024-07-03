# metodos string

nombre="Roony Roldan Cruz"

#UPPER convierte a mayuscula el texto
print(nombre.upper()) 

#LOWER convierte el texto a minusculas
print(nombre.lower()) 

#CAPITALIZE convierte la primera letra en mayuscula
print(nombre.capitalize()) 

#FIND busca una cadena dentro de otra cadena (retorna la posicion del caracter y si no lo encuentra retorna -1)
print(nombre.find("z"))

#INDEX busca una cadena dentro de otra (retorna el indice)
print(nombre.index("z"))

#ISNUMERIC si es numerico devuelve True
print(nombre.isnumeric())

#ISALPHA si es alfanumerico devuelve True
print(nombre.isalpha())

#COUNT busca una cadena en otra cadena y retorna el numero de coincidencia
print(nombre.count("Roony"))
print(nombre.count("o"))

#LEN cuenta los caracteres de una cadena
print(len(nombre))

#STARSWITH verifica si una cadena empieza con una cadena dada, retorna un valor booleano
print(nombre.startswith("R"))

#ENDSWITH verifica si una cadena acaba con una cadena dada, retornan valor booleano
print(nombre.endswith("z"))

#REPLACE remplaza una cadena dada por una otra dada
print(nombre.replace("Cruz", "Cruzzz"))#recibe dos parametros, la cadena a modificar y la cadena modificada

#SPLIT separa la cadena en caracteres por la cadena que le pases, retorna una lista
print(nombre.split(" "))
