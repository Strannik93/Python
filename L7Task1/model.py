phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)

def search_contact(search: str):
    global phone_book
    search_results = []
    search_index = []
    for i, line in enumerate(phone_book):
        for field in line:
            if search in field:
                search_results.append(line)
                search_index.append(i)
                break
    return search_results, search_index

def del_contact_phone_book(deletion_index: int):
    global phone_book
    if 0 <= deletion_index < len(phone_book):
        phone_book.pop(deletion_index)

def edit_contact_phone_book(edit_index: int, edit_type: int, name: str):
    global phone_book
    if 0 <= edit_index < len(phone_book):
        match edit_type:
            case 1:
                phone_book[edit_index][0] = name
            case 2:
                phone_book[edit_index][1] = name
            case 3:
                phone_book[edit_index][2] = name

def checking_match():
    global phone_book
    global path
    copy_book = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            copy_book.append(line.strip().split(';'))
    if len(copy_book) == len(phone_book):
        for line in range(len(phone_book)):
            for i in range(len(phone_book[line])):
                if copy_book[line][i] != phone_book[line][i]: return False
    else: return False
    return True