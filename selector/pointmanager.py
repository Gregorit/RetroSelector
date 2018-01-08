class ConsoleContainer:
    '''
    Klasa przechowująca konsole. Pozwala na zbieranie punktow
    i następnie okresla konsolę, ktora zdobyla ich najwiecej.
    '''
    def __init__(self):
        self.gen3 = ['7800', 'Master_System', 'NES']
        self.gen4 = ['Mega_Drive', 'Neo_Geo', 'SNES', 'TurboGrafx_16',
                     'GB', 'Game_Gear', 'Lynx']
        self.gen5 = ['3DO', 'Jaguar', 'N64', 'PlayStation', 'Saturn',
                     'GBC', 'Neo-Geo_Pocket', 'Virtual_Boy', 'WonderSwan']
        self.gen6 = ['Dreamcast', 'GameCube', 'PlayStation_2', 'Xbox',
                     'GBA', 'Neo-Geo_Pocket_Color', 'N-Gage']

        self.stationary = ['7800', 'Master_System', 'NES', 'Mega_Drive',
                           'Neo_Geo', 'SNES', 'TurboGrafx_16', '3DO', 'Jaguar',
                           'N64', 'PlayStation', 'Saturn', 'Dreamcast',
                           'GameCube', 'PlayStation_2', 'Xbox']
        self.portable = ['GB', 'Game_Gear', 'Lynx', 'GBC', 'Neo-Geo_Pocket',
                         'Virtual_Boy', 'WonderSwan', 'GBA',
                         'Neo-Geo_Pocket_Color', 'N-Gage']

        self.consoles = self.stationary + self.portable

        self.prices = {'7800': 480, 'Master_System': 120, 'NES': 320,
                       'Mega_Drive': 175, 'Neo_Geo': 2000, 'SNES': 260,
                       'TurboGrafx_16': 550, '3DO': 730, 'Jaguar': 1430,
                       'N64': 350, 'PlayStation': 140, 'Saturn': 410,
                       'Dreamcast': 460, 'GameCube': 200, 'PlayStation_2': 110,
                       'Xbox': 220, 'GB': 160, 'Game_Gear': 300, 'Lynx': 475,
                       'GBC': 200, 'Neo-Geo_Pocket': 400, 'Virtual_Boy': 1100,
                       'WonderSwan': 235, 'GBA': 170, 'Neo-Geo_Pocket_Color': 440,
                       'N-Gage': 250}

        # dict of console and current number of points "console: points"
        self.console_points = {}

        # list which contains rejected consoles when choosing generation or type
        self.console_flagger = []

        # initialize console points dictionary with zeros
        for console in self.consoles:
            self.console_points.update({console: 0})

    # adds given amount of points to specified console. Throws exceptions
    # if arguments are invalid.
    def add_points(self, console, points):
        if console not in self.consoles:
            raise ValueError('{} not found in console storage.'.format(console))
        elif not isinstance(points, int):
            raise TypeError('{} is not a digit number.'.format(points))
        else:
            current_points = self.console_points[console]
            self.console_points[console] = current_points + points

    def multiply_points(self, console, multiply):
        if console not in self.consoles:
            raise ValueError('{} not found in console storage.'.format(console))
        elif not isinstance(multiply, float):
            raise TypeError('{} is not a digit number.'.format(multiply))
        else:
            current_points = self.console_points[console]
            self.console_points[console] = current_points * multiply

    # prints amount of points for given console name.
    # [TAK NAPRAWDĘ W WERSJI KOŃCOWEJ BĘDZIE ZBĘDNE]
    def show(self, console):
        if console not in self.consoles:
            raise ValueError('{} not found in console storage.'.format(console))
        else:
            current_points = self.console_points[console]
            print('{} has {} points.'.format(console, str(current_points)))

    # returns name of console with maximum amount of points collected.
    def max_points_console(self):
        max_console = max(self.console_points, key=self.console_points.get)
        return max_console

    # flagging mismatched consoles by selecting an answer about console generation
    def flag_by_gen(self, console):
        self.console_flagger += console

    # flagging mismatched consoles by selecting an answer about console type
    def flag_by_type(self, console):
        self.console_flagger = list(set(self.console_flagger + console))
