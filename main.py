#perro negro

nombreCliente=input("¿Cual es su nombre?")
paisCliente=input("¿Cual es su pais de origen?")
cantidadDePersonas= int(input("Cual es la cantidad de personas a ingresar"))
añosNacimiento=int(input("¿En que año nació?"))

#Quiero calcular la edad del cliente


añoActual = 2024
edadCliente = (añoActual-añosNacimiento)

#Clasificar, preguntar, decidir


if edadCliente >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")    

