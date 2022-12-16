# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 6782 -> 23        0,56 -> 11

number = input('Введите число: ')
result = 0
for i in range(len(number)):
    if number[i] != '.':
        result += int(number[i])
print(f'Сумма цифр числа = {result}')