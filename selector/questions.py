import os
from .pointmanager import ConsoleContainer, json_loader

manage = ConsoleContainer()
data = json_loader()


def questions():
    generation_question()

    best_choice = manage.max_points_console()
    os.system('cls' if os.name == 'nt' else 'clear')

    if best_choice is 'None':
        print("Niestety nie możemy ci zaproponować konsoli. Twój budżet jest za niski.")
    else:
        # printing informations about console using data from json file
        print('Najlepszym wyborem dla Ciebie jest {}.'
              .format(data[best_choice]['name']))
        if best_choice in manage.stationary:
            print('-----------------------------------------')
            print(data[best_choice]['name'])
            print('\n    Producent: {}'
                  '\n    Generacja: {}'
                  '\n    Lata sprzedaży: {}\n'
                  '\n    Rodzaj konsoli: {}'
                  '\n    Grafika: {}'
                  '\n    Porty na kontrolery: {}'
                  '\n    Nośnik: {}\n'
                  '\n    Ilość gier: {}\n'
                  '\n    Aktualna dostępność: {}'
                  '\n    Aktualna cena sprzętu: około {} PLN'
                  '\n    Aktualne ceny gier: około {} PLN\n'
                  '\nInne modele: {}'
                  '\nPrzeczytaj więcej: {}'
                  .format(data[best_choice]['manufacturer'],
                          data[best_choice]['generation'],
                          data[best_choice]['retail_years'],
                          data[best_choice]['type'],
                          data[best_choice]['graphic'],
                          data[best_choice]['ports'],
                          data[best_choice]['media'],
                          data[best_choice]['library_number'],
                          data[best_choice]['rarity'],
                          data[best_choice]['price'],
                          data[best_choice]['games_price'],
                          data[best_choice]['other_models'],
                          data[best_choice]['read_more']))

        elif best_choice in manage.portable:
            print('-----------------------------------------')
            print(data[best_choice]['name'])
            print('\n    Producent: {}'
                  '\n    Generacja: {}'
                  '\n    Lata sprzedaży: {}\n'
                  '\n    Rodzaj konsoli: {}'
                  '\n    Rodzaj ekranu: {}'
                  '\n    Podświetlenie ekranu: {}'
                  '\n    Nośnik: {}'
                  '\n    Czas gry: {}'
                  '\n    Zasilanie: {}\n'
                  '\n    Ilość gier: {}\n'
                  '\n    Aktualna dostępność: {}'
                  '\n    Aktualna cena sprzętu: około {} PLN'
                  '\n    Aktualne ceny gier: około {} PLN\n'
                  '\nInne modele: {}'
                  '\nPrzeczytaj więcej: {}'
                  .format(data[best_choice]['manufacturer'],
                          data[best_choice]['generation'],
                          data[best_choice]['retail_years'],
                          data[best_choice]['type'],
                          data[best_choice]['screen'],
                          data[best_choice]['light'],
                          data[best_choice]['media'],
                          data[best_choice]['playtime'],
                          data[best_choice]['power'],
                          data[best_choice]['library_number'],
                          data[best_choice]['rarity'],
                          data[best_choice]['price'],
                          data[best_choice]['games_price'],
                          data[best_choice]['other_models'],
                          data[best_choice]['read_more']))

    # cleaning and restoration of lists and dictionaries in pointmanager.py
    manage.consoles = manage.stationary + manage.portable
    manage.console_points.clear()
    for console in manage.consoles:
        manage.console_points.update({console: 0})

    input('\n                  Kliknij [Enter]')


def choice_and_clear(answers_number):
    choice = input('Wybór: ')

    if not choice.isdigit() or int(choice) not in range(1, answers_number+1):
        print('Podano nieprawidłową odpowiedź.')
        print('Wpisz ją jeszcze raz')
        choice_and_clear(answers_number)

    os.system('cls' if os.name == 'nt' else 'clear')
    return choice


