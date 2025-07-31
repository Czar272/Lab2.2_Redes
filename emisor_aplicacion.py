from presentacion import codificar_mensaje
from enlace import agregar_integridad
from ruido import aplicar_ruido, solicitar_probabilidad

def solicitar_mensaje():
    mensaje = input("Ingrese el mensaje a enviar: ")
    print("Seleccione algoritmo de integridad:")
    print("1. Fletcher Checksum")
    print("2. Viterbi (codificador convolucional)")
    opcion = input("Opción (1 o 2): ")
    
    if opcion == "1":
        algoritmo = "fletcher"
    elif opcion == "2":
        algoritmo = "viterbi"
    else:
        print("Opción inválida. Usando Fletcher por defecto.")
        algoritmo = "fletcher"
    
    return mensaje, algoritmo

if __name__ == "__main__":
    mensaje, algoritmo = solicitar_mensaje()
    binario = codificar_mensaje(mensaje)
    print(f"Binario ASCII: {binario}")
    
    codificado = agregar_integridad(binario, algoritmo)
    print(f"Trama con integridad ({algoritmo}): {codificado}")

    prob = solicitar_probabilidad()
    final = aplicar_ruido(codificado, prob)
    print(f"Trama con ruido aplicado: {final}")