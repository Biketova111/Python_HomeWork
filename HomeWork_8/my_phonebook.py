

print(f'Добро пожаловать в телефонную книгу!\n')
path='phone_book.txt'
my_phonebooke = open(path, 'a', encoding= 'UTF-8')
my_phonebooke.close()



def work_phonebook():
    print('1 - посмотреть контакты')
    print('2 - добавить контакт')
    print('3 - найти контакт')
    print('4 -изменить контакт')
    print('5 -удалить контакт')
    print('6 - завершить работу с телефонной книгой\n')
    action = input((f'Выберите действие которое хотите совершить: '))
    print('')
    if action == '1':
       read_file()
       work_phonebook()
    elif action == '2':
        create_contact()
        work_phonebook()
    elif action == '3':
        contact_search()
        work_phonebook()
    elif action == '4':
        replace_contact ()
        work_phonebook()
    elif action == '6':
        close_file(my_phonebooke)


def read_file():
        with open(path, 'r', encoding= 'UTF-8') as my_file:
            read_file = my_file.readli()
            print('Ваш телефонный справочник пуст' if len(read_file) == 0 else print(read_file))
            
def create_contact():
    with open(path, 'a', encoding= 'UTF-8') as my_file:
        last_name=input('Введите фамилию: ').capitalize()
        first_name=input('Введите имя: ').capitalize()
        patronymic=input('Введите отчество: ').capitalize()
        phone_number=input('Введите номер телефона: ')
        new_contact =': '.join([' '.join([last_name, first_name, patronymic]), phone_number])
        my_file.write(f'{new_contact} \n')
        print('Контакт сохранен')
    

def contact_search():
    with open(path, 'r+', encoding= 'UTF-8') as my_file:
        characteristic = (input('Введите данные для поиска (например: имя или фамилию): '))    
        file = my_file.readlines()
        if len(file)==0:
            print('Ваш телефонный справочник пуст')       
        else:
            check=False
            for line in file:
                if characteristic in line:
                    check=True
                    print(line)
        if check == False:
            print('По вашему запросу ничего не найдено')


def replace_contact ():
    contact = contact_search()
    
    if len(contact) !=0:
        with open(path, "a+", encoding='UTF-8') as my_file:
            old_chracteristic = input("Введите данные которые вы хотите изменить: ")
            new_chracteristic=input("Введите новые данные: ")
            contact = contact.replace(old_chracteristic, new_chracteristic)
            my_file.write()

           
def close_file(file):
    file.close()        

work_phonebook()

