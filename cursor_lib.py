# START OF CURSOR FUNCTION: rabbit
def set_cursor_rabbit():
    # Cursor: rabbit
    # Size: (24, 16)
    # Hot Spot: (0, 6)
    cursor_rabbit = (
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
    return pygame.mouse.set_cursor((24, 16),(0, 6),*pygame.cursors.compile(cursor_rabbit))
# END OF CURSOR FUNCTION: rabbit

