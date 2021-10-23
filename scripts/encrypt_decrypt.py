
def encrypt(cadena: str) -> str:
    """Función encargada de encriptar
    una cadena de texto.

    Args:
        cadena (str): Cadena a encriptar

    Returns:
        str: cadena encriptada
    """

    asciiConcatenado: str = "" 
    cadenaEncriptada: str = "" # Espacio para cadena ya encriptada

    # Paso 1
    concatCodAscii = "" # Cadena para concatenar los códigos ASCII
    for letter in cadena:
        codAscii = str(ord(letter)).zfill(3) # Pasar el código Ascii
        codAscii = codAscii[-1]+codAscii[0]+codAscii[1] # Rotar el código Ascii de ABC a CAB
        concatCodAscii += codAscii # Concatenar los nuevos códigos ASCII

    # Paso 2
    listNewCodAscii = [] # Lista para guardar los códigos ASCII del paso 2
    cadenaImpar =  (len(concatCodAscii) % 2 == 1) # Calcular si la cadena es impar
    while len(concatCodAscii) > 1:
        addCodAscii = concatCodAscii[0:2].zfill(2) # Ir obteniendo los 2 primeros caracteres
        concatCodAscii = concatCodAscii[2:] #Eliminar los caracteres obtenidos
        listNewCodAscii.append(addCodAscii) # Agregarlos a la lista

    if cadenaImpar is True:
        # Sí quedo un último de longitud 1
        concatCodAscii = concatCodAscii[-1]
        listNewCodAscii.append(addCodAscii) # Agregarlo a la lista

    # Paso 3
    for i in range(len(listNewCodAscii)):
        codA = int(listNewCodAscii[i])+33
        listNewCodAscii[i] = str(codA).zfill(3)

    # Paso 4
    for item in listNewCodAscii:
        cadenaEncriptada += chr(int(item))

    # Paso 5
    if cadenaImpar:
        cadenaEncriptada += "¿"

    return cadenaEncriptada


def decrypt(cadenaEncriptada: str) -> str:
    """Función encargada de desencriptar
    una cadena de texto.

    Args:
        cadenaEncriptada (str): Cadena a desencriptar

    Returns:
        str: cadena desencriptada
    """

    cadenaDesencriptada: str = "" # Espacio para la cadena ya desencriptada

    # TO DO: Proceso desencriptar


    return cadenaDesencriptada # Retorno cadena desencriptada


# Ejecución del programa sí se ejecuta como script
if __name__ == "__main__":

    # Ejecución del programa
    from os import system

    # Definición de función de menú principal
    def menu():
        print("""
    1. Cifrar
    2. Descifrar
    3. Salir
    """)

    # Variable para controlar el bucle principal
    salir = False

    # Bucle principal
    while salir is False:
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            cadena = input("Ingrese la cadena a cifrar: ")
            cadenaEncriptada = encrypt(cadena)
            print("Cadena cifrada: ", cadenaEncriptada)
        elif opcion == "2":
            cadenaEncriptada = input("Ingrese la cadena a descifrar: ")
            cadenaDesencriptada = decrypt(cadenaEncriptada)
            print("Cadena descifrada: ", cadenaDesencriptada)
        elif opcion == "3":
            salir = True
        else:
            print("Opción inválida")

        # Pausa
        input("\nPresione una tecla para continuar...")
        
        # Limpiar pantalla
        system("cls")


    print("Fin del programa")
    input("Pulse una tecla para continuar... ")
    print("\n")
    