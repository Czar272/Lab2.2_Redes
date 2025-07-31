from fletcher import emisor_fletcher
from viterbi import emisor_viterbi

def agregar_integridad(bits: str, algoritmo: str) -> str:
    if algoritmo == "fletcher":
        return emisor_fletcher(bits)
    elif algoritmo == "viterbi":
        return emisor_viterbi(bits)
    else:
        print("Algoritmo no válido. Se usará Fletcher por defecto.")
        return emisor_fletcher(bits)
