#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame


def main():
    pygame.init()

    # colors in RGB
    white = (255, 255, 255)
    red = (200, 20, 50)
    blue = (70, 70, 190)

    # set window size
    screen = pygame.display.set_mode([400, 400])
    # set window title
    pygame.display.set_caption("Tutorial number 3")
    # new surfaces (size)
    surface1 = pygame.Surface((100, 150))
    surface1.fill(red)
    surface2 = pygame.Surface((25, 25))
    surface2.fill(blue)

    # rectangle (x, y, width, height)
    rect1 = pygame.Rect(50, 50, 45, 45)
    rect2 = pygame.Rect(200, 200, 100, 50)

    # exit (quit)
    quit_cond = False

    # timer
    clock = pygame.time.Clock()

    # main loop
    while not quit_cond:
        # check events
        for event in pygame.event.get():
            # detect a QUIT event (window cross)
            if event.type == pygame.QUIT:
                quit_cond = True
            # detect a MOUSE event, click down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # move rect1 10 points in x and y
                rect1 = rect1.move(10, 10)
            # detect a MOUSE event, moving
            elif event.type == pygame.MOUSEMOTION:
                # move rect2 10 points in x and y
                rect2 = rect2.move(-10, -10)

        # 20 frames per second
        clock.tick(20)

        # fill background with a color
        screen.fill(white)

        # draw rectangle
        pygame.draw.rect(screen, red, rect1)
        pygame.draw.rect(screen, blue, rect2)

        # refresh the window
        pygame.display.update()

    # close the window
    pygame.quit()


# Main
main()
