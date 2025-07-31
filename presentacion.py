def codificar_mensaje(mensaje: str) -> str:
    binario = ''.join(f'{ord(c):08b}' for c in mensaje)
    return binario

# Prueba
if __name__ == "__main__":
    mensaje = "Hola"
    binario = codificar_mensaje(mensaje)
    print(f"Mensaje original: {mensaje}")
    print(f"Codificado a binario ASCII: {binario}")
