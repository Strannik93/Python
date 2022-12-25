# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: Расширить значение коэффициентов до [-100..100]

import random
def create_equation():
    equation = {}
    n = int(input('Максимальная степень: '))
    for i in range(n, -1, -1):
        if i == n:
            while True:
                koef = random.randint(-100, 100)
                if koef != 0:
                    break
            equation[i] = koef
        else:
            equation[i] = random.randint(-100, 100)
    return equation

def convert_equation_text(equation: dict):
    equation_text = ''
    for key in equation:
        if key > 1 and key == len(equation) - 1:
            if equation.get(key) > 1 or equation.get(key) < -1:
                equation_text += f'{equation.get(key)}*x**{key} '
            elif equation.get(key) == 1:
                equation_text += f'x**{key} '
            else:
                equation_text += f'-x**{key} '
        elif key > 1:
            if equation.get(key) > 0:
                if equation.get(key) == 1:
                    equation_text += f'+ x**{key} '
                else:
                    equation_text += f'+ {equation.get(key)}*x**{key} '
            elif equation.get(key) < 0:
                if equation.get(key) == -1:
                    equation_text += f'- x**{key} '
                else:
                    equation_text += f'- {abs(equation.get(key))}*x**{key} '
        elif key == 1:
            if equation.get(key) > 0:
                if equation.get(key) == 1:
                    equation_text += f'+ x '
                else:
                    equation_text += f'+ {equation.get(key)}*x '
            elif equation.get(key) < 0:
                if equation.get(key) == -1:
                    equation_text += f'- x '
                else:
                    equation_text += f'- {abs(equation.get(key))}*x '        
        else:
            if equation.get(key) > 0:
                equation_text += f'+ {equation.get(key)}'
            elif equation.get(key) < 0:
                equation_text += f'- {abs(equation.get(key))}'
    return equation_text + ' = 0'

def convert_equation_dict(equation_text: str):
    equation = {}
    equation_text = equation_text.replace(' ', '').replace('*', '').replace('=0', '').replace('+', ' ').replace('-', ' -').split()
    if equation_text[len(equation_text)-1].startswith('-'):
        temp = 0
        for i in range(1, len(equation_text[len(equation_text)-1])):
            if equation_text[len(equation_text)-1][i].isdigit():
                temp += 1
        if temp == len(equation_text[len(equation_text)-1]) - 1:
            equation_text[len(equation_text)-1] += 'x0'
    else:
        if equation_text[len(equation_text)-1].isdigit():
            equation_text[len(equation_text)-1] += 'x0'
    for i in range(len(equation_text)):
        if (equation_text[i].startswith('x') or equation_text[i].startswith('-x')) and equation_text[i].endswith('x'):
            equation_text[i] = equation_text[i].replace('x', '1x1').split('x')
        elif equation_text[i].endswith('x'):
            equation_text[i] = equation_text[i].replace('x', 'x1').split('x')
        elif equation_text[i].startswith('x') or equation_text[i].startswith('-x'):
            equation_text[i] = equation_text[i].replace('x', '1x').split('x')
        else:
            equation_text[i] = equation_text[i].split('x')
    j = 0
    for i in range(int(equation_text[0][1]), -1, -1):
        if j <= len(equation_text)-1:
            if int(equation_text[j][1]) == i:
                equation[i] = int(equation_text[j][0])
                j += 1
            else:
                equation[i] = 0
        else:
            equation[i] = 0
    return equation

def sum_equation(equation_1: dict, equation_2: dict):
    equation_new = {}
    if len(equation_1) > len(equation_2):
        eq_max = len(equation_1)
    else:
        eq_max = len(equation_2)
    for key in range(eq_max-1, -1, -1):
        if len(equation_1) <= key:
            equation_new[key] = equation_2.get(key)
        elif len(equation_2) <= key:
            equation_new[key] = equation_1.get(key)
        else:
            equation_new[key] = equation_1.get(key) + equation_2.get(key)
    return equation_new

equation = create_equation()
print(equation)
equation_text = convert_equation_text(equation)
print(equation_text)
equation = convert_equation_dict(equation_text)
print(equation)
equation_new = {}
equation_x = create_equation()
print(equation_x)
equation_new = sum_equation(equation,equation_x)
print(equation_new)
equation_new_text = convert_equation_text(equation_new)
print(equation_new_text)
