"""
Peça ao usuário para inserir um número e exiba a tabuada completa (de 1 a 10) desse número.
- Permitir que o usuário escolha até qual número deseja ver a tabuada.
- Exibir a tabuada de vários números consecutivos.
"""

number = int(input("Qual número deseja exibir a tabuada?\n"))
limit = int(input("Até que número deseja gerar a tabuada?\n"))

for i in range(0, limit + 1):
    multiplication = i * number
    print(f"{number} * {i} = {multiplication}")