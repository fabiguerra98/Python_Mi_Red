
#DECISIONES COMPLEJAS    IF/ELSE/ELIF

#llueve = True
#temperatura = int(input("Ingrese temperatura"))
#if temperatura < 18:
#    if llueve == True:
#       print("llevare paraguas y abrigo ")
#    else:
#          print("solo llevare abrigo")
#else:
#    print("no necesito paraguas ni abrigo")

#llueve = True
#temperatura = int(input("INGRESE TEMPERATURA"))
#if temperatura < 18 and llueve == True:
#    print("llevare paraguas y abrigo")
#elif temperatura < 18 and llueve == False:
#    print("Solo llevare abrigo")
#else:
#    print("No llevare paraguas ni abrigo")


#llueve = True
#temperatura = int(input("Ingrese temperatura"))
#if temperatura >=18:
#    print(" No llevare paraguas ni abrigo")
#elif llueve == True:
#    print("llevare paraguas y abrigo")
#else:
#    print("Solo llevare abrigo")

#for i in range (1,100):
#     if i<18:
#         print(i, "Eres menor de edad")
#     else:
#        print(i,"Eres mayor de edad")

#i = 1
#while i < 100:
#    if i<18:
#        print(i,"menor de edad")
#    else:
#        print(i,"mayor de edad")
#    i = i +1


#for i in range(1,101):
# for j in range(1,101):
#   print(i,j)



#numero = 4

#if numero % 2 == 0:
#   resultado = numero ** 3
#else:
#   resultado = numero ** 2

#print("El resultado es:", resultado)


#def es_primo(numero):
#  primo = True
#  if numero >1:
#        for i in range(2, numero):
#            if (numero % i) == 0:
#                primo = False
#  else:
#        primo = False
#  return primo

#Ciclo for

#total = 3
#unidad =  "dias"
#for i in range (total):
#    print("han psado", str(i), unidad)



#def calculo (numero):
#    resultado = (numero - 3) ** 3
#    return resultado

#def es_par(numero):
#    if numero % 2 == 0:
#        return True
#    else:
#        return False

#    print(es_par(8))
#    print(es_par(7))

#def funcion(x,y):
#return (x-8)*(y**2)
#funcion(16,1)



#def maximo_divisor(n):
#    maximo_actual = 0
#    i = 1
#    while i < n:
#        if n % i == 0:
#            maximo_actual = i
#        i +=1
#    return maximo_actual

#def cuenta(tope):
#  i = 0
#  while i < tope:
#    print(i)
#    i += 1
#cuenta(3)

#def es_par(numero):
#  if numero % 2 == 0:
#     return True
#  else:
#     return False

#def operacion(n):
#  if n > 10:
#    return 20
#    return 15
#  return 10
#  return 25
#resultado = operacion(8)
#resultado = operacion(12)


#def funcion(n):
#  a = n ** 3
#  b = a ** 2
#  c = b + 100
#  d = 5 * c
#  return print(d)

#d = funcion(2)


# LISTAS

#no_olvidar = [" huevos", "palta", "lechuga", "naranjas", 7000]
#for elem in no_olvidar:
#    print("no olvides", elem)

#no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
#no_olvidar[1] = "queso"
#no_olvidar[3] = 10000
#print(no_olvidar)

#Concatenación y repetición

#no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
#tambien = ["apio", "tomates"]
#no_olvidar = no_olvidar + tambien
#print(no_olvidar)
#print(tambien * 2)

#no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
#no_olvidar.append("apio")
#print(no_olvidar)

#Cuantos elementos hay?

#no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
#print("hay", len(no_olvidar), "cosas por comprar")
#no_olvidar.append("jamon")
#print("hay", len(no_olvidar), "cosas por comprar")

#Esta este element ?    in

#no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
#print("¿debo comrar vino?", ( "vino" in no_olvidar))
#print("¿debo comprar palta", ("palta" in no_olvidar))

#Donde esta este elemnto?  Lista.index(elemnto)

#no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]
#print("lechuga:", no_olvidar.index("lechuga"))
#print("Queso:", no_olvidar.index("queso"))


#De str a list

#texto = input("Ingrese una lista: ")
#print("primero: ", texto[0])
#print("No lista: ", texto)
#no_olvidar = []
#inicio = 0
#for i in range(0,len(texto)):
#    if texto[i] == ",":
#        no_olvidar.append(texto[inicio:i])
#        inicio = i+1
#no_olvidar.append(texto[inicio:])
#print("lista: ", no_olvidar)


#Ordenar lista
#comprar = [ [1800, "huevos"], [2300, "palta"],
#            [450, "naranjas"], [610, "queso"]]
#print("original:", comprar)
#comprar.sort()
#print("ordenada: ", comprar)

contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print(splitted)




















