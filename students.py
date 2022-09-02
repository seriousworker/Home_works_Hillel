"""
1. В текстовый файл (файл прилагается), построчно записаны имя и
фамилия учащихся класса и их оценки.
Вывести на экран всех учащихся, чей средний балл меньше 5, также
посчитать и вывести средний балл по классу. Так же, записать в новый
файл всех учащихся в формате "Фамилия И. Ср. балл":

Говорухи А. 5.83
Петров В. 4.92
Варфаломеев Г. 5.92
Тюльпанов И. 4.08
Муромцев И. 5.42
Бессмертный К. 5.5
Мухин М. 6.92
Мартынова М. 6.08
Николаев П. 5.17
Гусева Г. 5.83
Тереньтьев С. 6.42
Трердолобов С. 5.33

Выравнивание колонок - ОБЯЗАТЕЛЬНО!

"""


# get file path from user
def get_file_path() -> str:
    file_path = input('Please type path and name of the source file: ')
    return file_path


# get path and name of the file to save
def get_path_to_save() -> str:
    file_path = input('Please type name and path to the save file: ')
    return file_path


# print student's name, surname and medium marks
def print_student(student_name: list, med_marks: int) -> None:
    name_abr = ' ' + student_name[0][0] + '.'
    print(f'{student_name[1] + name_abr: <15} {med_marks: >12.2f}')


# write student's name, surname and medium marks in file
def write_in_file(student_name: list = None, marks: int = None, file_path: str = None, trigger: bool = False) -> None:
    with open(file_path, 'a') as file:

        if trigger:
            names = 'Фамилия И.:'
            med_marks = 'Ср. бал:'
            file.write(f'{names: <15}{med_marks: >15}\n\n')
        else:
            name_abr = ' ' + student_name[0][0] + '.'
            file.write(f'{student_name[1] + name_abr: <15} {marks: >12.2f}\n')


# count medium mark per student
def count_med(marks: list) -> int:
    med_marks = sum(marks) / len(marks)
    return med_marks


# extract marks from the line
def get_marks(student: str) -> list:
    rs_stud = student.rstrip()
    extracted_digits = [int(i) for i in rs_stud.split() if i.isdigit()]
    return extracted_digits


# extract name from the given string, return list with full name and surname
def get_name(student: str) -> list:
    rs_stud = student.rstrip()
    extracted_name = [i for i in rs_stud.split() if i.isalpha()]
    return extracted_name


# count students in the class
def count_students():
    start_count = 0

    def func():
        nonlocal start_count
        start_count += 1
        return start_count

    return func


# count all marks in the class
def count_all_marks():
    mark_total = 0

    def count(mark):
        nonlocal mark_total
        mark_total += mark
        return mark_total

    return count


# counter for header
def header():
    start = 0

    def count():
        nonlocal start
        start += 1
        return start

    return count


# count medium mark in class between the whole students
def count_medium_mark_in_class(med_marks: float, students: int) -> float:
    return med_marks/students


def main() -> None:
    count_students_in_class = count_students()
    path = get_file_path()
    count_class_marks = count_all_marks()
    path_to_save = get_path_to_save()
    print_header = header()

    try:
        print('\n')
        write_in_file(file_path=path_to_save, trigger=True)
        with open(path) as file:
            for line in file.readlines():
                count_students_in_class()

                student_name = get_name(line)

                marks = get_marks(line)
                med_mark = count_med(marks)
                count_class_marks(med_mark)

                write_in_file(student_name, med_mark, file_path=path_to_save)

                # print names with medium marks less than 5 and header
                if med_mark < 5:
                    if print_header() < 2:
                        print('Учащиеся, чьи средние быллы меньше 5:\n')
                    print_student(student_name, med_mark)

    except (FileNotFoundError, PermissionError, ZeroDivisionError):
        print('Either name or path to the source file is wrong!')
        exit()

    print(f'\nСредний бал по классу: {count_medium_mark_in_class(count_class_marks(0), count_students_in_class()): .2f}')


if __name__ == '__main__':
    main()
