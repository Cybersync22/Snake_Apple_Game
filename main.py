#Snake and Apple game using Python

import pygame 
from pygame.locals import * #imports KEYDOWN
import time
import random
#import time //putting a delay so that the screen stays

#Draw block function
SIZE = 39
BG = (27,54,39)

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("APPLE.png").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 4
        self.y = SIZE * 4

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
 
    def move(self):
        self.x = random.randint(0,20) * SIZE
        self.y = random.randint(0,20) * SIZE
    

class Snake:
    def __init__(self,parent_screen,length):
        #load the image
        self.length = length
        self.parent_screen = parent_screen
        self.BLOCK = pygame.image.load("BLOCK.png").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'
    
    def inc_length(self): #increase length on collision
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
    
    def draw(self):
        self.parent_screen.fill((BG))
        for i in range(self.length):
            self.parent_screen.blit(self.BLOCK,(self.x[i],self.y[i]))
        pygame.display.flip()

#movement of the snake 
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    #The snake walks automatically
    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()
            

class Game:
    def __init__(self):
         pygame.init()
         pygame.display.set_caption("CODEBASICS SNAKE AND APPLE GAME")

         pygame.mixer.init()
         self.play_bg_music()

         self.surface = pygame.display.set_mode((1000,800))
         self.snake = Snake(self.surface,2)
         self.snake.draw()
         self.apple = Apple(self.surface)
         self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True 
        return False
    
    def play_bg_music(self):
        pygame.mixer.music.load("MUSIC.mp3")
        pygame.mixer.music.play()

    def Display_Score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(800,10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.Display_Score()
        pygame.display.flip()

        #snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            SOUND = pygame.mixer.Sound("TING.mp3")
            pygame.mixer.Sound.play(SOUND)
            self.apple.move()
            self.snake.inc_length()
            # print ("Collision Ocurred") #this mssg will print

        #snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def show_Game_Over(self):
        self.surface.fill(BG)
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f" GAME OVER! Your Score is {self.snake.length}",True,(255,255,255))
        self.surface.blit(line1,(200,300))
        line2 = font.render(f"To play again press ENTER. To exit press ESCAPE!!",True,(255,255,255))
        self.surface.blit(line2,(200,350))

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Apple(self.surface)


    def run(self):
        running = True #event loop
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False 

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    #the window will close when esc is hits
                    #pass
                        
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                    
                elif event.type == QUIT:
                    running = False #to exit the window
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_Game_Over()
                pause = True
                self.reset()

            time.sleep(0.2)


if __name__=="__main__":
    game = Game()
    game.run()
   

pygame.display.flip()

#time.sleep(5)





          
