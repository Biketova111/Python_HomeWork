import view
import model
import text



def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_pb_successful)
            case 3:
                phone_book =model.get_pb()
                view.print_contact(phone_book, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cansel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))

            case 5:
                contact_name = view.contact_search(text.contact_search_name)
                phone_book = model.get_pb()
                name = model.contact_search(contact_name, phone_book)
                view.print_contact(name, text.search_error)

            case 6:
                pb=model.get_pb()
                index = view.input_index(text.change_contact_index, pb, text.load_error)
                old_name = model.del_contact(index)
                new_contact = view.input_contact(text.new_contact_change, text.cansel_input)
                new_name = model.add_contact(new_contact)
                view.print_message(text.change_contact(old_name, new_name))
            case 7:
                pb=model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break
