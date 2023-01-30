journal = {}
subject = ''
path = ''
check_exit = False

def set_class(class_path: str):
    global path
    global check_exit
    if class_path == 'EXIT':
        check_exit = True
    path = 'Classes/' + class_path + '.txt'
    

def set_subject(our_subject: str):
    global subject
    global check_exit
    if our_subject == 'exit':
        check_exit = True
    subject = our_subject

def get_answer(answer: str):
    check = False
    for key in journal.keys():
        if key == answer: check = True
    if check == False and answer == 'exit': check = True
    return answer,check

def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks

def get_journal():
    return journal

def get_check_exit():
    return check_exit