import numpy as np
import pygame
import sys
import math
import time
ROW_COUNT=6
COLUMN_COUNT=7

def create_board():
    board = np.zeros((6, 7))
    return board

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
def drop_piece(board,row,col,piece):
    board[row][col]=piece
def print_board(board):
    print(np.flip(board,0))


def winning_move(board,piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece :
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

##########for drawing board##########
def draw_board():
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,(0,0,255),(c*SQUARESIXE,r*SQUARESIXE+SQUARESIXE,SQUARESIXE,SQUARESIXE))##########RGB
            pygame.draw.circle(screen,(0,0,0),(int(c*SQUARESIXE+SQUARESIXE/2),int(r*SQUARESIXE+SQUARESIXE+SQUARESIXE/2)),radius)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c]==1:
                pygame.draw.circle(screen,(255,0,0),(int(c*SQUARESIXE+SQUARESIXE/2),height-int(r*SQUARESIXE+SQUARESIXE/2)),radius)
            elif board[r][c]==2:
                pygame.draw.circle(screen,(0,255,0),(int(c*SQUARESIXE+SQUARESIXE/2),height-int(r*SQUARESIXE+SQUARESIXE/2)),radius)
    pygame.display.update()

######numpy board creation
board = create_board()
print(board)
game_over = False
turn = 0

######
pygame.init()
SQUARESIXE=100
width=COLUMN_COUNT*SQUARESIXE
height=(ROW_COUNT+1)*SQUARESIXE
size=(width,height)
screen=pygame.display.set_mode(size)
pygame.init()
radius=int(SQUARESIXE/2-5)
draw_board()
pygame.display.update()
myfont=pygame.font.SysFont("monospace",75)
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,(0,0,0),(0,0,width,SQUARESIXE))
            posx=event.pos[0]
            if turn==0:
                pygame.draw.circle(screen,(255,0,0),(posx,int(SQUARESIXE/2)),radius)
            else:
                pygame.draw.circle(screen,(0,255,0),(posx,int(SQUARESIXE/2)),radius)
        pygame.display.update()



        if event.type==pygame.MOUSEBUTTONDOWN:
            ##for player 1#####
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIXE))
            if turn == 0:
                posx = event.pos[0]  # print(event.pos)it gives the column value
                col = int(math.floor(posx / SQUARESIXE))
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        label=myfont.render("PLAYER 1 WINS",1,(255,0,0))
                        screen.blit(label,(40,10))
                        game_over = True

            else:
                posx = event.pos[0]  # print(event.pos)it gives the column value
                col = int(math.floor(posx / SQUARESIXE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        print("player Two wins")
                        label = myfont.render("PLAYER 2 WINS", 1, (0, 255, 0))
                        screen.blit(label, (40, 10))
                        game_over = True


            print_board(board)
            turn += 1
            turn = turn % 2
            draw_board()
            if game_over:
                pygame.time.wait(3000)



