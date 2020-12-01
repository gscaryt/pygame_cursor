import pygame
import pygame_cursor_library as pclib

ZOOM = 10
COLOR_BG = (50,50,50)
COLOR_CANVAS = (150,150,150)
COLOR_GRID = (120,120,120)
COLOR_HOTSPOT = (120,0,0)
COLOR_HIGHLIGHT = (0,200,200)
BLACK = (0,0,0)
WHITE = (255,255,255)

class CursorCanvas:
    def __init__(self, COLS, ROWS):
        self.COLS = COLS
        self.ROWS = ROWS
        self.GRID = []
        self.HOT_SPOT = (self.COLS//2, self.ROWS//2)
        self.CORNER = (0,0)
        self.__recursion_failsafe = 0
        self.build_grid()

    @property
    def WIDTH(self):
        return self.COLS*ZOOM
    
    @property
    def HEIGHT(self):
        return self.ROWS*ZOOM
    
    @property
    def RECT(self):
        return pygame.rect.Rect(0,0,self.WIDTH,self.HEIGHT)

    def build_grid(self):
        for j in range(self.ROWS):
            self.GRID.append([])
            for _ in range(self.COLS):
                self.GRID[j].append(0)

    def show_canvas(self, WINDOW):
        canva_rect = self.RECT
        canva_rect.center = (WINDOW.get_width()//2, WINDOW.get_height()//2)
        self.CORNER = (WINDOW.get_width()/2-self.WIDTH/2, WINDOW.get_height()/2-self.HEIGHT/2)
        pygame.draw.rect(WINDOW, COLOR_CANVAS, canva_rect)

    def show_grid(self, WINDOW):
        for i in range(self.COLS):
            for j in range(self.ROWS):
                x = round(self.CORNER[0] + i*ZOOM)
                y = round(self.CORNER[1] + j*ZOOM)
                SQUARE = pygame.rect.Rect(x,y,ZOOM,ZOOM)
                if self.HOT_SPOT == (i, j):
                    pygame.draw.rect(WINDOW, COLOR_HOTSPOT, SQUARE, 1)
                else:
                    pygame.draw.rect(WINDOW, COLOR_GRID, SQUARE, 1)

    def show_drawing(self, WINDOW):
        for i in range(self.COLS):
            for j in range(self.ROWS):
                x = round(self.CORNER[0] + i*ZOOM)
                y = round(self.CORNER[1] + j*ZOOM)
                SQUARE = pygame.rect.Rect(x,y,ZOOM,ZOOM)
                if self.get_square_state(i, j) == 1:
                    pygame.draw.rect(WINDOW, BLACK, SQUARE)
                elif self.get_square_state(i, j) == -1:
                    pygame.draw.rect(WINDOW, WHITE, SQUARE)

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

    def get_square_state(self, col, row):
        return self.GRID[row][col]

    def highlight(self, WINDOW):
        hover = self.get_square()
        if hover:
            x = self.CORNER[0] + hover[0]*ZOOM
            y = self.CORNER[1] + hover[1]*ZOOM
            SQUARE = pygame.rect.Rect(x,y,ZOOM,ZOOM)
            pygame.draw.rect(WINDOW, COLOR_HIGHLIGHT, SQUARE, 1)

    def draw(self):
        if self.get_square():
            click = pygame.mouse.get_pressed()
            col, row = self.get_square()
            if click == (1,0,0):
                self.GRID[row][col] = 1
            elif click == (0,0,1):
                self.GRID[row][col] = -1
            elif click == (0,1,0):
                self.GRID[row][col] = 0

    def fill(self):
        if self.get_square():
            col, row = self.get_square()
            old_state = self.get_square_state(col, row)
            click = pygame.mouse.get_pressed()
            if click == (1,0,0):
                new_state = 1
            elif click == (0,0,1):
                new_state = -1
            elif click == (0,1,0):
                new_state = 0
            else:
                new_state = None
            if old_state != new_state and new_state is not None:
                self.__fill(col, row, old_state, new_state)
                self.__recursion_failsafe = 0

    def __fill(self, col, row, old_state, new_state):
        '''
        Fill needs a recursion failsafe so it doesn't crash.
        This introduces incomplete filling on big canvas (>32x24).
        Need to find another way of doing it without recursion.
        '''
        self.GRID[row][col] = new_state
        self.__recursion_failsafe += 1
        if self.__recursion_failsafe > 800:
            return False
        if col < self.COLS-1:
            if self.get_square_state(col+1,row) == old_state:
                self.__fill(col+1,row,old_state,new_state)
        if row < self.ROWS-1:
            if self.get_square_state(col,row+1) == old_state:
                self.__fill(col,row+1,old_state,new_state)
        if col > 0:
            if self.get_square_state(col-1,row) == old_state:
                self.__fill(col-1,row,old_state,new_state)
        if row > 0:
            if self.get_square_state(col,row-1) == old_state:
                self.__fill(col,row-1,old_state,new_state)
    
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

    def set_cursor(self, cursor=1):
        if cursor == 0:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor((self.COLS, self.ROWS), self.HOT_SPOT, *pygame.cursors.compile(self.get_cursor()))

    def load_cursor(self):
        while True:
            name = input("What is the name of the cursor you want to load? (Use ONLY letters): ")
            if name.isalpha():
                break
        name = str(name).lower()
        if not name in pclib.Cursor.library.keys():
            print(f"{name} doesn't exist in the library.")
            return False
        cursor = pclib.Cursor.library[name]
        self.COLS = cursor.size[0]
        self.ROWS = cursor.size[1]
        self.HOT_SPOT = cursor.hot_spot
        self.GRID = []
        for i, line in enumerate(cursor.cursor):
            self.GRID.append([])
            line = line.strip("'")
            for char in line:
                if char == "X":
                    self.GRID[i].append(1)
                elif char == ".":
                    self.GRID[i].append(-1)
                else:
                    self.GRID[i].append(0)

    def save_cursor(self):
        cursor = self.get_cursor()
        while True:
            name = input("What is the name of the cursor you want to load? (Use ONLY letters): ")
            if name.isalpha():
                break
        name = str(name).lower()
        with open("pygame_cursor_library.py", "a+") as filename:
            filename.write(name + " = Cursor(\n")
            filename.write("    '" + name + "',\n") 
            filename.write("    " + str((self.COLS, self.ROWS)) + ",\n")
            filename.write("    " + str(self.HOT_SPOT) + ",\n")
            filename.write("    (\n")
            for line in cursor:
                filename.write("        '" + str(line) + "',\n")
            filename.write("    )\n")
            filename.write(")\n\n")

    def reset(self):
        self.COLS, self.ROWS = input_size()
        self.HOT_SPOT = (self.COLS//2, self.ROWS//2)
        self.GRID = []
        self.build_grid()

def input_cols():
    while True:
        COLS = input("What WIDTH (columns) your cursor will have? (Must be divisible by 8): ")
        if COLS.isdecimal():
            COLS = int(COLS)
            if COLS == 0:
                print("You cannot have a cursor with 0 WIDTH (columns).")
            elif COLS%8 != 0:
                print("WIDTH (columns) must be divisible by 8. (Note: Pygame requirement)")
            elif COLS > 80:
                print("WIDTH (columns) must be less than 81.") 
            else:
                return COLS
        else:
            print("You must give an integer number of columns (WIDTH).")

def input_rows():
    while True:
        ROWS = input("What HEIGHT (rows) your cursor will have? (Must be divisible by 8): ")
        if ROWS.isdecimal():
            ROWS = int(ROWS)
            if ROWS == 0:
                print("You cannot have a cursor with 0 HEIGHT (rows).")
            elif ROWS%8 != 0:
                print("HEIGHT (rows) must be divisible by 8. (Note: Pygame requirement)")
            elif ROWS > 80:
                print("HEIGHT (rows) must be less than 81.") 
            else:
                return ROWS
        else:
            print("You must give an integer number of rows (HEIGHT).")

def input_size():
    COLS = input_cols()
    ROWS = input_rows()
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
    
    CANVAS = CursorCanvas(COLS, ROWS)

    while run:
        clock.tick(60)
        WINDOW.fill(COLOR_BG)
        CANVAS.show_canvas(WINDOW)
        CANVAS.show_drawing(WINDOW)
        CANVAS.show_grid(WINDOW)
        CANVAS.highlight(WINDOW)

        for event in pygame.event.get():

            click = pygame.mouse.get_pressed()
            if click:
                if pygame.key.get_pressed()[pygame.K_f]:
                    CANVAS.fill()
                else:
                    CANVAS.draw()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CANVAS.set_cursor()
                if event.key == pygame.K_ESCAPE:
                    CANVAS.set_cursor(0)
                if event.key == pygame.K_h:
                    CANVAS.def_hotspot()
                if event.key == pygame.K_l:
                    CANVAS.load_cursor()
                    ZOOM = max(10 - int(CANVAS.ROWS//20), 1)
                    WINDOW = pygame.display.set_mode((CANVAS.WIDTH + ZOOM*10, CANVAS.HEIGHT + ZOOM*10))
                if event.key == pygame.K_s:
                    CANVAS.save_cursor()
                if event.key == pygame.K_r:
                    CANVAS.reset()
                    ZOOM = max(10 - int(CANVAS.ROWS//20), 1)
                    WINDOW = pygame.display.set_mode((CANVAS.WIDTH + ZOOM*10, CANVAS.HEIGHT + ZOOM*10))

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

if __name__ == "__main__":
    main()
