#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame


def main():
    pygame.init()

    # set window size
    screen = pygame.display.set_mode([300, 300])
    # set window title
    pygame.display.set_caption("Tutorial number 2")

    # exit (quit)
    quit_cond = False

    # timer
    clock = pygame.time.Clock()

    # white color in RGB
    white = (255, 255, 255)

    # main loop
    while not quit_cond:
        # check events
        for event in pygame.event.get():
            # detect a QUIT event
            if event.type == pygame.QUIT:
                quit_cond = True

        # 20 frames per second
        clock.tick(20)

        # fill with a color background
        screen.fill(white)

        # refresh the window
        pygame.display.update()

    # close the window
    pygame.quit()


# Main
main()
