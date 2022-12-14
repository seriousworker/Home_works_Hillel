"""
1. Создать view-функцию, которая будет возвращать средний рост и средний вес (в см и кг соответственно) для студентов из файла hw.csv

  get_avr_data() -> 127.0.0.1:5000/avr_data

В файле, исходные данные, заданы в дюймах для роста и в фунтах для веса. Соответственно, необходимо предусмотреть преобразование результатов к килограммы и сантиметры.

Плюс, хоть файл и имеет расширение CSV, данные в нём записаны по другому. Так что читать его как правильный CSV файл не стоит. Могу предложить, читать его как текстовый, построчно.


2. Создать view-функцию, которая возвращает содержимое файла с установленными пакетами в текущем проекте (requirements.txt)

  get_requirements() -> 127.0.0.1:5000/requirements

Для создания файла requirements.txt необходимо, в терминале (находясь в папке проекта) ввести команду: pip freeze > requirements.txt

"""



from flask import Flask

app = Flask(__name__)


def get_val_from_file() -> tuple | float:
    students = 0
    height = 0
    weight = 0

    with open('hw.csv') as file:
        for line in file:
            tem_lis = line.rstrip().split(', ')
            if tem_lis[0].isdigit():
                height += float(tem_lis[1])
                weight += float(tem_lis[2])
                students += 1

    return students, height, weight


def convert_to_metric(value: float, unit: float) -> float:
    return value / unit


def count_med_in_class(students: int, value: float) -> float:
    return round(value / students, 1)


def get_avr_data():
    values = get_val_from_file()
    height = convert_to_metric(values[1], 0.393701)
    weight = convert_to_metric(values[2], 2.204)
    med_height = count_med_in_class(values[0], height)
    med_weight = count_med_in_class(values[0], weight)
    return values[0], med_height, med_weight


# route to get average height and weight from the given file
@app.route('/avr_data')
def resp_avr_data():
    students, med_height, med_weight = get_avr_data()
    response = f'<h2>With total quantity of students - {students} pers., </h2>' \
               f'<h2>Medium height is - {med_height}cm, and medium weight is - {med_weight}kg '
    return response


# route to get installed requirements from the requirements.txt
@app.route('/requirements')
def get_requirements():
    with open('requirements.txt') as file:
        requirements = file.read()
    return f'<pre>{requirements}</pre>'
