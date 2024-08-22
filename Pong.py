import pygame
import sys

WIDTH = 800
HEIGHT = 600
FPS = 60
BALL_POS_X = 400
BALL_POS_Y = 300
BALL_SPEED = [3,3]

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
run = True

background = pygame.image.load('Code\\PyGames\\assets\\levels\\bg2.png').convert()

ball = pygame.image.load('Code\\PyGames\\assets\\ball\\ball.png').convert_alpha()
ball_rect = ball.get_rect(center = (BALL_POS_X,BALL_POS_Y))

paddle1 = pygame.image.load('Code\\PyGames\\assets\\bricks\\bricks_2p.png').convert_alpha()
paddle1_rect = paddle1.get_rect(center = (40,300))

paddle2 = pygame.image.load('Code\\PyGames\\assets\\bricks\\bricks_2p.png').convert_alpha()
paddle2_rect = paddle2.get_rect(center = (760,300))

###score = 0

sound = pygame.mixer.Sound('Code\\PyGames\\assets\\sounds\\hit.wav')
audio = pygame.mixer.Sound('Code\\PyGames\\assets\\sounds\\Level 1.wav')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0,0))
    audio.set_volume(1)
    audio.play()

    ###Paddles
    screen.blit(paddle1, paddle1_rect)
    screen.blit(paddle2, paddle2_rect)

    #Paddel movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_rect.y -= 5
    if keys[pygame.K_s]:
        paddle1_rect.y += 5
    if keys[pygame.K_UP]:
        paddle2_rect.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2_rect.y += 5

    #Paddle1
    if paddle1_rect.bottom >= 600:
        paddle1_rect.bottom = 600
    if paddle1_rect.top <= 0:
        paddle1_rect.top = 0

    #Paddle2
    if paddle2_rect.bottom >= 600:
        paddle2_rect.bottom = 600
    if paddle2_rect.top <= 0:
        paddle2_rect.top = 0

    ###Ball to Paddle Collision
    if ball_rect.colliderect(paddle1_rect):
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ball_rect.colliderect(paddle2_rect):
        BALL_SPEED[0] = -BALL_SPEED[0]
            
    ###Ball
    screen.blit(ball, ball_rect)

    #Ball Movement
    ball_rect.x += BALL_SPEED[0]
    ball_rect.y += BALL_SPEED[1]

    #Ball x,y Collision
    if ball_rect.bottom >= 600 or ball_rect.top <= 0: #y
        BALL_SPEED[1] = -BALL_SPEED[1]
    if ball_rect.right >= 800 or ball_rect.left <= 0: #x
        BALL_SPEED[0] = -BALL_SPEED[0]

    #Ball x Exit
    if ball_rect.right >= 800:
        ball_rect.center = (400,300)
    if ball_rect.left <= 0:
        ball_rect.center = (400,300)
            
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()