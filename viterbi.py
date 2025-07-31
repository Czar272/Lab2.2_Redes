def emisor_viterbi(bits: str) -> str:
    state = [0, 0]  # Registros de desplazamiento
    salida = ""
    for bit in bits:
        bit = int(bit)
        g1 = bit ^ state[0] ^ state[1]  # G1 = 111
        g2 = bit ^ state[1]             # G2 = 101
        salida += f"{g1}{g2}"
        state = [bit] + state[:1]
    return salida
