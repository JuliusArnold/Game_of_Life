import numpy as np
import pygame
import time
pygame.init()

grid_gray =  (0,0,0)
class Grid:
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    temp_board = board

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.selected = None
        self.model = None

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
        if self.cubes[row][col].value == 1:
            self.cubes[row][col].value = 0
            self.board[row][col] = 0
        else: 
            self.cubes[row][col].value = 1 
            self.board[row][col] = 1 

    def calc_next_state(self):
        #calculate temp 
        print("Board:   ")
        print(np.array(self.board))
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
                
        print("Temp_Board:")
        print(np.array(self.temp_board))
        
        # Pass new states to the cubes and to board then set temp back to 0 
        for i in range(len(self.temp_board)):
            for j in range(len(self.temp_board[i])):
                self.board[i][j] = self.temp_board[i][j]
                #self.temp_board[i][j] = 0

        for i in range(len(self.cubes)):
            for j in range(len(self.cubes[i])):
                self.cubes[i][j].value = self.board[i][j]

        print("Board2: ")
        print(np.array(self.board))


                

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]


class Cube:
    rows = 18
    cols = 18
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / self.rows
        x = self.col * gap
        y = self.row * gap
#       if self.temp != 0 and self.value == 0:
#            text = fnt.render(str(self.temp), 1, (128,128,128))
#            win.blit(text, (x+5,y+5))
#        elif not(self.value == 0) :
#            text = fnt.render(str(self.value), 1, (0,0,0))
#            win.blit(text, (x+gap/2 - text.get_width()/2, y+gap/2 - text.get_width()/2))
        if self.value == 1:
            pygame.draw.rect(win, (0,0,0), (x,y, gap ,gap))

def  draw_window(win, board):
    win.fill((255, 255, 255))

    fnt = pygame.font.SysFont("comicsans",40)

    board.draw(win)

def main():
    win = pygame.display.set_mode((542,542))
    pygame.display.set_caption("Conway's Game of Life")
    run = True
    board = Grid(18,18,540,540)
    preperationphase = True

    # Main Loop
    while run:
        if preperationphase:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("Start Game")
                        # preperationphase = False
                        board.calc_next_state()
                    if event.key == pygame.K_SPACE:
                        preperationphase = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = board.click(pos)
                    board.select(clicked[0],clicked[1])

            draw_window(win, board)
            pygame.display.update()
        else: #Game play phase 
            # pygame-Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # delay 
            pygame.time.wait(500)
            # calculate temp state
            board.calc_next_state()
            # quit()
            # Update states 
            #
            # reset temp state
            #
            #
            # Draw updated Window
            draw_window(win, board)
            pygame.display.update()
            
        pygame.display.update()

main()

