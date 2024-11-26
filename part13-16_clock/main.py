# WRITE YOUR SOLUTION HERE:
import pygame, math
from datetime import datetime

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

    current_time = datetime.now().strftime("%H:%M:%S")
    pygame.display.set_caption(f"{' '*85}{current_time}")
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second

    second_angle = second * (2 * math.pi) / 60
    second_x = 320 + math.cos(second_angle - math.pi / 2) * 180
    second_y = 240 + math.sin(second_angle - math.pi / 2) * 180

    minute_angle = minute * (2 * math.pi ) / 60
    minute_x = 320 + math.cos(minute_angle - math.pi / 2) * 155
    minute_y = 240 + math.sin(minute_angle - math.pi / 2) * 155

    hour_angle = ((hour % 12) + (minute / 60)) * (2 * math.pi) / 12
    hour_x = 320 + math.cos(hour_angle - math.pi / 2) * 100
    hour_y = 240 + math.sin(hour_angle - math.pi / 2) * 100

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), (320, 240), 200, 5)
    pygame.draw.circle(window, (255, 0, 0), (320, 240), 10)
    pygame.draw.line(window, (0, 0, 255), (320, 240), (second_x, second_y))
    pygame.draw.line(window, (0, 0, 255), (320, 240), (minute_x, minute_y), 3)
    pygame.draw.line(window, (0, 0, 255), (320, 240), (hour_x, hour_y), 5)
    pygame.display.flip()