"""
O programa escolhe um número aleatório entre 1 e 20, e o usuário precisa adivinhar qual é o número. O programa deve dar dicas de "maior" ou "menor" até que o usuário acerte.
- Limitar o número de tentativas.
- Exibir a pontuação baseada no número de tentativas usadas.
"""
import random

number = random.randint(0, 20)

print("Tente adivinhar o número secreto entre 1 e 20. Você tem 5 chances.")
guess = int(input("Digite o número: "))
number_of_guesses = 1

while number_of_guesses < 5:
    if guess != number:
        number_of_guesses += 1
        if guess > number:
            print("Ops, você errou! O número secreto é menor que sua tentativa.")
        if guess < number:
            print("Ops, você errou! O número secreto é maior que sua tentaiva.")
        guess = int(input("Digite o número: "))
    else:
        print("Parabéns, você venceu!")
        exit()
    if number_of_guesses == 5:
        print("Game over! Tente novamente!")
        exit()