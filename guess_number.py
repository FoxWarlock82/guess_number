from random import randint

comp_number = randint(1, 100)

while True:
    gamer_number = int(input('Ваше число от 1 до 100: '))

    if comp_number > gamer_number:
        print('Ваше число меньше того, что загадано')
    elif comp_number < gamer_number:
        print('Ваше число больше того, что загадано')
    else:
        break


print('Отличная интуиция! Вы угадали число :)')
