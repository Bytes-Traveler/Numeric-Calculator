from Logic import converters

def calculate(num1_str, num2_str, base, operation):

    bases = {
        'binario': 2,
        'octal': 8,
        'decimal': 10,
        'hexadecimal': 16
    }

    # Normalizar entradas
    base = base.lower()
    operation = operation.lower()

    # Validar base
    if base not in bases:
        raise ValueError(f'La base {base} no está soportada (válidas: {', '.join(bases.keys())})')

    # Convertir entradas a decimal
    try:
        n1 = int(num1_str, bases[base])
        n2 = int(num2_str, bases[base])
    except ValueError:
        raise ValueError(f'Entrada inválida para la base {base}: {num1_str}, {num2_str}')

    # Realizar operación
    if operation == 'suma':
        result = n1 + n2
    elif operation == 'resta':
        result = n1 - n2
    elif operation == 'multiplicación':
        result = n1 * n2
    elif operation == 'división':
        if n2 == 0:
            raise ValueError('División por cero no permitida')
        result = n1 // n2 
    else:
        raise ValueError(f'Operación {operation} no soportada')

    # Convertir resultado a la base seleccionada
    match base:
        case 'decimal':
            return converters.from_decimal(result, 10)
        case 'binario':
            return converters.from_decimal(result, 2)
        case 'octal':
            return converters.from_decimal(result, 8)
        case 'hexadecimal':
            return converters.from_decimal(result, 16)
