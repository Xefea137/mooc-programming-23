# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")
x = 300
y = 100
x_speed = 2
y_speed = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += x_speed
    y += y_speed

    if y+ball.get_height() >= height:
        y_speed = -2
    if x+ball.get_width() >= width:
        x_speed = -2
    if y == 0:
        y_speed = 2
    if x == 0:
        x_speed = 2
        
    clock.tick(60)