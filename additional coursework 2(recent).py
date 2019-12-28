# please note lose conditions have not been implemented as of yet, neither have win lose screens, if onene were to win they are sent back to the start up screen.
# the bullets of the sprite also no longer sync up with the defender sprites movements as of my adding the sprite to the aliens group, this is due to me changing how the defenders rect is moved and as of yet not finding a suitable change to make to the bullet sprite.
import pygame
#from pygame.sprite import *
#import time
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Attack of the cromulons')
pygame.display.update()

#THE USER STARTS THE GAME!
gameRunning = False
x=0
y=0
x2=0
y2=0
defX=0# This is left from a previous design of the code, it has not been removed because it does not change how the game runs
defenderX=0
clock = pygame.time.Clock()
FPS = 60
bulletY=0
bulletX=0
counter=0
timer= 0
level= 1
#this did not need to be a boolean variable it was just convenient in choosing what directin to send the Sprites in
direction=True
class Alien(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                #image loaded from the same file as the coursework so no need for the entire filename to be written
                self.image= pygame.image.load("alien.png")#.convert()
                # image was initially far too large, this line sets it to a fixed size
                self.image = pygame.transform.scale(self.image, (35, 35))
                #self.rect = self.image.get_rect().move(x, y)

                # this line acually draws it to a given position on the screen
                gameDisplay.blit(self.image,(x2, y2))
                #creates a rectangle to act as the hitbox, which will follow the Sprite of the aliens
                self.rect= pygame.sprite.Rect(x2, y2, 35,35)
        def update(self):  # right by 3px per tick
                self.rect = self.rect.move(x, y)

#the default Sprite initiation is used

class Defender(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image= pygame.image.load("rick and morty.jpg")
                self.image = pygame.transform.scale(self.image, (50, 50))
                gameDisplay.blit(self.image, (400, 550))
                self.rect = pygame.sprite.Rect(400, 550, 50, 50)
        def update(self):
                self.rect = self.rect.move(defenderX, 0)



class Bullet(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image= pygame.image.load("bullet.jpeg")
                self.image = pygame.transform.scale(self.image, (7, 20))
                self.rect = pygame.sprite.Rect(defender.rect.x + 20, 550, 7, 20)
                #the bullet is blited to 425 + defX to place it at the centre of the defender Sprite, the variable bulletX
                gameDisplay.blit(self.image, (defender.rect.x+ 20, 550))
        def update(self):
                self.rect = self.rect.move(0, -25)

class Background():
        def __init__(self):
                self.image= pygame.image.load("background.jpg")
                self.image= pygame.transform.scale(self.image,(800,600))
                gameDisplay.blit(self.image,(0, 0))

def text(msg, posx, posy):
        font = pygame.font.SysFont(None, 55)
        textObj = font.render(msg, True, (255, 255, 255))
        gameDisplay.blit(textObj, [posx, posy])


def level2():
        #Background()
        gameDisplay.fill((0, 0, 0))
        text("brace yourself", 100, 155)
        text("here comes another wave", 50, 205)

        pygame.display.flip()
        clock.tick(0.5)

def lose():
        global x2, y2
        #this loop itarates through the aliens to delete all remaining aliens in the event of a lose screen, to prevent them from interupting the next game being played
        for alien in allAliens:
                allAliens.remove(alien)
        gameDisplay.fill((0, 0, 0))

        text("some cromulons made it to earth,", 10, 100)
        text("Guess we better find a new reality morty.", 10, 160)
        pygame.display.flip()
        clock.tick(0.25)



alien = Alien()
defender = Defender()
bullet = Bullet()
allAliens = pygame.sprite.Group()#adding the defender to the alien group so it will not need to be called sepparatly.
allBullets = pygame.sprite.Group()




def StartScreen():
        global gameRunning, x2, y2
        allAliens.add(defender)
        gameRunning=False
        y2=0
        while y2<=200:
            x2= 0
            while x2<=400:
                    x2+= 40
                    alien= Alien()
                    allAliens.add(alien)

            y2+= 40

        while gameRunning==False:
                #Background()
                gameDisplay.fill((0, 0, 0))
                text("welcome all, to the", 50, 100)# each time the function is called the local variable are used to change the position and content of the text
                text("world of Rick and Morty", 50, 155)
                text("stop the cromulons!!!", 50, 210)
                text("use the arrow keys to move,", 50, 265)
                text("space to fire.", 50, 315)
                text("press arrow up to begin.", 250, 400)

                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                                if event.key == pygame.K_UP:
                                        gameRunning= True

                pygame.display.flip()
                clock.tick(FPS)

#START THE GAME LOOP.

StartScreen()
while gameRunning:
        Background()
        allAliens.draw(gameDisplay)
        allAliens.update()
        allBullets.draw(gameDisplay)
        allBullets.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameRunning= False

                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                defX-= 10
                                defenderX=-10
                        elif event.key == pygame.K_RIGHT:
                                defX += 10
                                defenderX=10
                        elif event.key ==pygame.K_SPACE:
                                bullet=Bullet()
                                allBullets.add(bullet)

                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                                defenderX= 0
                        elif event.key == pygame.K_RIGHT:
                                defenderX= 0



        if (counter> 40):
                direction= False
                y= 25
                clock.tick()
                allAliens.update()
                allBullets.update()
        elif (counter<0):
                direction= True
                y= 25
                clock.tick(FPS)
                allAliens.update()
                allBullets.update()
        if direction==True:
                x= 4
                counter+= 1
                y= 0
                clock.tick(FPS)
                allAliens.update()
                allBullets.update()
        elif direction == False:
                x= -4
                counter-= 1
                y= 0
                clock.tick(FPS)
                allAliens.update()
                allBullets.update()
          #  if bulletY>-50:
           #     Bullet()
            #    bulletY=bulletY- 50
        if pygame.sprite.groupcollide(allBullets, allAliens, True, True):
                print("sprite dead")

        if timer >= 800:
            print("you lose")
            lose()# calls the lose screen for a set time
            direction= True
            counter= 0
            timer= 0
            StartScreen() # calls the start screen, which allows the user to restart the game

        if len(allAliens)<= 1 and level==1:
                print ("wave 2!")
                level= 2
                timer= 0
                direction=True
                counter= 0
                level2()
                #now a new list of aliens will be created for the next stage
                y2= 0
                while y2 <= 280:
                    x2 = 0
                    while x2<=400:
                            x2 += 40
                            alien = Alien()
                            allAliens.add(alien)

                    y2 += 40
        if len(allAliens)<=1 and level==2:
            print("victory!")
            counter = 0
            direction = True
            StartScreen()



        timer+=1
        #print(timer)

        clock.tick(FPS)
        pygame.display.flip()


pygame.quit()
quit()
