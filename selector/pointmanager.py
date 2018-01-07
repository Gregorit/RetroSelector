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

        self.prices = {}

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
