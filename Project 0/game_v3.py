"""Игра компьютер угадает число меньше чем за 20 попыток"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1
    max = 101
    number = np.random.randint(min, max)
    mid = (min+max) // 2 #используем бинарный поиск
    
    while True:
        count += 1
        if mid > number:
            max = mid
            mid = (min+max) // 2
        elif mid < number:
            min = mid
            mid = (min+max) // 2
        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return(count)
   
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)