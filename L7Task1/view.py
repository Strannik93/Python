def main_menu():
    commands = ['Показать все контакты', 'Открыть файл', 'Сохранить файл', 'Новый контакт', 
                'Изменить контакт', 'Удалить контакт', 'Найти контакт', 'Выйти из программы']
    for i, item in enumerate(commands):
        print(i+1, item)
    value = input('\nВыберите пункт меню: ')
    return value
        
def show_contacts(phone_book: list, flag = True):
    if len(phone_book)>0:
        if type(flag) == list:
            i = 0
            for item in phone_book:
                print(f'{flag[i]:3} {item[0]:20} {item[1]:15} {item[2]:15}')
                i += 1
        else:
            for i,item in enumerate(phone_book):
                print(f'{i:3} {item[0]:20} {item[1]:15} {item[2]:15}')
    else:
        if  flag == True: print('Телефонная книга пуста или не загружена')
        else: print('Совпадении в телефонной книге не найдено')

def deletion_contact(line):
    if line > 0:
        while True:
            try:
                search_deletion = int(input('Введите индекс удаляемого контакта: '))
                if 0 <= search_deletion < line: return search_deletion
                else: print('Такого индекса нет')
            except:
                print('Только целое число')
    else:
        print('Телефонная книга пуста')
        return -1

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно')

def new_contact():
    name = input('Введите название контакта: ')
    phone = input('Введите номер контакта: ')
    comment = input('Введите комментарий контакта: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def edit_contact(line):
    if line > 0:
        while True:
            try:    
                change_index = int(input('Введите индекс изменяемого контакта: '))
                if 0 <= change_index < line:
                    change_type = int(input('1 для изменения названия\n2 - номера\n3 - комментария\nВвод: '))
                    if 0 < change_type < 4:
                        new = input('Введите новое значение: ')
                        return change_index, change_type, new
                    else: print('Такого поля в контакте нет')
                else: print('Такого индекса нет')
            except:
                print('Индекс и тип целым числом')
    else:
        print('Телефонная книга пуста')
        return -1, -1, -1

def confirm_save():
    while True:
        confirm = input('Обнаружены изменения\nВведите yes для сохранения: ')
        if confirm.lower() == 'yes':    return confirm.lower()
        else: return confirm