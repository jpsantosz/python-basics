"""
Peça ao usuário para inserir uma lista de números separados por vírgula e exiba a média deles.
- Permitir que o usuário insira números indefinidamente até digitar “sair”.
- Exibir a média arredondada para duas casas decimais.
"""

numbers = []
number = input("Insira um número: ")
soma = 0

while number != "sair":
    soma += int(number)
    numbers.append(int(number))
    number = input("Insira um número: ")
    
average = soma / len(numbers)
print(f"A média de {numbers} é igual a {round(average, 2)}.")