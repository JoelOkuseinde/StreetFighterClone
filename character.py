#import and initialise pygame 
import pygame 
#Character Class
class Character():
    #attributes
    def __init__(self,x, y): #x and y are coordinates 
        self.rect = pygame.Rect((x, y, 85, 160)) #using rectangles as placeholder 
        self.v_y  = 0  #velcoity, how fast the y position changes 
        self.j = False #is the player currently airborne?
        self.p = False #is the player currently punching?
        self.p_v = 0 #punch version, for the differnt types of punches
        self.turn = False #is the player facing the opponent?
        self.h = 500 #health of player 
    #methods
    def move(self, screenWidth, screenHeight, surface, enemy):
        S = 12 #speed 
        G = 1.5 #gravity 
        dx = 0 
        dy = 0 
        #key pressing 
        key = pygame.key.get_pressed() 
        #movement 
        if key[pygame.K_a]:
            dx = -S
        if key[pygame.K_d]:
            dx = S
        #make sure play doesnt come of screen 
        #left handside
        if self.rect.left + dx < 0: #if the position of the player + the spped is below zero i.e beyond the of screen
            dx = -self.rect.left #...then change dx to be distancre between the edge of the screen and the left hand side of the player
       #right handside 
        if self.rect.right + dx > screenWidth: #same logic as above
            dx = screenWidth - self.rect.right
        #falling off 
        if self.rect.bottom + dy > screenHeight -  50: #same logic but for the y axis 
            self.v_y = 0 #setting velocity to 0
            self.j = False #since player is in contact with the "ground", jumping can take place
            dy = screenHeight - 50 - self.rect.bottom #creating distance
        #jumping 
        if key[pygame.K_w]:
            if self.j == False:
                self.v_y = -24
                self.j = True  #jump variable becomes true and can no longer jump 
        #adding gravity 
        self.v_y += G #the velocity wil always be brought back down becasue of gravity 
        dy += self.v_y #simmilar to the SPEED VARIABLE, but the y variable is changing 
        #what direcetion is the player facing? 
        if enemy.rect.centerx > self.rect.centerx: #if the enemy position is greater than the player
            self.turn = False #dont turn
        else:
            self.turn = True #otherwise, turn to face the opponent 
        #changing the position of the player 
        self.rect.x += dx 
        self.rect.y += dy  
        #punching
        #jab
        if key[pygame.K_7]:
            self.jab(surface, enemy) #allow the player to punch 
            self.p_v = 1   
        #hook
        if key[pygame.K_8]:    
            self.hook(surface, enemy)
            self.p_v = 2
        #uppercut
        if key[pygame.K_9]:
            self.upcut(surface, enemy)
            self.p_v = 3
    #punching methods
    def jab(self, surface, enemy):       #box comes from centre of rectangle  #hitbox thrown 3 times away from player 
        punch_rect = pygame.Rect(self.rect.centerx - (2.5 * self.rect.width * self.turn), self.rect.y, 2.5 * self.rect.width, 0.4 * self.rect.height)
        pygame.draw.rect(surface, (255, 0, 0), punch_rect) #draws the hitox
        if punch_rect.colliderect(enemy.rect): #if the hitbox comes into contact with another rectangle
            enemy.h -= 2
    def hook(self, surface, enemy):       #box comes from centre of rectangle  #hitbox thrown 2 times away from player 
        punch_rect = pygame.Rect(self.rect.centerx - (1.7 * self.rect.width * self.turn), self.rect.y, 1.6 * self.rect.width, 0.6 *self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), punch_rect) #draws the hitox
        if punch_rect.colliderect(enemy.rect): #if the hitbox comes into contact with another rectangle
            enemy.h -= 5
    def upcut(self, surface, enemy):       #box comes from centre of rectangle  #hitbox thrown 1 times away from player 
       punch_rect = pygame.Rect(self.rect.centerx - (1.15 * self.rect.width * self.turn), self.rect.y, 1.2 * self.rect.width, 0.9 * self.rect.height)
       pygame.draw.rect(surface, (255, 174, 66), punch_rect) #draws the hitox
       if punch_rect.colliderect(enemy.rect): #if the hitbox comes into contact with another rectangle
            enemy.h -= 8
    def draw(self, surface, colour): #draw player to the screen 
        pygame.draw.rect(surface, colour, self.rect)