#METODOS DE LISTAS

lista= ["Roony","Roldan","Cruz",18]

#LEN retorna la cantidad de elementos que hay en la lista
print(len(lista))

#APPENED agrega elementos a la lista
lista.append(1.78)
print(lista)

#INSERT agrega un elemento a la lista a un indice especifico
lista.insert(4,"hola")
print(lista)

#EXTEND agrega varios elementos a la lista
lista.extend(["elementos", "nuevos"])
print(lista)

#POP eliminamos un elemento de la lista por su indice
lista.pop(5)
print(lista)

#REMOVE remueve un elemento dependiendo el valor que le pasemos
lista.remove("elementos")

#SORT ordena los elementos de menor a mayor
lista2= [6,5,48,875,47,51,13,1,254,133,66]
lista2.sort()
print(lista2)

lista2.sort(reverse=True) #este parametro las ordena de mayor a menor
print(lista2)

#REVERSE invierte los elementos de la lista
lista.reverse()
print(lista)

