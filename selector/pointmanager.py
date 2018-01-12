import json


def json_loader():
    json_file = open('selector/consoles.json', encoding="utf-8")
    json_data = json.load(json_file)
    json_file.close()
    return json_data


class ConsoleContainer:
    '''
    Klasa przechowująca konsole. Pozwala na zbieranie punktow
    i następnie okresla konsolę, ktora zdobyla ich najwiecej.
    '''

    def __init__(self):
        data = json_loader()

        self.gen3 = []
        self.gen4 = []
        self.gen5 = []
        self.gen6 = []
        self.stationary = []
        self.portable = []

        # completion generations and types lists from json data
        for key in data:
            if data[key]['generation'] == 'III generacja':
                self.gen3.append(key)
            elif data[key]['generation'] == 'IV generacja':
                self.gen4.append(key)
            elif data[key]['generation'] == 'V generacja':
                self.gen5.append(key)
            elif data[key]['generation'] == 'VI generacja':
                self.gen6.append(key)

            if data[key]['type'] == 'stacjonarna':
                self.stationary.append(key)
            elif data[key]['type'] == 'przenośna':
                self.portable.append(key)

        self.consoles = self.stationary + self.portable

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
