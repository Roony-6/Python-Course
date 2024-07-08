#Suponiendo que una persona persona promedio habla 2 palabras por segundo

#a) pedirle al usuario que diga cualquier texto y:
# -calcular cuanto tiempo tardaria en decir esa frase y cuantas palabras fueron las que dijo

texto=input("Dame un texto: ")
numero_palabras=len(texto.split(" "))
tiempo=numero_palabras/2
print(f"El tiempo aproximado en decir '{texto}' es de: {tiempo} segundos")
print(f"El numero de palabras que dijo: {numero_palabras}")

# b) si se tarda más de 1 segundo decirle "aguanta, no te pedí la biblia"

if tiempo>1:
    print("aguanta!, tampoco te pedí la biblia")

#c) si otra persona habla un 30% más rapido
#- cuánto tiempo tardaría en decirlo?

print(f"La persona diría '{texto}' en {tiempo-(tiempo*0.3)}")
