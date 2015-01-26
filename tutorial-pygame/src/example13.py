#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame

pygame.init()

# set window size
screen = pygame.display.set_mode((480, 300))

# exit (quit)
quit_cond = False

# timer
clock = pygame.time.Clock()

# create the text
font1 = pygame.font.Font(None, 48)
text1 = font1.render("Hello world!", 0, (255, 255, 255))

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
    screen.fill((30, 30, 200))

    # draw the text
    screen.blit(text1, (100, 100))

    # refresh the window
    pygame.display.update()

# close the window
pygame.quit()
