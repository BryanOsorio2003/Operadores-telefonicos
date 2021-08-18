Tigo= (100)
claro=(150)
Movistar=(200)
promocion=(20000)


opcion=int(input("Ingrese 1 si quiere hacer paquete de minutos; ingrese 2 si quiere paquete de datos: "))
if opcion==1:
    print("Tigo operador 1")
    print("claro operador 2")
    print("movistar operador 3")
    operador=int(input("Que operador va recargar :  "))
    cantidad=int(input("De cuanto es la recarga : "))
    numero=int(input("Ingrese su numero telefonico: "))
    if operador == 1 :
        resultado = cantidad / Tigo 
        print("Usted ha obtenido ", resultado , " Minutos")
        if cantidad >= promocion :
            resultado1= (cantidad/Tigo)*2
            print ("Por su compra mayor a 20.000 te hemos multiplicado tu valor, ahora tendrá" , resultado1, " minutos.")
    if operador== 2:
        resultado = cantidad / claro 
        print(resultado , "Minutos")
        if cantidad >= promocion :
            resultado1= (cantidad/claro)*2
            print ("Por su compra mayor a 20.000 te hemos multiplicado tu valor, ahora tendrá" , resultado1, " minutos.")
    if operador== 3:
        resultado = cantidad / Movistar
        print(resultado , "Minutos")
        if cantidad >= promocion :
            resultado1= (cantidad/Movistar)*2
            print ("Por su compra mayor a 20.000 te hemos multiplicado tu valor, ahora tendrá" , resultado1, " minutos.")

if opcion ==2:
    print("Tigo operador opcion 1")
    print("claro operador opcion 2")
    print("movistar operador opcion 3")
    operador=int(input("Que operador va a recargar?:  "))
    print("Los costos son: ")
    print("Diario: 3.000$ opcion 1")
    print("Mensual: 20.000$ opcion 2")
    costo=int(input("Que paquete desea obtener?: "))
    numero=int(input("Ingrese su numero telefonico: "))
    if operador==1:
        if costo==1:
            print("Usted ha elegido el paquete diario con un costo de 3.000$")
            print("La recarga del paquete diario al numero " + str(numero) + " ha sido exitosa.")
        if costo==2:
            print("Usted ha elegido el paquete mensual con un costo de 20.000$")
            print("La recarga del paquete mensual al numero " + str(numero) + " ha sido exitosa.")
    if operador==2:
        if costo == 1:
            print("Usted ha elegido el paquete diario con un costo de 3.000$")
            print("La recarga del paquete diario al numero " + str(numero) + " ha sido exitosa.")
        if costo==2:
            print("Usted ha elegido el paquete mensual con un costo de 20.000$")
            print("La recarga del paquete mensual al numero " + str(numero) + " ha sido exitosa.")
    if operador==3:
        print("El operador Movistar no tiene paquete de datos.")
