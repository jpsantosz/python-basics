"""
Peça ao usuário para inserir um número n e exiba os primeiros n termos da sequência de Fibonacci.
- Implementar a solução de forma recursiva.
- Exibir apenas os termos ímpares da sequência.
"""

def fibonacci(num):
    fib_sequence = [0, 1]
    for i in range(2, num):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[:num]

number = int(input("Digite um número: "))
result = fibonacci(number)
print(f"Os primeiros {number} números da sequência de Fibonacci são {result}.")