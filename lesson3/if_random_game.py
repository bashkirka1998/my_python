#if_random_game.py
import random
def random_game():
    num=int(input('Введите число от 1 до 4 \n'))
    rez=random.randint(1,4)
    if num==rez:
        return 'Победа!'
    elif num>rez:
        return 'Повторите еще раз! Результат меньше, чем введенное число!'
    elif num<rez:
        return 'Повторите еще раз! Результат больше, чем введенное число!'
print(random_game())
