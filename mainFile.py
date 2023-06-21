#import and initialise pygame 
import pygame 
from character import Character #importing the Character class from the character file
pygame.init()
#create game window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Punching Game")
#set framerate 
clock = pygame.time.Clock()
FPS = 60 
#game variables
gameStart = False 
gamePaused = False 
gameInstruct = False
isPaused = False 
#flip 
def flip(a):
    if a == True:
        a = False 
        return a 
    elif a == False:
        a = True 
        return a 
#define fonts 
font = pygame.font.SysFont("arialblack", 40)
#define colours 
textColour = (255, 255, 255)
#onscreen text 
def draw_text(text, font, textColour, x, y):
    img = font.render(text, True, textColour)
    screen.blit(img, (x, y)) 
#Instruction Game State 
def instr():
    draw_text("Instructions", font, textColour, 0, 0)
    draw_text("Press 1 to Left Jab", font, textColour, 0, 50)
    draw_text("Press 2 to Right Jab", font, textColour, 0, 100)
    draw_text("Press 3 to Left Hook", font, textColour, 0, 150)
    draw_text("Press 4 to Right Hook", font, textColour, 0, 200)
    draw_text("Press 5 to Left Uppercut", font, textColour, 0, 250)
    draw_text("Press 6 to Right Uppercut", font, textColour, 0, 300)
    draw_text("Press A to Move Left", font, textColour, 0, 350)
    draw_text("Press D to Move Right", font, textColour, 0, 400)
    draw_text("Hold W to Jump", font, textColour, 0, 450)
    draw_text("Press S to Block", font, textColour, 0, 500)
    draw_text("Press I to return to previous menu", font, textColour, 0, 550)
#create characters 
#player 
player = Character(65, 450)
#dummy
dummy = Character(750, 342)
#create charater health bar
def draw_health(h, x, y):
    health = h / 500 #create a ratio from the health parameter, the width is * by the ratio
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 420, 25)) #bar under heallth bar for visibility 
    pygame.draw.rect(screen, (255, 0, 255), (x, y, 420 * health, 25))
#game loop 
run = True 
while run:
    clock.tick(FPS) #game runs at constant fps 
    screen.fill((50, 20, 205)) #sets the game background colour to be blue
    #checks the game state 
    if gamePaused == True: #pause the game 
        if gameInstruct == True: #states the instructions 
            instr()
            isPaused = False 
        else:
            draw_text("Paused", font, textColour, 0, 0)
            draw_text("Press P to resume", font, textColour, 0, 100)
            draw_text("Press I for Instructions", font, textColour, 0, 200)
            draw_text("Press X to Quit", font, textColour, 0, 300)
            isPaused = True
    elif gameStart == True:
        #move characters 
        player.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, dummy)
        #draw the chaacter onto the screen 
        player.draw(screen, (255, 255, 255)) 
        dummy.draw(screen, (0, 0, 0))
        #call health function for each character
        draw_health(player.h, 20, 20)
        draw_health(dummy.h, 460, 20)
        isPaused = False 
    elif gameInstruct == True: #states the instructions 
        instr()
        isPaused = False 
    #main menu 
    else:
        draw_text("Punching Game", font, textColour, 100,50) #displays text on screen at the stated coordinates 
        draw_text("Press SPACE to start", font, textColour, 100, 150) #start the game 
        draw_text("Press I for instructions", font, textColour, 100, 250) #show instructions 
        draw_text("Press X to quit", font, textColour, 100, 350) #quits game 
        isPaused = True
    #event handler -- toggles game states 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #checks for the event of a key press
            if event.key == pygame.K_SPACE: #starts game
                gameStart = True
            if event.key == pygame.K_p: #pause game
                gamePaused = flip(gamePaused)
            if event.key == pygame.K_i: #shows instructions 
                gameInstruct = flip(gameInstruct)
            if event.key == pygame.K_x: #quits game 
                if isPaused == True:
                    run = False 
        if event.type == pygame.QUIT:
            run = False 
    pygame.display.update() #update to the display 
pygame.quit() #quit pygame once the while loop is completed