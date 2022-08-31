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
