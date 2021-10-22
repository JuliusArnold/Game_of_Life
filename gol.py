import numpy as np
import pygame
import time
pygame.init()

# Define Global Variables
_GRIDSIZE = 25 *3
_WINSIZE = 750
grid_gray = (0,0,0)


class Grid:
    global _GRIDSIZE    
    board = [[0 for i in range(_GRIDSIZE + 2)] for j in range(_GRIDSIZE +2)]
    temp_board = board

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]

    def draw(self, win):
        gap = self.width / self.rows
        for i in range(self.rows+1):
            thick = 2
            pygame.draw.line(win, grid_gray,(0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, grid_gray,(i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)


    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / self.rows
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def select(self, row, col):
        # set active/dead cells in grid and cubes
        if self.cubes[row][col].value == 1:
            self.cubes[row][col].value = 0
            self.board[row][col] = 0
        else: 
            self.cubes[row][col].value = 1 
            self.board[row][col] = 1 

    def calc_next_state(self):
        #calculate temp 
        #print("Board:   ")
        #print(np.array(self.board))
        for i in range(len(self.cubes)-1):
            for j in range(len(self.cubes[i])-1):
                #self.temp_board[i][j] = self.board[i][j]
                own_state = self.cubes[i][j].value
                if i == 0 or j == 0 :
                    next_state = own_state 
                else:
                    # Count active neighbours
                    active_neighbours = 0
                    for offset_x in range(-1,2):
                        for offset_y in range(-1,2):
                            active_neighbours += self.cubes[i+offset_y][j+offset_x].value
                    active_neighbours -= self.cubes[i][j].value
                    # Conditions
                    #if i < 5 and j < 5:
                    #    print(own_state,active_neighbours)
                    if own_state == 1 and active_neighbours < 2:
                        next_state = 0
                    elif own_state == 1 and active_neighbours >3:
                        next_state = 0
                    elif own_state == 0 and active_neighbours == 3:
                        next_state = 1
                    else:
                        next_state = own_state
                    #if i < 5 and j < 5:
                    #    print(next_state)
                # Set new state
                self.temp_board[i][j] = next_state
                
        #print("Temp_Board:")
        #print(np.array(self.temp_board))
        
        # Pass new states to the cubes and to board then set temp back to 0 
        for i in range(len(self.temp_board)):
            for j in range(len(self.temp_board[i])):
                self.board[i][j] = self.temp_board[i][j]
                #self.temp_board[i][j] = 0

        for i in range(len(self.cubes)):
            for j in range(len(self.cubes[i])):
                self.cubes[i][j].value = self.board[i][j]

        #print("Board2: ")
        #print(np.array(self.board))


                

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]


class Cube:
    global _GRIDSIZE    
    global _WINSIZE
    rows = _GRIDSIZE
    cols = _GRIDSIZE
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def draw(self, win):
        gap = self.width / self.rows
        x = self.col * gap
        y = self.row * gap
        if self.value == 1:
            pygame.draw.rect(win, (0,0,0), (x,y, gap ,gap))

def  draw_window(win, board):
    # Fll with background color
    win.fill((255, 255, 255))
    # Draw the board
    board.draw(win)



def main():
    # Set speed:
    speed = int(input("Select Speed from 1 to 10: "))


    # Set Window Settings
    win = pygame.display.set_mode((_WINSIZE + 2,_WINSIZE + 2))
    pygame.display.set_caption("Conway's Game of Life")

    # Variables displaying the current State 
    run = True
    preperationphase = True

    # Initialize the grid
    board = Grid(_GRIDSIZE,_GRIDSIZE,_WINSIZE,_WINSIZE)

    # Main Loop
    while run:
        if preperationphase:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Quit
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #Quit
                        run = False
                    if event.key == pygame.K_RETURN:
                        # Play one Generation
                        board.calc_next_state()
                    if event.key == pygame.K_SPACE:
                        # Start 0 Player Game
                        preperationphase = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set cell alive 
                    pos = pygame.mouse.get_pos()
                    clicked = board.click(pos)
                    board.select(clicked[0],clicked[1])
            # Refresh Window
            draw_window(win, board)
            pygame.display.update()
        else: #Game play phase 
            # pygame-Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    if event.key == pygame.K_SPACE:
                        # Pause 0 Player Game
                        preperationphase = True
            # delay 
            pygame.time.wait( int(2000 / speed))
            #Calculate and update State:
            board.calc_next_state()
            # Update Window
            draw_window(win, board)
            pygame.display.update()
        


if __name__ == "__main__":
    main()

