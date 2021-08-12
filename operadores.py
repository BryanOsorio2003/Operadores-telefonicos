Tigo= (100)
claro=(150)
Movistar=(200)
promocion=(20000)

print("Tigo operador 1")
print("claro operador 2")
print("movistar operador 3")
operador=int(input("Que operador va recargar :  "))
cantidad=int(input("De cuanto es la recarga : "))
if operador == 1 :
    
    resultado = cantidad / Tigo 
    print(resultado , "Minutos")

if cantidad >= promocion :
    resultado1= (cantidad/Tigo)*2
    print (resultado1 ,"te hemos multiplicado tu valor :")

if operador== 2:
    resultado = cantidad / claro 
    print(resultado , "Minutos")

if cantidad >= promocion :
    resultado1= (cantidad/claro)*2
    print (resultado1 ,"te hemos multiplicado tu valor :")

if operador== 3:
    resultado = cantidad / Movistar
    print(resultado , "Minutos")

if cantidad >= promocion :
    resultado1= (cantidad/Movistar)*2
    print (resultado1 ,"te hemos multiplicado tu valor :")
