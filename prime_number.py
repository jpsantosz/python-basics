"""
Peça ao usuário para inserir um número e determine se ele é primo ou não.
- Exibir todos os números primos de 1 até o número fornecido.
- Implementar uma função separada para verificar se um número é primo.
"""

def is_prime(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) > 2:
        return f"{num} é um número composto"
    else:
        return f"{num} é um número primo"
    
def all_prime_numbers(num):
    prime_numbers = []
    for i in range(2, num + 1):
        result = is_prime(i)
        if result == f"{i} é um número primo":
            prime_numbers.append(i)
    return prime_numbers
    
number = int(input("Digite um número: "))
result = is_prime(number)
print(result)
print(all_prime_numbers(number))