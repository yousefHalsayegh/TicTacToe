import pygame as pg, sys
from pygame.locals import *
import time 
import Brain
import Board

#Initialize variables 

width = 400 
height = 400
white = (255, 255, 255)
gray = (170,170,170)
black = (10,10,10)
buttonW = width/2 - 70
#Main menu buttons
quit_buttonH = height/2 + 150
human_buttonH = height/2
humanVai_buttonH = height/2 + 50 
aiVai_buttonH = height/2 + 100

#Agent brain buttons
random_buttonH = height/2
smaller_buttonH = height/2 + 50 
bigger_buttonH = height/2 + 100
back_buttonH = height/2 + 150

switch = False
our_agent = Brain.Agent(2, 0)
cpu = Brain.Agent(-1, 1)

screen_number = 1

#Board 
game = Board.Board()


#Start window 
pg.init()
text_font = pg.font.SysFont('Corbel',35)
text_fontB = pg.font.SysFont('Corbel',54)
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0 ,32)
pg.display.set_caption("Tic Tac Toe")


#Lodaing images
x_img = pg.image.load('X.png')
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.image.load('O.png')
o_img = pg.transform.scale(o_img, (80,80))


def game_opening():
    """
    This method create the first screen the player see
    conist of 4 buttons and a title screen 
    """
    screen.fill(white)

    #Drawing the title 
    title =  text_fontB.render('Tic Tac Toe', True, black)
    screen.blit(title , (width/2 - 110 ,height/2 - 80))

    #Drawing Human vs Human Button 
    human_text = text_font.render('P1 Vs P2', True, black) 
    pg.draw.rect(screen,gray,[buttonW, human_buttonH,140,40])
    screen.blit(human_text , (buttonW + 15 ,human_buttonH))

    #Drawing Human vs Ai 
    ai_text = text_font.render('P1 Vs AI', True, black) 
    pg.draw.rect(screen,gray,[buttonW, humanVai_buttonH,140,40])
    screen.blit(ai_text , (buttonW + 15 ,humanVai_buttonH))

    #Drawing Ai vs Ai 
    ai_text2 = text_font.render('AI Vs AI', True, black) 
    pg.draw.rect(screen,gray,[buttonW, aiVai_buttonH,140,40])
    screen.blit(ai_text2 , (buttonW + 15 ,aiVai_buttonH))

    #Drawing the Quit Button 
    quit_text = text_font.render('Quit', True, black) 
    pg.draw.rect(screen,gray,[buttonW, quit_buttonH,140,40])
    screen.blit(quit_text , (buttonW + 40 ,quit_buttonH))

    pg.display.update()


def agent_selection():
    """
    This method create the agent selection screen if the player
    choose any of the options that contain 'Ai' and it will 
    enable him/her to choose a specific agent type
    """
    screen.fill(white)

    #Drawing the title 
    title =  text_fontB.render('Tic Tac Toe', True, black)
    screen.blit(title , (width/2 - 110 ,height/2 - 80))

    #Drawing Random Ai button
    random_text = text_font.render('Random', True, black) 
    pg.draw.rect(screen,gray,[buttonW, random_buttonH,140,40])
    screen.blit(random_text , (buttonW + 10 ,random_buttonH))

    #Drawing Aggresive Ai button 
    smaller_text = text_font.render('Depth = 2', True, black) 
    pg.draw.rect(screen,gray,[buttonW, smaller_buttonH,140,40])
    screen.blit(smaller_text , (buttonW ,smaller_buttonH))

    #Drawing Defensive Ai button  
    bigger_text = text_font.render('Depth = 4', True, black) 
    pg.draw.rect(screen,gray,[buttonW, bigger_buttonH,140,40])
    screen.blit(bigger_text , (buttonW ,bigger_buttonH))

    #Drawing the Back Button 
    back_text = text_font.render('Back', True, black) 
    pg.draw.rect(screen,gray,[buttonW, back_buttonH,140,40])
    screen.blit(back_text , (buttonW + 40 ,back_buttonH))

    pg.display.update()


def game_board():
    """
    This method will create UI for the game board
    """
    pg.display.update()
    screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(screen,black,(width/3,0),(width/3, height),7)
    pg.draw.line(screen,black,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,black,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,black,(0,height/3*2),(width, height/3*2),7)
    draw_status()

def draw_status():
    """
    This method draw the game status present in the bottom 
    part of the screen when the players and playing the game
    """
    if game.status == -1:
        message =  'X' + "'s Turn" if game.turn == 0 else 'O' + "'s Turn"

    elif game.status == 2:
        message = 'Game Draw!'

    else:
        message =  'X' + " won!" if game.status == 0 else 'O' + " won!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
    

