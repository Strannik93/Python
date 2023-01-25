import view
import model

def start(flag = False):
    while True:
        user_choice = view.main_menu()
        
        match user_choice:
            case '1':
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case '2':
                model.open_phone_book()
                flag = True
                view.load_success()
            case '3':
                model.save_phone_book()
                flag = True
                view.save_success()
            case '4':
                new = list(view.new_contact())
                model.update_phone_book(new)
            case '5':
                change_index, change_type, name = view.edit_contact(len(model.phone_book))
                model.edit_contact_phone_book(change_index,change_type,name)
            case '6':
                deletion_index = view.deletion_contact(len(model.phone_book))
                model.del_contact_phone_book(deletion_index)
            case '7':
                search = view.find_contact()
                result,indexes = model.search_contact(search)
                view.show_contacts(result,indexes)
            case '8':
                if flag == True:
                    check = model.checking_match()
                    if check == False:
                        confirm = view.confirm_save()
                        if confirm == 'yes':
                            model.save_phone_book()
                break