def generation_question():
    print('***')
    print('Czy celujesz w konkretną generację konsol?')
    print('[UWAGA!: wybierając konkretną generację odrzucasz')
    print('         pozostałe konsole niezgodne z wyborem]')
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


# możliwa redukcja opcji, poprzez brak którejś kategorii uważanej za najpopularniejszą
# na danej konsoli
def game_genre_question(gen_choice):
    print('***')
    print('Jaki gatunek gier preferujesz najbardziej?')
    print('(1) gry akcji')
    print('(2) przygodowe')
    print('(3) platformówki')
    print('(4) symulacyjne')
    print('(5) RPG')
    print('(6) strzelanki')
    print('(7) strategie')
    print('(8) wyścigowe')
    print('(9) sportowe')
    print('(10) bez znaczenia')
    print('***')

    choice = choice_and_clear(10)

    # if choice is '1':
    #     manage.add_points('NES', 1)
    # elif choice is '2':
    #     manage.add_points('SNES', 1)
    # [...]

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
        for key in data:
            if key in manage.stationary and \
               data[key]['graphic'] == '2D':
                manage.add_points(key, 3)

    elif choice is '2':
        for key in data:
            if key in manage.stationary and \
               data[key]['graphic'] == '3D':
                manage.add_points(key, 3)

    storage_question()


def storage_question():
    print('***')
    print('Jaki rodzaj nośnika preferujesz w konsoli?')
    print('(1) kartridż')
    print('(2) płyta CD/DVD')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        for key in data:
            if key in manage.stationary and \
              (data[key]['media'] == 'kartridż' or
               data[key]['media'] == 'kartridż/CD'):
                manage.add_points(key, 2)

    elif choice is '2':
        for key in data:
            if key in manage.stationary and \
              (data[key]['media'] == 'kartridż/CD' or
               data[key]['media'] == 'CD' or
               data[key]['media'] == 'DVD' or
               data[key]['media'] == 'miniDVD'):
                manage.add_points(key, 2)

    stationary_ports_question()


# zmiania na pytanie obejmujące ilość portów w konsoli na kontrolery (bez adapterów)
def stationary_ports_question():
    print('***')
    print('Ile portów na kontrolery powinna posiadać\n'
          'konsola? (adaptery nie są brane pod uwagę)')
    print('(1) 1')
    print('(2) 2')
    print('(3) 4')
    print('***')

    choice = choice_and_clear(3)

    if choice is '1':
        for key in data:
            if key in manage.stationary and \
               data[key]['ports'] == '1':
                manage.add_points(key, 1)

    elif choice is '2':
        for key in data:
            if key in manage.stationary and \
               data[key]['ports'] == '2':
                manage.add_points(key, 1)

    elif choice is '3':
        for key in data:
            if key in manage.stationary and \
               data[key]['ports'] == '3':
                manage.add_points(key, 1)

    online_multi_question()


