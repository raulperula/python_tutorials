#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame
import random

pygame.init()

# set window size
screen = pygame.display.set_mode((480, 500))

# exit (quit)
quit_cond = False

# timer
clock = pygame.time.Clock()

# create random rectangles
list_rect = []
for index in range(25):
    width = random.randrange(10, 30)
    height = random.randrange(10, 40)
    x_pos = random.randrange(450)
    y_pos = random.randrange(450)
    list_rect.append(pygame.Rect(x_pos, y_pos, width, height))

rect1 = pygame.Rect(0, 0, 25, 25)

# create the text
font1 = pygame.font.SysFont("Arial", 20, True, False)
info = font1.render("Click in rectangles!", 0, (255, 255, 255))

# main loop
while not quit_cond:
    # check events
    for event in pygame.event.get():
        # detect a QUIT event (window cross)
        if event.type == pygame.QUIT:
            quit_cond = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for rects in list_rect:
                if rect1.colliderect(rects):
                    rects.width = 0
                    rects.height = 0

    # 20 frames per second
    clock.tick(20)

    # fill background with a color
    screen.fill((0, 0, 0))

    # move red rectangle
    (rect1.left, rect1.top) = pygame.mouse.get_pos()
    rect1.left -= rect1.width / 2
    rect1.top -= rect1.height / 2

    # draw random rectangles
    for rects in list_rect:
        pygame.draw.rect(screen, (0, 200, 0), rects)
    pygame.draw.rect(screen, (200, 20, 20), rect1)

    # draw text
    screen.blit(info, (5, 5))

    # draw time in secs
    secs = str(pygame.time.get_ticks() / 1000)
    counter = font1.render(secs, 0, (0, 255, 255))
    screen.blit(counter, (300, 5))

    # refresh the window
    pygame.display.update()

# close the window
pygame.quit()
