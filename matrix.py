"""
Написать функцию сортировки двухмерного списка МхМ (матрицы)
Значение М - задаётся пользователем, с клавиатуры. Может быть любым
целым, положительным числом, больше 5.
Функция должна:
1. найти сумму элементов столбцов и отсортировать столбцы по
возрастанию этих сумм
2. отсортировать каждый нечётный столбец по возрастанию значений снизу
вверх, а каждый чётный столбец по возрастанию значений сверху вниз.
Так же, ваша программа должна иметь функцию вывода данного списка
на экран. При выводе, внизу каждого столбца должна выводиться сумма
элементов этого столбца.
Что можно использовать:
1. для создания списка использовать ТОЛЬКО 'list comprehension' и
генератор случайных чисел. Диапазон случайных чисел для заполнения
списка от 1 до 50. Список должен создаваться однострочным
выражением.
2. Можно использовать ТОЛЬКО ДВА списка. Первый это двухмерный список
размером МхМ, второй, вспомогательный, одномерный список размером
М. Использование других списков (или коллекций) НЕДОПУСТИМО.
3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера
списка, плюс переменные циклов for.
4. Для сортировки можно использовать алгоритм пузырьковой сортировки.
Использование встроенных функций сортировки - НЕДОПУСТИМО (да и не
получится их использовать)!
5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (по
правилам описанным выше) и функцию вывода на экран.
Задача считается решённой верно при условии соблюдения всех требований.
Аккуратный вывод на экран - приветствуется.
Пример вывода задачи:
До сортировки
47 48 36 12 39 33 13 1 47 20
17 2 9 40 2 1 36 35 48 44
50 24 20 29 27 49 8 50 20 32
30 3 17 33 43 10 17 2 42 19
14 5 50 38 17 18 24 26 19 24
12 41 45 12 4 33 33 16 36 25
15 27 12 30 22 36 45 46 43 21
46 34 34 47 22 34 45 12 47 19
31 47 2 1 12 45 44 26 11 23
25 49 47 50 36 9 36 10 21 26
287 280 272 292 224 268 301 224 334 253
После сортировки
43 1 44 1 50 2 50 1 45 11
39 2 32 9 47 3 47 12 45 19
36 10 26 10 45 5 46 12 44 20
27 12 25 18 36 24 31 29 36 21
22 16 24 33 34 27 30 30 36 36
22 26 23 33 20 34 25 33 33 42
17 26 21 34 17 41 17 38 24 43
12 35 20 36 12 47 15 40 17 47
4 46 19 45 9 48 14 47 13 47
2 50 19 49 2 49 12 50 8 48
224 224 253 268 272 280 287 292 301 334

"""



from random import randint


# bubble sort for the list and matrix of numbers, depend on trigger - sorts matrix (if True) and list (if False)
def get_sorted(arr: list, trigger: bool = False) -> list:

    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if trigger:
                if sum(arr[j]) > sum(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# function that gets size, creates, sums column of numbers and prints matrix
def print_sorted_matrix() -> None:

    try:
        matrix_size = int(input('Please type size of the matrix, '
                                'the size should be number and not less than 5: '))
        if matrix_size < 5:
            raise TypeError
    except (TypeError, ValueError):
        print('Entered symbol is not a number or less than 5, '
              'in the next time - please type a number and which is grater than 5!')
        exit('Adios;)')

    # gets matrix from given size
    matrix = [[randint(1, 50) for i in range(matrix_size)]
              for i in range(matrix_size)]

    # gets list of sums numbers in columns
    aux_list = list(map(sum, list(zip(*matrix))))

    # prints matrix and auxiliary list before sort
    print('\n\nBefore sorting')
    for i in matrix:
        for j in i:
            print(f'{j: >5}', end='')
        print('\n', end='')

    for k in aux_list:
        print(f'{k: >5}', end='')

    # turn and sort
    matrix = list(map(get_sorted, get_sorted(list(map(list, zip(*matrix))), True)))

    # reverses list
    matrix = list(map(lambda x: x[::-1] if matrix.index(x) % 2 == 0 else x, matrix))

    # gets list of sums numbers in columns
    aux_list = list(map(sum, matrix))

    # turn matrix to the source position
    matrix = list(map(list, zip(*matrix)))

    # prints matrix and auxiliary list after sort
    print('\n\nAfter sorting')
    for i in matrix:
        for j in i:
            print(f'{j: >5}', end='')
        print('\n', end='')

    for k in aux_list:
        print(f'{k: >5}', end='')


if __name__ == '__main__':
    print_sorted_matrix()
