import text



def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contact(phone_book: list[dict[str, str]], error: str):
    if phone_book:
        print('\n' + '=' * 71)
        for i, contact in enumerate(phone_book, 1):
            print(f'{i:>3}. {contact.get("name"):<20} | {contact.get("phone"):<20} | {contact.get("comment"):<20}')
        print('=' * 71 + '\n')    
    else:
        print_message(error)

def input_contact(message: str, cansel: str) -> dict:
    contact = {}
    print(message)
    for key, value in text.input_contact.items():
        data = input(value)
        if data:
            contact[key] = data
        else: print_message(cansel)
    return contact


def input_index(message: str, pb: list, error: str) -> int:
    print_contact(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index)<len(pb)+1:
            return int(index)
        
def contact_search(message: str) -> str:
    contact = input(message)
    return contact


       


    


