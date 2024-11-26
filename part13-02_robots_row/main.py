# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()

window.fill((0, 0, 0))

x = 50
for item in range(10):
    window.blit(robot, (x, 100))
    x += width
pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()