"""
Peça ao usuário para inserir dois números e calcule o máximo divisor comum usando o algoritmo de Euclides.
- Implementar uma função separada para cada cálculo.
"""

first_number = int(input("Insira o primeiro número: "))
second_number = int(input("Insira o segundo número: "))

def greatest_common_divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

first_number_divisors = greatest_common_divisor(first_number)
second_number_divisors = greatest_common_divisor(second_number)
        
print(f"Os divisores de {first_number} são {first_number_divisors}")
print(f"Os divisores de {second_number} são {second_number_divisors}")

common_divisors = []
for i in first_number_divisors:
    for j in second_number_divisors:
        if i == j:
            common_divisors.append(i)
            
print(f"O MDC entre {first_number} e {second_number} é igual a {max(common_divisors)}.")