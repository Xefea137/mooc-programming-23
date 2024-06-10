# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

robots = []
for item in range(10):
    robots.append([random.randint(0, width-robot_width), random.randint(-500, 0)])

clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

    for i in range(10):
        if robots[i][1]+robot_height <= height:
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot_width or robots[i][0] >= width:
                robots[i] = [random.randint(0, width-robot_width), random.randint(-500, 0)]
            elif robots[i][0] >= width/2:
                robots[i][0] += 1
            elif robots[i][0] <= width/2:
                robots[i][0] -= 1

    window.fill((0, 0, 0))
    for i in range(10):
        window.blit(robot, (robots[i]))
    pygame.display.flip()

    clock.tick(60)