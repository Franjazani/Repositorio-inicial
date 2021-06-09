print("Hola")

print("como estan?")

print("estamos estudiando Python")

print("al fin se esta imprimiendo")

print("como estas! Como es tu nombre?")
nombre = input()

if(nombre == ""):
    print("por favor escribe tu nombre")
    nombre = input()

print("ok, Hola", nombre,"¿como estas?")

def imprimirNombre():
    nombre = "Fran"
    print(nombre)

imprimirNombre()