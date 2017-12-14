'''
To będzie plik do wykonywania ciągu pytań i naliczania punktów
'''

from .pointmanager import ConsoleContainer
import os

points = ConsoleContainer()


def questions():
    generation_question()


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

    '''
    przyklad dodawania punktow do konsol,
    tylko propozycja :)
    '''
    if choice is 1:
        points.add('NES', 2)
    elif choice is 2:
        points.add('SNES', 2)

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

    if gen_choice is '1':
        graphic_dim_question()
    else:
        console_type_question()


def console_type_question():
    print('***')
    print('Jaki rodzaj konsoli preferujesz?')
    print('(1) stacjonarna')
    print('(2) przenośna')
    print('***')

    choice = choice_and_clear(2)

    action = {
        '1': graphic_dim_question,
        '2': graphic_colors_question,
    }
    action[choice]()


def graphic_dim_question():
    print('***')
    print('Jaki rodzaj grafiki ma mieć twoja konsola?')
    print('(1) 2D')
    print('(2) 3D')
    print('***')

    choice = choice_and_clear(2)
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
