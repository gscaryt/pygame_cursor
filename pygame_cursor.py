import pygame

ZOOM = 10

class Canvas:
    def __init__(self, COLS, ROWS):
        self.COLS = COLS
        self.ROWS = ROWS
        self.WIDTH = COLS*ZOOM
        self.HEIGHT = ROWS*ZOOM
        self.rect = pygame.rect.Rect(0,0,self.WIDTH,self.HEIGHT)
        self.GRID = []
        self.HOT_SPOT = (self.COLS//2, self.ROWS//2)
        self.CORNER = (0,0)
        for j in range(ROWS):
            self.GRID.append([])
            for _ in range(COLS):
                self.GRID[j].append(0)

    def show_canvas(self, WINDOW):
        self.rect.center = (WINDOW.get_width()//2, WINDOW.get_height()//2)
        self.CORNER = (WINDOW.get_width()/2-self.WIDTH/2, WINDOW.get_height()/2-self.HEIGHT/2)
        pygame.draw.rect(WINDOW, pygame.Color(100,100,100), self.rect)

    def show_grid(self, WINDOW):
        for i in range(self.COLS):
            for j in range(self.ROWS):
                x = round(self.CORNER[0] + i*ZOOM)
                y = round(self.CORNER[1] + j*ZOOM)
                SQUARE = pygame.rect.Rect(x,y,ZOOM,ZOOM)
                if self.HOT_SPOT == (i, j):
                    pygame.draw.rect(WINDOW, pygame.Color(120,0,0), SQUARE, 1)
                else:
                    pygame.draw.rect(WINDOW, pygame.Color(120,120,120), SQUARE, 1)

    def show_drawing(self, WINDOW):
        for i in range(self.COLS):
            for j in range(self.ROWS):
                x = round(self.CORNER[0] + i*ZOOM)
                y = round(self.CORNER[1] + j*ZOOM)
                SQUARE = pygame.rect.Rect(x,y,ZOOM,ZOOM)
                if self.get_square_state(i, j) == 1:
                    pygame.draw.rect(WINDOW, pygame.Color(0,0,0), SQUARE)
                elif self.get_square_state(i, j) == -1:
                    pygame.draw.rect(WINDOW, pygame.Color(255,255,255), SQUARE)

    def get_square(self):
        mouse = pygame.mouse.get_pos()
        for col in range(self.COLS):
            for row in range(self.ROWS):
                if (
                    self.CORNER[0] + col*ZOOM < mouse[0] <= self.CORNER[0] + (col+1)*ZOOM and
                    self.CORNER[1] + row*ZOOM < mouse[1] <= self.CORNER[1] + (row+1)*ZOOM
                ):
                    return (col,row)
        else:
            return False

    def highlight(self, WINDOW):
        hover = self.get_square()
        if hover:
            x = self.CORNER[0] + hover[0]*ZOOM
            y = self.CORNER[1] + hover[1]*ZOOM
            SQUARE = pygame.rect.Rect(x,y,ZOOM,ZOOM)
            pygame.draw.rect(WINDOW, pygame.Color(180,180,180), SQUARE)

    def get_square_state(self, col, row):
        return self.GRID[row][col]

    def draw(self):
        click = pygame.mouse.get_pressed()
        if self.get_square():
            col, row = self.get_square()
            if click == (1,0,0):
                self.GRID[row][col] = 1
            elif click == (0,0,1):
                self.GRID[row][col] = -1
            elif click == (0,1,0):
                self.GRID[row][col] = 0

    def set_cursor(self, cursor=1):
        if cursor == 0:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor((self.COLS, self.ROWS), self.HOT_SPOT, *pygame.cursors.compile(self.get_cursor()))
        
    def def_hotspot(self):
        if self.get_square():
            col, row = self.get_square()
            self.HOT_SPOT = (col, row)
            return self.HOT_SPOT

    def get_cursor(self):
        cursor = []
        line = ''
        for j in range(self.ROWS):
            for i in range(self.COLS):
                if self.get_square_state(i,j) == 1:
                    line = line+"X"
                elif self.get_square_state(i,j) == -1:
                    line = line+"."
                else:
                    line = line+" "
            cursor.append(line)
            line = ''
        return tuple(cursor)

    def save_cursor(self, name):
        cursor = self.get_cursor()
        name = str(name).lower()
        with open("cursor_lib.py", "a+") as filename:
            filename.write("# START OF CURSOR FUNCTION: " + name + "\n")
            filename.write("def set_cursor_"+name+"():\n")
            filename.write("    # Cursor: " + name +"\n") 
            filename.write("    # Size: " + str((self.COLS, self.ROWS)) + "\n")
            filename.write("    # Hot Spot: " + str(self.HOT_SPOT) + "\n")
            filename.write("    cursor_" + name + " = (\n")
            for line in cursor:
                filename.write("        '" + str(line) + "',\n")
            filename.write("    )\n")
            filename.write("    return pygame.mouse.set_cursor(" + str((self.COLS, self.ROWS)) + ',' + str(self.HOT_SPOT) + ',' + '*pygame.cursors.compile(cursor_' + name + '))\n')
            filename.write("# END OF CURSOR FUNCTION: " + name + "\n\n")

def input_size():
    _valid = False
    while not _valid:
        COLS = input("What WIDTH (columns) your cursor will have? (Must be divisible by 8)")
        if COLS.isdecimal():
            COLS = int(COLS)
            if COLS == 0:
                print("You cannot have a cursor with 0 WIDTH (columns).")
            elif COLS%8 != 0:
                print("WIDTH (columns) must be divisible by 8. (Note: Pygame requirement)")
            elif COLS > 80:
                print("WIDTH (columns) must be less than 81.") 
            else:
                _valid = True # Probably
        else:
            print("You must give an integer number of columns (WIDTH).")
    _valid = False
    while not _valid:
        ROWS = input("What HEIGHT (rows) your cursor will have? (Must be divisible by 8)")
        if ROWS.isdecimal():
            ROWS = int(ROWS)
            if ROWS == 0:
                print("You cannot have a cursor with 0 HEIGHT (rows).")
            elif ROWS%8 != 0:
                print("HEIGHT (rows) must be divisible by 8. (Note: Pygame requirement)")
            elif COLS > 80:
                print("HEIGHT (rows) must be less than 81.") 
            else:
                _valid = True # Probably
        else:
            print("You must give an integer number of rows (HEIGHT).")
    return COLS, ROWS

def main():
    global ZOOM
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    COLS, ROWS = input_size()
    ZOOM = max(10 - int(ROWS//20), 1)
    pygame.display.set_caption("Pygame Cursor Drawing")
    WINDOW = pygame.display.set_mode((COLS*ZOOM + ZOOM*10, ROWS*ZOOM + ZOOM*10))
    
    CANVAS = Canvas(COLS, ROWS)

    while run:
        clock.tick(60)
        WINDOW.fill((50,50,50))
        CANVAS.show_canvas(WINDOW)
        CANVAS.show_drawing(WINDOW)
        CANVAS.show_grid(WINDOW)
        CANVAS.highlight(WINDOW)
        for event in pygame.event.get():
            click = pygame.mouse.get_pressed()
            if click:
                CANVAS.draw()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CANVAS.set_cursor()
                if event.key == pygame.K_ESCAPE:
                    CANVAS.set_cursor(0)
                if event.key == pygame.K_h:
                    CANVAS.def_hotspot()
            if event.type == pygame.QUIT:
                CANVAS.save_cursor("TESTING")
                run = False

        pygame.display.update()

if __name__ == "__main__":
    main()
