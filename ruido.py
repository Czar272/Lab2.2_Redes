import random

def aplicar_ruido(bits: str, probabilidad: float) -> str:
    bits_con_ruido = ""
    for bit in bits:
        if random.random() < probabilidad:
            # Flip del bit
            bits_con_ruido += '0' if bit == '1' else '1'
        else:
            bits_con_ruido += bit
    return bits_con_ruido

def solicitar_probabilidad():
    try:
        tasa = int(input("Ingrese la tasa de error (ej: 100 para 1 error cada 100 bits): "))
        if tasa <= 0:
            raise ValueError
        return 1.0 / tasa
    except:
        print("Valor inválido, se usará tasa por defecto 1/100")
        return 1.0 / 100
