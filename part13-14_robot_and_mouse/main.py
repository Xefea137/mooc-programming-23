# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

        if events.type == pygame.MOUSEMOTION:
            x = events.pos[0] - robot.get_width()/2
            y = events.pos[1] - robot.get_height()/2

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()