# Datos compuestos

# Listas[] (Se pueden modificar y  acceder a sus elementos sin necesidad de un bucle)

lista= ["Roony", "Roldan", 18, 1.78, True]
print(lista)
lista[4]= False
print(lista[4])
print(lista)

#Tuplas() (No se pueden modificar sus elementos, se necesita un bucle para acceder a sus elementos)}

tupla= ("Roony", "Roldan",18,1.78,True)
print(tupla)
#no valido:
#tupla[1]= "Cruz"


# Conjuntos{} (No se pueden modificar sus elementos, no se puede acceder a ellos sin un bucle, no permite elementos repetidos)

conjunto= {"Roony", "Roldan",18,1.78,True,"Roony"}

print(conjunto)