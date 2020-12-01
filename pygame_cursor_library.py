# Made by G. 'Scary' T. (2020)

import pygame

class Cursor:
    library = {}

    def __init__(self, name, size, hot_spot, cursor):
        self.name = name
        self.size = size
        self.hot_spot = hot_spot
        self.cursor = cursor
        if self.name in Cursor.library.keys():
            Cursor.library.pop(self.name, None)
        Cursor.library[self.name] = self

    def set_cursor():
        pygame.mouse.set_cursor(self.size,self.hot_spot,*pygame.cursors.compile(self.cursor))


eye = Cursor(
    'eye',
    (32,24),
    (15,11),
    (    
    "                                ",
    "                                ",
    "             XXXXX              ",
    "           XXXXXXXXX            ",
    "         XXXX.....XXXX          ",
    "       XXXX.........XXXX        ",
    "      XXX.....XXX.....XXX       ",
    "     XXX....XXXXXXX....XXX      ",
    "    XXX....XXXXXX.XX....XXX     ",
    "   XXX....XXXXXX...XX....XXX    ",
    "  XXX....XXXXXXX...XXX....XXX   ",
    " XXX.....XXXXXXXX..XXX.....XXX  ",
    "XXX......XXXXXXXXX.XXX......XXX ",
    " XXX.....XXXXXXXXXXXXX.....XXX  ",
    "  XXX.....XXXXXXXXXXX.....XXX   ",
    "   XXX.....XXXXXXXXX.....XXX    ",
    "    XXX.....XXXXXXX.....XXX     ",
    "     XXX......XXX......XXX      ",
    "      XXXX...........XXXX       ",
    "        XXXX.......XXXX         ",
    "          XXXXXXXXXXX           ",
    "            XXXXXXX             ",
    "                                ",
    "                                ",
    )
)

transparenteye = Cursor(
    'transparent_eye',
    (32, 24),
    (15, 11),
    (
        '                                ',
        '                                ',
        '             XXXXX              ',
        '           XXXXXXXXX            ',
        '         XXXX.....XXXX          ',
        '       XXXX.........XXXX        ',
        '      XXX.....XXX.....XXX       ',
        '     XXX....XXXXXXX....XXX      ',
        '    XXX....XXX   XXX....XXX     ',
        '   XXX....XX   XX  XX....XXX    ',
        '  XXX....XX   XXXX  XX....XXX   ',
        ' XXX.....XX     XXX XX.....XXX  ',
        'XXX......XX      XX XX......XXX ',
        ' XXX.....XX      X  XX.....XXX  ',
        '  XXX.....XX       XX.....XXX   ',
        '   XXX.....XX     XX.....XXX    ',
        '    XXX.....XXXXXXX.....XXX     ',
        '     XXX......XXX......XXX      ',
        '      XXXX...........XXXX       ',
        '        XXXX.......XXXX         ',
        '          XXXXXXXXXXX           ',
        '            XXXXXXX             ',
        '                                ',
        '                                ',
    )
)

uglyrabbit = Cursor(
    'ugly_rabbit',
    (24,16),
    (0,6),
    (
        '        XXX             ',
        '      XX..X         XX  ',
        '  XXXX...X         X..X ',
        ' X.....XX  XXXXXX X...X ',
        'X..X...X XX......XX..X  ',
        'X.......X.........XXX   ',
        ' X..................X   ',
        '  XXXX..............X   ',
        '     XX.............X   ',
        '     XXX..........XXX   ',
        '     X.X..XXXXXX..X.X   ',
        '     X.XX.X    X.XX.X   ',
        '     XX XXX    XX XXX   ',
        '                        ',
        '                        ',
        '                        ',
    )
)

magnify = Cursor(
    'magnify',
    (24, 16),
    (7, 5),
    (
        '     XXXXXX             ',
        '    XXXXXXXX            ',
        '   XX      XX           ',
        '  XX   ...  XX          ',
        '  XX  ..... XX          ',
        '  XX     .. XX          ',
        '  XX        XX          ',
        '  XX        XXX         ',
        '   XX      XX.XX        ',
        '    XXXXXXXX...XX       ',
        '     XXXXXXXX...XX      ',
        '            XX...XX     ',
        '             XX...XX    ',
        '              XX...X    ',
        '                XXX     ',
        '                        ',
    )
)

