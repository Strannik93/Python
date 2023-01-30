import model

def not_in_list():
    print('Такого ученика нет')

def error_found(check = True):
    if check == True:   print('Нет введенного класса')
    else: print('Нет введенного предмета')

def get_check():
    check = input('Если хотите продолжить работу с другим классом, введите yes: ')
    if check.lower() == 'yes': return True
    else: return False

def input_class():
        print('Для выхода в этом или следующем запросе введите exit')
        return input('С каким классом работаем? ').upper()

def input_subject():
        return input('Какой предмет? ').lower()

def who_answer():
    return input('Кто будет отвечать? ')

def what_mark():
    while True:
        try:
            mark = input('На какую оценку ответил? ')
            if 0 < int(mark) < 6: return mark
            else: print('Только число от 1 до 5')
        except:
            print('Только число от 1 до 5')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        summa = 0
        for k in journal.get(child):
            summa += k
        print(f'{i}. {child:20} {journal.get(child)} ср. значание: {round(summa/len(journal.get(child)),1)}')
