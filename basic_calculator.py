"""
Crie uma calculadora que permita ao usuário escolher uma operação (+, -, *, /) e insira dois números para realizar o cálculo
- Tratar divisão por zero
- Adicionar opção de repetir ou sair da calculadora 
"""

print("Gostaria de executar algum cálculo? S/N")
answer = input("")

if answer == 'S':
    while answer == 'S':
        operator = input("Qual operação você deseja executar?\n")

        first_num = int(input("Qual o primeiro número?\n"))
        second_num = int(input("Qual o segundo número?\n"))

        match operator:
            case "+":
                result = first_num + second_num
                print(f"O resultado de {first_num} + {second_num} = {result}")
            case "-":
                result = first_num - second_num
                print(f"O resultado de {first_num} - {second_num} = {result}")
            case "*":
                result = first_num * second_num
                print(f"O resultado de {first_num} * {second_num} = {result}")
            case "/":
                if second_num != 0:
                    result = first_num / second_num
                    print(f"O resultado de {first_num} / {second_num} = {result}")
                else:
                    print("Divisão por 0 não é permitido.")
            case _:
                print("Essa não é uma operação válida.") 
        print("Gostaria de executar mais algum cálculo? S/N")
        answer = input("")
else:
    exit()