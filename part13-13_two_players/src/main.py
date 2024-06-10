# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")
x1, y1 = width, height/2
x2, y2 = 0, height/2

to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False

to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False

clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                to_left1 = True
            if events.key == pygame.K_RIGHT:
                to_right1 = True
            if events.key == pygame.K_UP:
                to_up1 = True
            if events.key == pygame.K_DOWN:
                to_down1 = True

            if events.key == pygame.K_a:
                to_left2 = True
            if events.key == pygame.K_d:
                to_right2 = True
            if events.key == pygame.K_w:
                to_up2 = True
            if events.key == pygame.K_s:
                to_down2 = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT:
                to_left1 = False
            if events.key == pygame.K_RIGHT:
                to_right1 = False
            if events.key == pygame.K_UP:
                to_up1 = False
            if events.key == pygame.K_DOWN:
                to_down1 = False

            if events.key == pygame.K_a:
                to_left2 = False
            if events.key == pygame.K_d:
                to_right2 = False
            if events.key == pygame.K_w:
                to_up2 = False
            if events.key == pygame.K_s:
                to_down2 = False

    if to_right1:
        x1 += 2
    if to_left1:
        x1 -= 2
    if to_up1:
        y1 -= 2
    if to_down1:
        y1 += 2
    
    if to_right2:
        x2 += 2
    if to_left2:
        x2 -= 2
    if to_up2:
        y2 -= 2
    if to_down2:
        y2 += 2

    x1 = max(x1,0)
    x1 = min(x1,width-robot1.get_width())
    y1 = max(y1,0)
    y1 = min(y1,height-robot1.get_height())

    x2 = max(x2,0)
    x2 = min(x2,width-robot2.get_width())
    y2 = max(y2,0)
    y2 = min(y2,height-robot2.get_height())

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    clock.tick(60)