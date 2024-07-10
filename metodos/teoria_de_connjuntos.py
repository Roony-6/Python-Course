
conjunto=set(["dato1", "dato2","dato4","datos6"])

#FROZENSET convierte un conjunto en un conjunto congelado, permite meter un conjunto dentro de otro
conjunto2=("datos3","dato5",frozenset(conjunto))
print(conjunto2)



# Teoria de conjuntos

#creamos dos conjuntos
conjunto1={1,3,5,7,9}
conjunto2={1,3,5}

#verificamos si conjunto2 es un subconjunto de conjunto1
resultado=conjunto2.issubset(conjunto1) #True
print(resultado)

#verificamos si conjunto1 es un superconjunto del conjunto2
resultado=conjunto1.issuperset(conjunto2) #True
print(resultado)

conjunto3={2,4,6,8}
#verificamos si conjunto3 es disconjunto de conjunbto1 (si tiene al menos un elementop igual retorna falso)
resultado=conjunto3.isdisjoint(conjunto1) # True, nungun valor en común 
print(resultado)