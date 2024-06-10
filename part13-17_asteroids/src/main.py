# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(f'{" "*80}Asteroids')
game_font = pygame.font.SysFont("Arial", 24)

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

points = 0
total = 5
rocks = []
for i in range(total):
    rocks.append([random.randint(0, width-rock.get_width()), -random.randint(0, 1000)])

to_right = False
to_left = False
stop = False

robot_x, robot_y = width/2 - robot.get_width()/2, height-robot.get_height()

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
        
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT:
                to_left = False
            if events.key == pygame.K_RIGHT:
                to_right = False

    if to_left:
        robot_x -= 2
    if to_right:
        robot_x += 2

    robot_x = max(robot_x, 0)
    robot_x = min(robot_x,width-robot.get_width())

    for i in range(total):
        rocks[i][1] += 1

        if rocks[i][1] + rock.get_height() >= robot_y:
            if robot_x < rocks[i][0] + rock.get_width() and robot_x + robot.get_width() > rocks[i][0]:
                rocks[i] = [random.randint(0, width-rock.get_width()), -random.randint(0, 1000)]
                points += 1

        if rocks[i][1] + rock.get_width() > height:
            stop = True

    if not stop:
        window.fill((0, 0, 0))
        for i in range(total):
            window.blit(rock, (rocks[i]))
        window.blit(robot, (robot_x, robot_y))
        text = game_font.render(f"Points: {points}", True, (255, 0, 0))
        window.blit(text, (500, 10))
        pygame.display.flip()

    clock.tick(60)