# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

for y in range(10):
    for x in range(10):
        window.blit(robot, (50+x*40+y*10, 50+y*20))
pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()