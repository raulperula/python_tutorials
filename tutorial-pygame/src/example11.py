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
for index in range(15):
    width = random.randrange(15, 45)
    height = random.randrange(20, 60)
    x_pos = random.randrange(450)
    y_pos = random.randrange(450)
    list_rect.append(pygame.Rect(x_pos, y_pos, width, height))

# main loop
while not quit_cond:
    # check events
    for event in pygame.event.get():
        # detect a QUIT event (window cross)
        if event.type == pygame.QUIT:
            quit_cond = True

    # 20 frames per second
    clock.tick(20)

    # fill background with a color
    screen.fill((0, 0, 0))

    # draw random rectangles
    for rects in list_rect:
        pygame.draw.rect(screen, (0, 200, 0), rects)

    # refresh the window
    pygame.display.update()

# close the window
pygame.quit()
