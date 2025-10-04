DIGITS = '0123456789ABCDEF'
DIGIT_MAP = {ch: i for i, ch in enumerate(DIGITS)}

def to_decimal(num_str, base):

    if not (2 <= base <= len(DIGITS)):
        raise ValueError(f'La base {base} no está soportada (mínimo 2, máximo {len(DIGITS)})')

    num_str = num_str.upper()
    decimal_value = 0
    power = 0

    for digit in reversed(num_str):
        if digit not in DIGITS[:base]:
            raise ValueError(f' {digit} no es válido en base {base} para el número {num_str}')
        value = DIGIT_MAP[digit]
        decimal_value += value * (base ** power)
        power += 1

    return decimal_value


def from_decimal(number, base):

    if not (2 <= base <= len(DIGITS)):
        raise ValueError(f'La base {base} no está soportada (mínimo 2, máximo {len(DIGITS)})')

    if number == 0:
        return '0'

    digits = []
    n = number

    while n > 0:
        remainder = n % base
        digits.append(DIGITS[remainder])
        n //= base

    return ''.join(reversed(digits))


def convert(num_str, base_origen, base_destino):

    decimal_value = to_decimal(num_str, base_origen)

    return from_decimal(decimal_value, base_destino)
