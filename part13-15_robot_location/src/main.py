# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
x, y = random.randint(0, width-robot_width), random.randint(0, height-robot_height)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            quit()
        
        if events.type == pygame.MOUSEBUTTONDOWN:
            x1 = events.pos[0] - robot_width/2
            y1 = events.pos[1] - robot_height/2
            if x1 > x-robot_width/2 and x1 < x+robot_width/2 and y1 > y-robot_height/2 and y1 < y+robot_height/2:
                x, y = random.randint(0, width-robot_width), random.randint(0, height-robot_height)
                
        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()