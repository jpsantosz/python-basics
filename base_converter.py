"""
Peça ao usuário para inserir um número decimal e converta-o para binário, octal e hexadecimal.
- Permitir a conversão de qualquer base para qualquer outra base.
- Validar a entrada para aceitar apenas números válidos.
"""

numero_decimal = int(input("Digite um número decimal: "))

def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

binario = decimal_para_binario(numero_decimal)
print(f"O número {numero_decimal} em binário é: {binario}")