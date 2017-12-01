class ConsoleContainer:
    '''
    Klasa przechowująca konsole. Pozwala na zbieranie punktow
    i następnie okresla konsolę, ktora zdobyla ich najwiecej.
    '''
    def __init__(self):
        self.consoles = [
            'Atari_7800', 'NES', 'Master_System', 'Neo_Geo', 'TurboGrafx_16',
            'SNES', 'Mega_Drive', 'Game_Boy', 'Sega_Game_Gear', 'Atari_Lynx',
            'Nintendo_64', 'Atari_Jaguar', 'Sega_Saturn', '3DO', 'Playstation',
            'Neo-Geo_Pocket', 'WonderSwan', 'Virtual_Boy', 'Game_Boy_Color',
            'Dreamcast', 'GameCube', 'Playstation_2', 'Xbox',
            'Game_Boy_Advance', 'N-Gage', 'Neo-Geo_Pocket_Color']

        # dict of console and current number of points "console: points"
        self.console_points = {}

        # initialize console points dictionary with zeros
        for console in self.consoles:
            self.console_points.update({console: 0})

    # adds given amount of points to specified console. Throws exceptions
    # if arguments are invalid.
    def add(self, console, points):
        if console not in self.consoles:
            raise ValueError(console + ' not found in console storage.')
        elif not isinstance(points, int):
            raise TypeError(points + ' is not a digit number.')
        else:
            current_points = self.console_points[console]
            self.console_points[console] = current_points + points

    # prints amount of points for given console name.
    def show(self, console):
        if console not in self.consoles:
            raise ValueError(console + ' not found in console storage.')
        else:
            current_points = self.console_points[console]
            print(console + ' has ' + str(current_points) + ' points.')

    # returns name of console with maximum amount of points collected.
    def max_points_console(self):
        max_console = max(self.console_points, key=self.console_points.get)
        return max_console
