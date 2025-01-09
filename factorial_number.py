"""
Peça ao usuário para inserir um número e calcule o fatorial dele.
- Implementar usando recursão.
- Verificar se o número é negativo e exibir uma mensagem apropriada.
"""

def factorial(num):
    answear = 1
    for i in range(1, num):
        answear += answear * i
    return answear

number = int(input("Digite um número: "))
result = factorial(number)
print(f"O fatorial de {number} é igual a {result}.")