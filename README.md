# pygame_cursor
Script to draw ASCII cursors compatible with pygame.mouse.set_cursor.

### At Start:
    - Choose the WIDTH (number of pixels in a row) and HEIGHT (number of rows).
        Note: These must be divisible by 8 and cannot be larger than 80.

### Clicks (Drawing):
    - Left Click: Paints the highlighted pixel with Black
    - Right Click: Paints the highlighted pixel with White
    - Wheel Click: Erases the highlighted pixel

### Hotkeys:
    - SPACE: Sets the cursor to the current drawing

    - ESC: Resets the cursor to an arrow

    - H: Sets the Hot Spot of the cursor (Dark Red outline)

    - R: Takes Size input again and resets the canvas
        Note: This will clear the Canvas.

    - F+Click: Fills all the pixels of the same color within an enclosed area with the new color
        Note: This uses a recursive method and has a failsafe of 800 layers (it stops after ~800 painted pixels). For areas larger than 800 pixels you'll need to use it multiple times to cover the entire area.

    - S: Takes Name input and saves the current drawing as a cursor in pygame_cursor_library.py
        Note: This will append a new instance of the Cursor class to the end of the .py file. If you use an existing name, it won't delete the previous with the same name, but will override their instances on import, so it should always load the last cursor of said name.

    - L: Takes Name input and loads the drawing if it exists