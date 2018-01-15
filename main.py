import os
from selector import questions


def about():
    print('**********************************************************\n'
          '** Program ma za zadanie wybrać konsolę retro według\n'
          '** na podstawie wyborów z zadanych pytań.\n'
          '**\n'
          '** Pytania o generację oraz rodzaj konsoli odrzucają\n'
          '** niepasujący do wyboru sprzęt.\n'
          '**\n'
          '** Jeżeli podany budżet nie będzie za niski, to zostanie\n'
          '** zarekomendowana konsola zgodna z wyborami.\n'
          '**********************************************************')
    input('                                           Kliknij [Enter]')


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
        '2': about,
        '0': exit_confirmation
    }

    choice = input("            Wybór: ")
    if not choice.isdigit() or int(choice) not in range(0, 3):
        menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    action[choice]()


while True:
    menu()
