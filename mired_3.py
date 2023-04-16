#Vamos a modificar el cÃ³digo que acabamos de ver para encapsular algunas partes de Ã©l
#en funciones.

#En particular haremos esto con:
#1. El mensaje de bienvenida
#2. El codigo para solicitar datos al usuario.
#3. El codigo para mostrar el perfil del usuario
#4. El codigo para mostrar un mensaje en pantalla

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input(" Para comenzar, dime cual es tu nombre. ")
    return nombre

def obtener_edad():
    agno = int(input(" Para preparar tu perfil, dime en que año naciste"))
    return 2023-agno-1

def obtener_sexo():
    sexo = input(" Indicanos cual es tu sexo: ")
    if sexo.lower() == "hombre":
        print()
    elif sexo.lower() == "mujer":
        print()
    return sexo



def obtener_estatura():
    estatura = float(input("Cuentame mas de ti , para agregarlo a tu perfil. cuanto mides?, Dimelo en metros"))
    metros = int(estatura)
    centimetros = int(( estatura - metros)*100)
    return (metros, centimetros)

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, Cuentame cuantos amigos tienes. "))
    return amigos

def mostrar_perfil(nombre, edad, sexo,  estatura_m, estatura_cm, num_amigos,):
    print("-----------------------------------------------")
    print("Nombre: ", nombre)
    print("Edad: ", edad, "Años")
    print("Tu sexo es: ", sexo)
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centimetros")
    print("Amigos: ", num_amigos)
    print("-----------------------------------------------")

def opcion_menu():
    print("Acciones disponibles: ")
    print(" 1. Escribir un mensaje publico ")
    print(" 2. Escribir un mensaje solo a algunos amigos ")
    print(" 3. Mostrar los datos del perfil ")
    print(" 4. Actualizar el perfil del usuario")
    print(" 0. Salir ")
    opcion = int(input("Ingresa una opción "))
    while opcion < 0 or opcion > 4:
        print(" No conozco la opcion que has ingresado. Intentelo otra vez. ")
        opcion = int(input(" Ingresa una opcion: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Que piensas hoy ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("------------------------------------------")
    if destinatario == None:
        print(origen, "dice: ", mensaje)
    else:
        print(origen, "dice: ", "@"+destinatario,  mensaje)
    print("-------------------------------------------")

# El Codigo anterior era solamente definicion de funciones que seran usadas mas adelante
# Ahora empieza el programa principal.

mostrar_bienvenida()
nombre = obtener_nombre()
print()
print("Hola", nombre, "Bienbenido a Mi Red")
print()
edad = obtener_edad()
sexo = obtener_sexo()
(estatura_m, estatura_cm ) = obtener_estatura()
num_amigos = obtener_num_amigos()
print("Muy buen", nombre, "Entonces podemos crear tu perfil con estos datos")
mostrar_perfil(nombre, edad,  sexo, estatura_m, estatura_cm, num_amigos)
print(" Ya podemos preguntar, recordar y calcular datos. Esperemos que disfrutes con Mi Red")
print("---------------------------------------------------")


# Ingresamos al ciclo que permite ejecutar acciones
opcion = 1
while opcion != 0:
    opcion =  opcion_menu()

# Codigo para la opcion 1 . Publicar mensaje.
    if opcion == 1:
        mensaje = obtener_mensaje()
        mostrar_mensaje(nombre, None, mensaje)

    elif opcion == 2:
        mensaje = obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mostrar_mensaje(nombre, nombre_amigo, mensaje)

    elif opcion == 3:
        mostrar_perfil(nombre, edad, sexo, estatura_m, estatura_cm, num_amigos)

    elif opcion == 4:
        nombre = obtener_nombre()
        edad = obtener_edad()
        sexo = obtener_sexo()
        (estatura_m, estatura_cm) = obtener_estatura()
        num_amigos = obtener_num_amigos()
        mostrar_perfil(nombre, edad, sexo,  estatura_m, estatura_cm, num_amigos)
    elif opcion == 0:
        print("Has decidido salir. ")

print("Gracias por usar Mi Red, Hasta Pronto!")






