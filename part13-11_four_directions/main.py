# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
x, y = width/2, height/2

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                to_left = True
            if events.key == pygame.K_RIGHT:
                to_right = True
            if events.key == pygame.K_UP:
                to_up = True
            if events.key == pygame.K_DOWN:
                to_down = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT:
                to_left = False
            if events.key == pygame.K_RIGHT:
                to_right = False
            if events.key == pygame.K_UP:
                to_up = False
            if events.key == pygame.K_DOWN:
                to_down = False

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)