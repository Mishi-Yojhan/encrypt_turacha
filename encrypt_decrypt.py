
def encrypt(cadena: str) -> str:
    """Función encargada de encriptar la cadena ingresada

    Args:
        cadena (str): Cadena a ingresar

    Returns:
        str: Cadena ya encriptada
    """

    asciiConcatenado: str = "" 
    cadenaEncriptada: str = "" # Espacio para cadena ya encriptada

    # Paso 1
    concatCodAscii = "" # Cadena para concatenar los códigos ASCII
    for letter in cadena:
        codAscii = str(ord(letter)).zfill(3) # Pasar el código Ascii
        codAscii = codAscii[-1]+codAscii[0]+codAscii[1] # Rotar el código Ascii de ABC a CAB
        concatCodAscii += codAscii # Concatenar los nuevos códigos ASCII

    return cadenaEncriptada


def decrypt(cadenaEncriptada: str) -> str:
    """Función encargada de desencriptar

    Args:
        cadenaEncriptada (str): Cadena a desencriptar

    Returns:
        str: cadena desencriptada
    """

    cadenaDesencriptada: str = "" # Espacio para la cadena ya desencriptada

    # TO DO: Proceso desencriptar

    return cadenaDesencriptada # Retorno cadena desencriptada
