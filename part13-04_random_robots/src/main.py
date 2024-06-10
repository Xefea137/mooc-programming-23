# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

for item in range(1000):
    window.blit(robot, (random.randint(0, 640-width), random.randint(0, 480-height)))
pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()