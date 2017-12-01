import os
from selector import questions


def fancy_function():
    print('Chyba Cię coś pokiełbasiło. Ten skrypt to samo menu!')
    input('\n                 O gówno, ja przepraszam. Kliknij [Enter]')


def exit_confirmation():
    print('Czy na pewno chcesz zakończyć program?')
    print('(1) Tak')
    print('(0) Nie')
    exit_choice = input("Wybór: ")
    if exit_choice == '1':
        print('Do zobaczenia wkrótce!')
        exit(0)


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # czyszczenie międzyplatformowe konsoli/terminala
    print('         *******************')
    print('         ** RetroSelector **         ')
    print('*************************************')
    print('** Autorzy:     Grzegorz Urych     **')
    print('**            Grzegorz Zakrzewski  **')
    print('*************************************')
    print('\n    ****************************')
    print('    **          MENU          **')
    print('    ****************************')
    print('    ** (1) Rozpocznij program **')
    print('    ** (2) O programie        **')
    print('    ****************************')
    print('    ** (0) Zakończ program    **')
    print('    ****************************')

    action = {
        '1': questions,
        '2': fancy_function,
        '0': exit_confirmation
    }

    choice = input("Wybór: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    action[choice]()


while True:
    menu()
