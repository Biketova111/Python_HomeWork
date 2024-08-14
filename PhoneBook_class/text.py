main_menu = '''\nГлавное меню:
1. Открыть файл
2. Записать файл
3. Показать контакт
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта!'

load_error = 'Телефонная книга пуста или не открыта'

input_contact = {'name': 'Введите имя: ', 
                 'phone':'Введите телефон: ', 
                 'comment':'Введите комментарий: '}

new_contact = 'Введите данные нового контакта (пустое поле для отмены): '

def new_contact_successful(name: str) -> str:
    return f'Котакт {name} успешно добавлен!'


cansel_input = 'Отмена ввода'

save_pb_successful = 'Телефонная книга сохранена!'

index_del_contact = 'Введите индекс контакта, который хотите удалить: '

def del_contact(name: str):
    return f'Контакт {name} успешно удален!'

contact_search_name = 'Введите искомый контакт: '

search_error = 'Контакт не найден!'

change_contact_index = 'Введите индекс контакта, который хотите изменить: '

new_contact_change = 'Введите данные измененного контакта (пустое поле для отмены): '

def change_contact(old_name: str, new_name: str):
    return f'Контакт {old_name} успешно заменен на {new_name}'