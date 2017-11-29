import os


def default_function():
    print('Chyba Cię coś pokiełbasiło. Ten skrypt to samo menu!')
    input('\n                 O gówno, ja przepraszam. Kliknij [Enter]')


def menu_function():
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

    choice = input("Wybór: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == '1':
        default_function()
    elif choice == '2':
        default_function()
    elif choice == '0':
        print('Czy na pewno chcesz zakończyć program?')
        print('(1) Tak')
        print('(0) Nie')
        exit_choice = input("Wybór: ")
        if exit_choice == '1':
            print('Do zobaczenia wkrótce!')
            exit(0)


while True:
    menu_function()
