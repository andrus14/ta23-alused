import random

secret = random.randrange(1, 101)

guess = 0

while secret != guess:
    guess = int(input('Paku arv 1..100: '))

    if guess < secret:
        print('Paku suurem arv')
    elif guess > secret:
        print('Paku väiksem arv')

print('Õige!')