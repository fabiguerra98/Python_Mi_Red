print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

nombre = input("¿Para comenzar, cúal es tu nombre?")
print()
print("Hola" , nombre, "bienvenido a mi red")
print()

agno = int (input(" para preparar tu perfil, dime en que año naciste?"))
edad = 2023-agno-1
print()


sexo = input("¿Cuál es tu sexo? ")
if sexo.lower() == "hombre":
    print(" En efecto eres un hombre.")
elif sexo.lower() == "mujer":
    print("En efecto eres una mujer.")
else:
    print("Sexo no reconocido.")

numero_t = int(input("indicanos tu numero telefonico: "))
print()

ciudad_n = input("¿Cual es tu ciudad de nacimiento? ")
print()

dirección = (input("ingrese su direccion"))
print()



estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. cuanto mides? dimelo en metro. "))
estatura_m = int(estatura)
estatura_cm = int(( estatura - estatura_m)*100)
print(" {},{}  metros de estatura" .format(estatura_m, estatura_cm))

num_amigos = int(input(" Muy bien. finalmente, cuentame ¿Cuantos amigos tienes?"))

print()
print("muy bien", nombre, ". Entonces podemos crear un perfil con estos datos.")
print(" ------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad, "años")
print("tu sexo es:", sexo)
print("Tu direeción es:", dirección)
print("Tu numero telefonico es:", numero_t)
print("Tu ciudad de nacimiesto es:", ciudad_n)
print("Estatura", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos: ", num_amigos)
print("-------------------------------")
print("Gracias por la información. Esperamos que disfrutes con mi red :D")
print()

mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿ En que piensas hoy? ")
print()
print("--------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------")


