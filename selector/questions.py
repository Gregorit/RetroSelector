'''
To będzie plik do wykonywania ciągu pytań i naliczania punktów
'''

import os
import random
from .pointmanager import ConsoleContainer

manage = ConsoleContainer()


def questions():
    generation_question()
    print('Najlepszym wyborem dla Ciebie jest {}.'
          .format(manage.max_points_console()))
    input('\n                  Kliknij [Enter]')


def choice_and_clear(answers_number):
    choice = input('Wybór: ')

    if (not choice.isdigit()) or int(choice) > answers_number or int(choice) < 1:
        print('Podano nieprawidłową odpowiedź.')
        print('Wpisz ją jeszcze raz')
        choice_and_clear(answers_number)

    os.system('cls' if os.name == 'nt' else 'clear')
    return choice


def generation_question():
    print('***')
    print('Czy celujesz w konkretną generację konsol?')
    print('(1) III generacja')
    print('(2) IV generacja')
    print('(3) V generacja')
    print('(4) VI generacja')
    print('(5) nie mam konkretnej')
    print('***')

    choice = choice_and_clear(5)

    if choice is '1':
        manage.flag_by_gen(manage.gen4 + manage.gen5 + manage.gen6)
    elif choice is '2':
        manage.flag_by_gen(manage.gen3 + manage.gen5 + manage.gen6)
    elif choice is '3':
        manage.flag_by_gen(manage.gen3 + manage.gen4 + manage.gen6)
    elif choice is '4':
        manage.flag_by_gen(manage.gen3 + manage.gen4 + manage.gen5)

    game_genre_question(choice)


def game_genre_question(gen_choice):
    print('***')
    print('Jaki gatunek gier preferujesz najbardziej?')
    print('(1) gry akcji')
    print('(2) przygodowe')
    print('(3) platformówki')
    print('(4) symulacyjne')
    print('(5) RPG')
    print('(6) beat\'em up')
    print('(7) strzelanki')
    print('(8) strategie')
    print('(9) shoot\'em up')
    print('(10) strzelanki na szynach')
    print('(11) run & gun')
    print('(12) wyścigowe')
    print('(13) imprezowe')
    print('(14) rytmiczne')
    print('(15) puzzle')
    print('(16) sportowe')
    print('(17) bez znaczenia')
    print('***')

    choice = choice_and_clear(17)

    if choice is '1':
        manage.add_points('NES', 2)
    elif choice is '2':
        manage.add_points('SNES', 2)
    elif choice is '3':
        manage.add_points('SNES', 2)
    elif choice is '4':
        manage.add_points('SNES', 2)
    elif choice is '5':
        manage.add_points('SNES', 2)
    elif choice is '6':
        manage.add_points('SNES', 2)
    elif choice is '7':
        manage.add_points('SNES', 2)
    elif choice is '8':
        manage.add_points('SNES', 2)
    elif choice is '9':
        manage.add_points('SNES', 2)
    elif choice is '10':
        manage.add_points('SNES', 2)
    elif choice is '11':
        manage.add_points('SNES', 2)
    elif choice is '12':
        manage.add_points('SNES', 2)
    elif choice is '13':
        manage.add_points('SNES', 2)
    elif choice is '14':
        manage.add_points('SNES', 2)
    elif choice is '15':
        manage.add_points('SNES', 2)
    elif choice is '16':
        manage.add_points('SNES', 2)

    if gen_choice is '1':
        storage_question()
    else:
        console_type_question(gen_choice)


def console_type_question(gen_choice):
    print('***')
    print('Jaki rodzaj konsoli preferujesz?')
    print('(1) stacjonarna')
    print('(2) przenośna')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        manage.flag_by_type(manage.portable)
        if gen_choice is '5':
            graphic_dim_question()
        else:
            storage_question()
    elif choice is '2':
        manage.flag_by_type(manage.stationary)
        graphic_colors_question()


