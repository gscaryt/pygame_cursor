# Pygame Cursor Draw

Script to easily draw ASCII cursors compatible with pygame.mouse.set_cursor().

### Features:

- Update the cursor while you draw to see your progress and easy retouches.
- Save your cursor in a python file formated and ready to use.
- Open and edit cursors on the library.
- Fill tool to color a large enclosed area with one click.
- 2 sizes of brush to speed the work.

### Requirements:
- Python 3.8 or higher (untested on older versions)
- Pygame 2.0 or higher

## Instructions:

### At Start:

- Run pygame_cursor_draw.py
- Choose the WIDTH (number of pixels in a row) and HEIGHT (number of rows).
    
    Note: These must be divisible by 8 and cannot be larger than 80.

### Clicks (Drawing):
- Left Click: Paints the highlighted pixel with Black
- Right Click: Paints the highlighted pixel with White
- Wheel Click: Erases the highlighted pixel
- F + any CLICK: Fills all the pixels of the same color as the one clicked within an enclosed area with the new color (based on the mouse button pressed)
    
    Note: This uses a recursive method and has a failsafe of 800 layers (it stops after ~800 painted pixels). For areas larger than 800 pixels you'll need to use it multiple times to cover the entire area.

### Hotkeys:
- SPACE: Sets the cursor to the current drawing
- ESC: Resets the cursor to an arrow
- H: Sets the Hot Spot of the cursor (Dark Red outline)
- R: Takes Size input again and resets the canvas
    
    Note: This will clear the Canvas.
- G: Shows or Hides the grid
- 1: Set the size of the brush to 1 pixel (Default)
- 2: Set the size of the brush to a 3x3 cross
- S: Takes Name input and saves the current drawing as a cursor in pygame_cursor_library.py
    
    Note: This will append a new instance of the Cursor class to the end of the .py file. If you use an existing name, it won't delete the previous with the same name, but will override their instances on import, so it should always load the last cursor of said name.
- I: Returns the Names of the cursors in the library dictionary.

    Note: If the library contains more than one cursor with the same Name, the dictionary will only contain the last instance of it.
- L: Takes Name input and loads the drawing if it exists
- Q: Quits the application

## ADDING THE CURSOR TO YOUR GAME

The cursor is saved in the file pygame_cursor_library.py. There are two simple ways of using your cursor:

- Import:

    import pygame_cursor_library as pclib # Must be in the same folder of your game, or add the proper path before the module name.
    
    pclib.Cursor.library['name'].set_cursor()

- Copy and Paste: 

    Just copy and paste the created tuples (size, hot_spot, cursor) onto your code and set the cursor with:
    
    pygame.mouse.set_cursor(SIZE_TUPLE,HOT_SPOT_TUPLE,*pygame.cursors.compile(CURSOR_TUPLE))
