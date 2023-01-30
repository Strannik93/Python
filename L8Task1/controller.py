import view
import model


def start():
    while True:
        while True:
            try:
                model.set_class(view.input_class())
                model.set_subject(view.input_subject())
                if model.get_check_exit() == True:
                    break
                model.open_file()
                if len(model.get_journal()) != 0:
                    break
                else: view.error_found(False)
            except:
                view.error_found()
        if model.get_check_exit() == True:
            break
        student = ''
        while True:
            journal = model.get_journal()
            view.list_of_child(journal)
            temp = False
            while temp == False:
                student,temp = model.get_answer(view.who_answer())
                if temp == False: view.not_in_list()
            if student == 'exit':
                break
            mark = int(view.what_mark())
            model.student_mark(student, mark)
        model.save_file()
        if view.get_check() == False:
            break