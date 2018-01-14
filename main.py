import os
from selector import questions


def fancy_function():
    print('Chyba Cię coś pokiełbasiło. Opis jest jeszcze nie gotowy!')
    input('\n                 O gówno, ja przepraszam. Kliknij [Enter]')


def exit_confirmation():
    print('*******************************************\n'
          '** Czy na pewno chcesz zakończyć program?\n'
          '*******************************************\n'
          '** (1) Tak\n'
          '** (0) Nie\n'
          '*******************************************')
    exit_choice = input("Wybór: ")
    if exit_choice == '1':
        print('Do zobaczenia wkrótce!')
        exit(0)
    elif exit_choice == '0':
        menu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit_confirmation()


def menu():
    # czyszczenie międzyplatformowe konsoli/terminala
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*************************************\n'
          '**          RetroSelector          **\n'
          '*************************************\n'
          '** Autorzy:     Grzegorz Urych     **\n'
          '**            Grzegorz Zakrzewski  **\n'
          '*************************************\n\n'
          '    ****************************\n'
          '    **          MENU          **\n'
          '    ****************************\n'
          '    ** (1) Rozpocznij program **\n'
          '    ** (2) O programie        **\n'
          '    ****************************\n'
          '    ** (0) Zakończ program    **\n'
          '    ****************************')

    action = {
        '1': questions,
        '2': fancy_function,
        '0': exit_confirmation
    }

    choice = input("            Wybór: ")
    if not choice.isdigit() or int(choice) not in range(0, 3):
        menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    action[choice]()


while True:
    menu()
