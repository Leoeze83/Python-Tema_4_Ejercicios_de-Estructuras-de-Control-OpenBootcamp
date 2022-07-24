"""
Consigna:
 Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
# Solicito al usuario su edad
# Valido si su type es str , vuelvo a solicitar el dato en type numerico

print("Ingrese su edad y presione la tecla Enter")
edad = input()
if isinstance(edad, str):
    print("La edad debe ser ingresada en números , por favor vuelva a introducirlo ")
    edad = input()
elif isinstance(edad, int):
    if edad >= 21:
        print("Usted tiene ", edad, " años. Es mayor de edad")
    else:
        print("Su edad es: ", edad, " años, usted no es mayor de edad")
