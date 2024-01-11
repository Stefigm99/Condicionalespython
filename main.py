#perro negro
#datos de entrada (variables)
nombreCliente=input("Cual es su nombre? ")
paisCliente=input("Cual es su pais de origen? ")
cantidadPersonas=int(input("cuantas personas van a reservar? "))
añoNacimientoCliente=int(input("En que año nació? "))


#calcular la edad del cliente operando aritmeticamente + - * / %
añoActual=2024
edadCliente=añoActual-añoNacimientoCliente

#clasificar, preguntar, decidir
if edadCliente >= 18:
    print("Usted es mayor de edad :D")
else:
    print("Usted es menor de edad D:<")

