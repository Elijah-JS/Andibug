#import libraries
import pygame
import random
import os
import pickle
#initialize game
pygame.init()

#game window dimensions
SCREEN_WIDTH = 375
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Andibug <3')

#set frame rate
clock = pygame.time.Clock()
FPS = 40
#game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0
if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0
#load  images
Andibug_image = pygame.image.load('Andibug 1.png').convert_alpha()
bg_image = pygame.image.load('bg image.gif').convert_alpha()
bg2_image = pygame.image.load('1200 (3).jpg').convert_alpha()
bg3_image = pygame.image.load('1200(4).jpg').convert_alpha()
bg4_image = pygame.image.load('1200(5).jpg').convert_alpha()
bg5_image = pygame.image.load('1200(6).jpg').convert_alpha()
bg6_image = pygame.image.load('pretty sky.jpg').convert_alpha()
platform_image = pygame.image.load('minecraft-ideas.jpg').convert_alpha()

#define colors
WHITE = (255, 255, 255)
Black = (0, 0, 0)
PANEL = (123, 104, 238)
#Define font
font_small = pygame.font.SysFont('Lucida Sans', 20)
font_big = pygame.font.SysFont('Lucida Sans', 24)

#Function for outputting text on screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#function for drawing info panel
def draw_panel():
    pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
    pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH , 30), 2)
    draw_text('SCORE: ' + str(score), font_small, WHITE, 0, 0)

#function for drawing background
def draw_bg(bg_scroll):
    screen.blit(bg_image, (0, 0 + bg_scroll))
    screen.blit(bg2_image, (0, -600 + bg_scroll))
    screen.blit(bg3_image, (0, -1200 + bg_scroll))
    screen.blit(bg4_image, (0, -1800 + bg_scroll))
    screen.blit(bg5_image, (0, -2400 + bg_scroll))
    screen.blit(bg6_image, (0, -3000 + bg_scroll))
    screen.blit(bg6_image, (0, -3600 + bg_scroll))
    screen.blit(bg6_image, (0, -4200 + bg_scroll))
    screen.blit(bg6_image, (0, -4800 + bg_scroll))
    screen.blit(bg6_image, (0, -5400 + bg_scroll))
    screen.blit(bg6_image, (0, -6000 + bg_scroll))
    screen.blit(bg6_image, (0, -6600 + bg_scroll))
    screen.blit(bg6_image, (0, -7200 + bg_scroll))
    screen.blit(bg6_image, (0, -7800 + bg_scroll))
    screen.blit(bg6_image, (0, -8400 + bg_scroll))
    screen.blit(bg6_image, (0, -9000 + bg_scroll))
    screen.blit(bg6_image, (0, -9600 + bg_scroll))



#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(Andibug_image, (55, 55))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False


    def move(self):
        #reset vairable
        scroll = 0
        dx = 0
        dy = 0
        #process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -9
            self.flip = True
        if key[pygame.K_d]:
            dx = 9
            self.flip = False
        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player doesn't go off screen

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        #check collision with platform
        for platform in platform_group:
             #collison in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if above platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20



        # check if player has bounced off top of screen
        if self.rect.top <= SCROLL_THRESH:
            # if player is jumping
            if self.vel_y < 0:
                scroll = -dy




         # update rectangle position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll


    def draw(self):
       screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
     #  pygame.draw.rect(screen, WHITE, self.rect, 2)
#player instance
Andibug = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 22))
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1, 2)
        if score > 1000:
            self.speed = random.randint(1, 3)
        if score > 4000:
            self.speed = random.randint(1, 4)
        if score > 5000:
            self.speed = random.randint(1, 5)
        if score > 6000:
            self.speed = random.randint(1, 6)
        if score > 7000:
            self.speed = random.randint(1, 7)
        if score > 8000:
            self.speed = random.randint(1, 8)
        if score > 9000:
            self.speed = random.randint(1, 9)
        if score > 9000:
            self.speed = random.randint(1, 10)
        if score > 10000:
            self.speed = random.randint(2, 10)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        #move platform side to side if moving platform
        if self.moving == True:
            self.move_counter += 1
            self.rect.x += self.direction * self.speed
        #change platform if it has moved fully or hit wall
        if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.move_counter = 0
        #update platform's vertical position
        self.rect.y += scroll

        #check if platform has gone off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


#create sprite groups
platform_group = pygame.sprite.Group()

#create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
platform_group.add(platform)

#game loop
run = True
while run:

    clock.tick(FPS)

    if game_over == False:

        scroll = Andibug.move()

        #draw background
        bg_scroll += scroll
        if bg_scroll >= 5400:
            bg_scroll = 4200
        draw_bg(bg_scroll)


        #gernerate platforms
        if len(platform_group) < MAX_PLATFORMS:
            p_w = random.randint(40, 60)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type = random.randint(1, 2)
            if p_type == 1 and score > 100:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, p_w, p_moving)
            platform_group.add(platform)

        #update platforms
        platform_group.update(scroll)

        #update score
        if scroll > 0:
            score += scroll

        #draw line at previous high score
        pygame.draw.line(screen, PANEL, (0, score - high_score + SCROLL_THRESH), (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
        draw_text('HIGH SCORE', font_small, PANEL, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

        #draw sprites
        platform_group.draw(screen)
        Andibug.draw()

        #draw panel
        draw_panel()

        #check game Over
        if Andibug.rect.top > SCREEN_HEIGHT:
            game_over = True

    else:
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 8
            for y in range(0, 6, 2):
                pygame.draw.rect(screen, Black, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(screen, Black, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
        else:
            draw_text('GAME OVER!', font_big, WHITE, 130, 200)
            draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
            draw_text('PRESS SPACE TO PLAY AGAIN', font_big, WHITE, 20, 300)

            #update high score
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:

                #reset variables
                game_over = False
                score = 0
                scroll = 0
                bg_scroll = 0
                fade_counter = 0

                #reposition Andibug
                Andibug.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
                #reset platforms
                platform_group.empty()
                # create starting platform
                platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
                platform_group.add(platform)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))


            run = False


    #update display visibility
    pygame.display.update()

