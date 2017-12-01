'''
To będzie plik do wykonywania ciągu pytań i naliczania punktów
'''

from .pointmanager import ConsoleContainer


def questions():
    points = ConsoleContainer()
    points.add('NES', 2)
    points.show('NES')
    input(points.max_points_console())
