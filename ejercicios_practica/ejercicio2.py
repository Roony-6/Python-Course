#Ejercicio 2.
#Pedir el nombre y edad de n numero de alumnos y ordenar los datos de mayor a menor
#El mayor de la clase será el profesor y el menor el asistente, ¿Quién es quién?

def obtener_compañero(numero_compañeros):
    alumnos=[]
    for i in range(numero_compañeros):
        nombre=input("Cuál es tu nombre?")
        edad=input("Cuál es tu edad")
        alumnos.append((nombre,edad))
    alumnos.sort(key=lambda x: x[1],reverse=True)
    maestro=alumnos[0][0]
    asistente= alumnos[-1][0]
    return maestro,asistente

n_alumnos=int(input("Cuántos alumnos son?"))
maestro,asistente=obtener_compañero(n_alumnos) 
print(f"El maestro es: {maestro} y el asistente es: {asistente}")

#otra solucion: 
print("--------------------------------------------------------------------")
def obtener_compañero(numero_compañeros):
    alumnos=[]
    for i in range(numero_compañeros):
        nombre=input("Cuál es tu nombre?")
        edad=input("Cuál es tu edad")
        alumnos.append((nombre,edad))
    alumnos_ordenados=sorted(alumnos,key=lambda x:x[1],reverse=True)
    maestro=alumnos_ordenados[0][0]
    asistente= alumnos[-1][0]
    return maestro,asistente

n_alumnos=int(input("Cuántos alumnos son?"))
maestro,asistente=obtener_compañero(n_alumnos) 
print(f"El maestro es: {maestro} y el asistente es: {asistente}")
    
    
        