def graphic_dim_question():
    print('***')
    print('Jaki rodzaj grafiki ma wspierać twoja konsola?')
    print('(1) 2D')
    print('(2) 3D')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        manage.add_points('7800', 2)
        manage.add_points('Master_System', 2)
        manage.add_points('NES', 2)
        manage.add_points('Mega_Drive', 2)
        manage.add_points('Neo_Geo', 2)
        manage.add_points('SNES', 2)
        manage.add_points('TurboGrafx_16', 2)

    elif choice is '2':
        manage.add_points('3DO', 2)
        manage.add_points('Jaguar', 2)
        manage.add_points('N64', 2)
        manage.add_points('PlayStation', 2)
        manage.add_points('Saturn', 2)
        manage.add_points('Dreamcast', 2)
        manage.add_points('GameCube', 2)
        manage.add_points('PlayStation_2', 2)
        manage.add_points('Xbox', 2)

    storage_question()


def storage_question():
    print('***')
    print('Jaki rodzaj nośnika preferujesz w konsoli?')
    print('(1) kartridż')
    print('(2) płyta CD/DVD')
    print('***')

    choice = choice_and_clear(2)

    stationary_multi_question()


def stationary_multi_question():
    print('***')
    print('Do ilu maksymalnie graczy przewidujesz')
    print('grę lokalną na podzielonym ekranie?')
    print('(1) 2')
    print('(2) 4')
    print('(3) nie przewiduję')
    print('***')

    choice = choice_and_clear(3)

    online_multi_question()


def online_multi_question():
    print('***')
    print('Czy przewidujesz grę po sieci jeśli')
    print('jest to możliwe?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    exclusive_games_question()


def graphic_colors_question():
    print('***')
    print('Jaki rodzaj grafiki ma mieć twoja konsola?')
    print('(1) odcienie szarości')
    print('(2) kolor')
    print('***')

    choice = choice_and_clear(2)

    battery_time_question()


def battery_time_question():
    print('***')
    print('Jaki czas pracy na baterii jest dla ciebie optymalny?')
    print('(1) 3-8 godzin')
    print('(2) 8-15 godzin')
    print('(3) 15 i więcej godzin')
    print('***')

    choice = choice_and_clear(3)

    battery_type_question()


def battery_type_question():
    print('***')
    print('Baterie czy wbudowany akumulator?')
    print('(1) baterie')
    print('(2) wbudowany akumulator')
    print('***')

    choice = choice_and_clear(2)

    display_backlight_question()


def display_backlight_question():
    print('***')
    print('Czy konsola ma posiadać podświetlenie ekranu?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    local_multi_question()


def local_multi_question():
    print('***')
    print('Do ilu maksymalnie graczy przewidujesz grę lokalną?')
    print('(1) 2')
    print('(2) 4')
    print('(3) nie przewiduję')
    print('***')

    choice = choice_and_clear(3)

    exclusive_games_question()


def exclusive_games_question():
    print('***')
    print('Czy ma znaczenie dla ciebie ilość gier ekskluzywnych?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    games_library_question()


def games_library_question():
    print('***')
    print('Jakiej wielkości biblioteka gier ma być dostępna na sprzęt?')
    print('(1) duża')
    print('(2) średnia')
    print('(3) mała')
    print('(4) bez znaczenia')
    print('***')

    choice = choice_and_clear(4)

    accessories_question()


def accessories_question():
    print('***')
    print('Czy ma dla ciebie znaczenie wsparcie konsoli')
    print('o akcesoria 1st i 3rd party?')
    print('(1) tak')
    print('(2) tak, ale tylko 1st party')
    print('(3) nie')
    print('***')

    choice = choice_and_clear(3)

    popularity_question()


def popularity_question():
    print('***')
    print('Czy upragniony sprzęt ma być popularnym wyborem w latach')
    print('jego świetności?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    removing_flagged_consoles()


def removing_flagged_consoles():
    print(manage.console_flagger)
    print(manage.console_points)
    for key in manage.console_flagger:
        if key in manage.console_points:
            del manage.console_points[key]
    print(manage.console_points)
    budget_question()


def budget_question():
    print('***')
    print('Podaj maksymalny budżet przeznaczony na zakup konsoli.')
    print('***')

    budget = input('Wpisz budżet: ')

    if not budget.isdigit():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Podano nieprawidłową wartość.')
        budget_question()

    # tu pętla sprawdzająca jest więcej niż jedna konsola posiadająca
    # najwięcej punktów
    # należy stworzyć tymczasową listę takich konsol po czym wykonać random
