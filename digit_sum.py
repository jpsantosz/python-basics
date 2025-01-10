"""
Peça ao usuário para inserir um número inteiro e exiba a soma de todos os seus dígitos.
- Repetir o processo até que a soma seja apenas um dígito (redução digital).
- Tratar números negativos.
"""

number = int(input("Insira um número inteiro: "))
list = []

for num in str(number):    
    list.append(int(num))

sum = 0    
for digit in list:
    sum += digit
    
print(f"A soma dos dígitos é igual a {sum}.")