def online_multi_question():
    print('***')
    print('Czy przewidujesz grę po sieci jeśli')
    print('jest to możliwe?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        for key in data:
            if key in manage.stationary and \
               data[key]['online'] == 'active':
                manage.add_points(key, 1)

    games_library_question()


def graphic_colors_question():
    print('***')
    print('Jaki rodzaj grafiki ma mieć twoja konsola?')
    print('(1) odcienie szarości/monochromatyczny')
    print('(2) kolor')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        for key in data:
            if key in manage.portable and \
              (data[key]['screen'] == 'monochromatyczny/kolorowy' or
               data[key]['screen'] == 'monochromatyczny'):
                manage.add_points(key, 3)

    elif choice is '2':
        for key in data:
            if key in manage.portable and \
              (data[key]['screen'] == 'monochromatyczny/kolorowy' or
               data[key]['screen'] == 'kolorowy'):
                manage.add_points(key, 3)

    battery_time_question()


def battery_time_question():
    print('***')
    print('Jaki czas pracy na baterii jest dla ciebie optymalny?')
    print('(1) 2-8 godzin')
    print('(2) 8 i więcej godzin')
    print('(3) bez znaczenia')
    print('***')

    choice = choice_and_clear(3)

    if choice is '1':
        for key in data:
            if key in manage.portable and \
               data[key]['playtime_in_words'] == 'short':
                manage.add_points(key, 2)

    elif choice is '2':
        for key in data:
            if key in manage.portable and \
               data[key]['playtime_in_words'] == 'long':
                manage.add_points(key, 2)

    battery_type_question()


def battery_type_question():
    print('***')
    print('Baterie czy wbudowany akumulator?')
    print('(1) baterie')
    print('(2) wbudowany akumulator')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        for key in data:
            if key in manage.portable and \
              (data[key]['power_type'] == 'battery' or
               data[key]['power_type'] == 'battery/rechargeable'):
                manage.add_points(key, 1)

    elif choice is '2':
        for key in data:
            if key in manage.portable and \
              (data[key]['power_type'] == 'rechargeable' or
               data[key]['power_type'] == 'battery/rechargeable'):
                manage.add_points(key, 1)

    display_backlight_question()


def display_backlight_question():
    print('***')
    print('Czy konsola ma posiadać podświetlenie ekranu?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        for key in data:
            if key in manage.portable and \
              (data[key]['light'] == 'tak' or
               data[key]['light'] == 'zależne od wersji'):
                manage.add_points(key, 2)

    elif choice is '2':
        for key in data:
            if key in manage.portable and \
              (data[key]['light'] == 'nie' or
               data[key]['light'] == 'zależne od wersji'):
                manage.add_points(key, 2)

    local_multi_question()


def local_multi_question():
    print('***')
    print('Czy interesuje ciebie gra lokalna?')
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

    if choice is '1':
        for key in data:
            if int(data[key]['library_number']) >= 700:
                manage.add_points(key, 2)

    elif choice is '2':
        for key in data:
            if int(data[key]['library_number']) in range(250, 700):
                manage.add_points(key, 2)

    elif choice is '3':
        for key in data:
            if int(data[key]['library_number']) in range(0, 250):
                manage.add_points(key, 2)

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

    extra_functions_question()


def extra_functions_question():
    print('***')
    print('Jeżeli konsola pełni dodatkowe funckje (bez dodatkowych')
    print('akcesoriów), np: odtwarzanie muzyki bądź filmów, rozmowy telefoniczne')
    print('to czy byłbyś nimi zainteresowany?')
    print('(1) tak')
    print('(2) nie')
    print('***')

    choice = choice_and_clear(2)

    if choice is '1':
        for key in data:
            if data[key]['extra_functions'] == 'yes':
                manage.add_points(key, 1)

    popularity_question()


def popularity_question():  # DONE
    print('***')
    print('W jakim stopniu upragniony sprzęt ma być')
    print('popularnym wyborem w latach jego świetności?')
    print('(1) najpopularniejszym')
    print('(2) popularnym')
    print('(3) mało popularnym/niszowym')
    print('***')

    choice = choice_and_clear(3)

    if choice is '1':
        for key in data:
            if data[key]['popularity'] == 'most popular':
                manage.multiply_points(key, 1.25)

    elif choice is '2':
        for key in data:
            if data[key]['popularity'] == 'popular':
                manage.multiply_points(key, 1.5)

    elif choice is '3':
        for key in data:
            if data[key]['popularity'] == 'not popular':
                manage.multiply_points(key, 1.75)

    removing_flagged_consoles()


def removing_flagged_consoles():
    for key in manage.console_flagger:
        if key in manage.console_points:
            del manage.console_points[key]
    del manage.console_flagger[:]

    budget_question()


def budget_question():
    print('***')
    print('Podaj maksymalny budżet przeznaczony na zakup konsoli.')
    print('***')

    budget = input('Wpisz budżet: PLN ')

    if not budget.isdigit():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Podano nieprawidłową wartość.')
        budget_question()

    for key in list(manage.console_points.keys()):
        if int(data[key]['price']) > int(budget):
            del manage.console_points[key]

    if not manage.console_points:
        manage.console_points['None'] = None
