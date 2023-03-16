import json
from colorama import Fore, Style

book = {}
BOOK = 'book.json'


def write_in(your_book):
    with open(BOOK, 'w', encoding="UTF-8") as some_file:
        some_content = json.dumps(your_book)
        some_file.write(some_content)
    print('\n', "Changes is saved. What do you want to do next? ")
    phone_book(book)


def read_out():
    with open(BOOK, 'r', encoding="UTF-8") as some_file:
        some_content = some_file.read()
        book = json.loads(some_content)
    return book


def phone_book(book):
    print('\n', f"{'CHOOSE THE ACTION': ^30}", '\n', f"{'MENU BAR': ^30}", '\n', '#' * 33, '\n',
          Fore.GREEN + Style.BRIGHT + 'Press 1 to open the phone book', '\n',
          'Press 2 to save the file', '\n',
          'Press 3 to search the contact information', '\n',
          'Press 4 to add a contact', '\n',
          'Press 5 to delete a contact', '\n',
          'Press 6 to modify a contact data', '\n',
          'Press 7 to exit',
          Style.RESET_ALL + " ")

    choice = input("Enter your choice ")

    if choice == str(1):
        book = read_out()
        for key in book:
            for i in range(len(book[key])):
                print(f'{book[key][i]:^20}', end='')
            print()
        print('\n', "The book is opened. What do you want to do next? ")
        phone_book(book)

    if choice == str(2): write_in(book)

    if choice == str(3):
        data_to_search = input("Enter name or number or special info of the contact: ")
        for key in book:
            if data_to_search in book[key]:
                print()
                for i in range(len(book[key])):
                    print(f'{book[key][i]:^20}', end='')
                print()
        print('\n', "Info is found. What do you want to do next? ")
        phone_book(book)

    if choice == str(4):
        new_name = input("Enter the name of the new contact ")
        new_number = input("Enter the number of the new contact ")
        new_info = input("Enter the info about the new contact ")
        new_list = [new_name] + [new_number] + [new_info]
        book[new_name] = new_list
        answer = input("Do you want to save changes? (y/n) ")
        if answer == 'y':
            print('\n', f"New contact '{new_name}' is added. What do you want to do next? ")
            write_in(book)
        elif answer == 'n':
            phone_book(book)

    if choice == str(5):
        contact_to_delete = input("Enter the name of the contact to delete ")
        if contact_to_delete in book.keys():
            answer = input(f"Do you really want to delete contact {contact_to_delete}? (y/n) ")
            if answer == 'y':
                del book[contact_to_delete]
                print(f"Contact '{contact_to_delete}' have been deleted.  "
                      f"What do you want to do next?")
                write_in(book)
            elif answer == 'n':
                print(f"Contact '{contact_to_delete}' have not been deleted.  What do you want to do next?")
                phone_book(book)
        else:
            print(f"There is now contact '{contact_to_delete}' in your phone book")
            phone_book(book)

    if choice == str(6):
        contact_to_modify = input("What contact info do you want to modify? ")
        if contact_to_modify in book.keys():
            attribute = input("What attribute do you want to modify: name, num, info? ")
            if attribute == 'name':
                new_attribute_name = input("Enter new name of the contact ")
                book[contact_to_modify][0] = new_attribute_name
            elif attribute == 'num':
                new_attribute_num = input("Enter new number of the contact ")
                book[contact_to_modify][1] = new_attribute_num
            elif attribute == 'info':
                new_info = input("Enter new info of the contact ")
                book[contact_to_modify][0] = new_info
            write_in(book)
            print('\n', f"New contact {contact_to_modify} is modified. What do you want to do next? ")
            phone_book(book)

        if contact_to_modify not in book.keys():
            print('\n', f"There is no contact {contact_to_modify} in phone book. What do you want to do next? ")
            phone_book(book)

    if choice == str(7):
        answer = input("Do you want to leave? (y/n) ")
        if answer == 'y':
            return -1
        phone_book(book)


phone_book(read_out())
