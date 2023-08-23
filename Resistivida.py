#Resistencia en un conductor electrico
# R = p * (L/S)

resistividad = {"Al" : (0.028, "Aluminio"), 
                "Cu" : (0.017, "Cobre"), 
                "Au" : (0.023, "Oro"),
                "Hg" : (0.96, "Mercurio"),
                "Ag" : (0.016, "Plata"),
                "Pb" : (0.22, "Plomo")}
L = float(input("Ingresa la longitud del conductor en [m] "))

while True:

    S=float(input("Ingresa la seccion del conductor en [mm2]: "))

    if S == 0:

        print("Error, la sección no puede ser cero. Ingresa una sección diferente.")

    else:

        break

while True:

    material = input("Ingresa el símbolo del material: ")

    if material in resistividad:

        p = resistividad[material][0] / 1000  

        print("Resistividad de", resistividad[material][1], "=[ohm.m/m]")

        R = p * (L / S)

        print("La resistencia =", R, "ohms")

        break

    else:

        print("Lo sentimos pero material no encontrado.Intenta con otro material: ")

# while True:
#     S = float(input("Ingresa la seccion del conductor en [mm2] "))

#     if S == 0:
#         print("Error. la seccion no puede ser cero, ingresa una seccion diferente")
#     else:
#         break

#     R = p * L/S

#     print("La resistencia de ", R, "ohms")

#     if material in resistividad:
#         material = input("Ingresa el simbolo del material ")
#         p = resistividad [material][0]
#         print("Resistencia de ",resistividad[material][1], " = [ohm.mm1/m]")

#     else:

#         print("Material no existe")




