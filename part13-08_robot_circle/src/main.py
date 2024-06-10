# WRITE YOUR SOLUTION HERE:
import pygame, math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    for i in range(10):
        x = 320+math.cos(angle+6.28*(i/10))*130-robot.get_width()/2
        y = 240+math.sin(angle+6.28*(i/10))*130-robot.get_height()/2
        window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)