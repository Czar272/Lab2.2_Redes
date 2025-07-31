def pad_to_bytes(bits: str) -> list[int]:
    while len(bits) % 8 != 0:
        bits += '0'
    return [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]

def fletcher16(data: list[int]) -> tuple[int, int]:
    s1 = 0
    s2 = 0
    for byte in data:
        s1 = (s1 + byte) % 255
        s2 = (s2 + s1) % 255
    return s1, s2

def emisor_fletcher(bits: str) -> str:
    data_bytes = pad_to_bytes(bits)
    s1, s2 = fletcher16(data_bytes)
    checksum = f'{s1:08b}{s2:08b}'
    return bits + checksum