def check_win():
    global game

    game.terminal()
    condition = game.condition 

    if condition == 1:
        pg.draw.line(screen, (250,0,0), (0, (game.index + 1)*height/3 -height/6),\
                              (width, (game.index + 1)*height/3 - height/6 ), 4)
    elif condition == 2:
        pg.draw.line (screen, (250,0,0),((game.index + 1)* width/3 - width/6, 0),\
                          ((game.index + 1)* width/3 - width/6, height), 4)
    elif condition == 3:
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
    elif condition == 4:
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

    draw_status()

def drawXO(row,col):
    """
    args:
    row : the index of the row that have been clicked
    col : the index of the coloum that have been clicked
    ---------------------------------------------------
    This method make sure to draw the X or O 
    in the appropiate square that the player or AI
    clicks on.
    """
    global game
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30
    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
    game.matrix[row - 1][col - 1] = 'X' if game.turn == 0 else 'O'
    if(game.turn == 0):
        screen.blit(x_img,(posy,posx))
        game.turn = 1
    else:
        screen.blit(o_img,(posy,posx))
        game.turn = 0
    pg.display.update()


def userClick():
    """
    This method locate the square the player clicked on
    """
    global switch
    mouse = pg.mouse.get_pos()
    #get column of mouse click (1-3)
    if(mouse[0]<width/3):
        col = 1
    elif (mouse[0]<width/3*2):
        col = 2
    elif(mouse[0]<width):
        col = 3
    else:
        col = None
    #get row of mouse click (1-3)
    if(mouse[1]<height/3):
        row = 1
    elif (mouse[1]<height/3*2):
        row = 2
    elif(mouse[1]<height):
        row = 3
    else:
        row = None
    #print(row,col)
    if(switch == 1):
        if(row and col and game.matrix[row - 1][col - 1] is None):
            #draw the x or o on screen
            drawXO(row,col)
            check_win()
    elif(switch == 2):
        if(row and col and game.matrix[row - 1][col - 1] is None):
            #draw the x or o on screen
            drawXO(row,col)
            check_win()
        if (game.status < 0):
            row, col = cpu.action(game)
            #draw the x or o on screen
            drawXO(row,col)
            check_win()
        

def main_menu():
    """
    this method check which button that have been chosen 
    and act accrodingly
    """
    global screen_number, switch 
    mouse = pg.mouse.get_pos()
    if buttonW <= mouse[0] <= buttonW +140 :
        if quit_buttonH <= mouse[1] <= quit_buttonH + 40:
            pg.quit()
            sys.exit()
        elif human_buttonH <= mouse[1] <= human_buttonH + 40:
            game_board()
            switch = 1
            screen_number = 3
        elif humanVai_buttonH <= mouse[1] <= humanVai_buttonH + 40:
            agent_selection()
            switch = 2
            screen_number = 2
        elif aiVai_buttonH <= mouse[1] <= aiVai_buttonH + 40:
            agent_selection()
            switch = 3
            screen_number = 2

def brain_screen():
    """
    this method check which button that have been chosen 
    and act accrodingly
    """
    global screen_number, switch, our_agent
    mouse = pg.mouse.get_pos()
    if buttonW <= mouse[0] <= buttonW +140 :
        if back_buttonH <= mouse[1] <= back_buttonH + 40:
            game_opening()
            screen_number = 1
        elif random_buttonH <= mouse[1] <= random_buttonH + 40:
            cpu.type = 0
            game_board()
            screen_number = 3
        elif smaller_buttonH <= mouse[1] <= smaller_buttonH + 40:
            cpu.type = 1
            game_board()
            screen_number = 3
        elif bigger_buttonH <= mouse[1] <= bigger_buttonH + 40:
            cpu.type = 2
            game_board()
            screen_number = 3


def reset_game():
    """
    This method reset everything in the game to 
    start over
    """
    global game, screen_number, switch 
    time.sleep(3)
    game_opening()
    game.reset()
    screen_number = 1
    switch = False


game_opening()
# run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            if screen_number == 1:
                main_menu()

            elif screen_number == 2:
                brain_screen()

            elif screen_number == 3:
                if switch == 3:
                    while(game.status == -1):
                        row, col = our_agent.action(game)
                        drawXO(row,col)
                        check_win()
                        if((game.status == - 1)):
                            row, col = cpu.action(game)
                            #draw the x or o on screen
                            drawXO(row,col)
                            check_win()
                            if(game.status > -1):
                                break
                userClick()
                if(game.status > -1):
                    reset_game()
    pg.display.update()
    CLOCK.tick(fps)