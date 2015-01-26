#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame


def main():
    pygame.init()

    # define colors in RGB
    white = (255, 255, 255)
    red = (200, 20, 50)
    blue = (70, 70, 190)

    # set window size
    screen = pygame.display.set_mode([400, 400])
    # set window title
    pygame.display.set_caption("Tutorial number 6")
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(150, 150)

        # 20 frames per second
        clock.tick(20)

        # fill background with a color
        screen.fill(white)

        # save old position
        (old_posX, old_posY) = (rect1.left, rect1.top)

        # move rectangle by mouse movement
        (rect1.left, rect1.top) = pygame.mouse.get_pos()

        # center the mouse in the rectangle
        rect1.left -= rect1.width / 2
        rect1.top -= rect1.height / 2

        # check collisions
        if rect1.colliderect(rect2):
            (rect1.left, rect1.top) = (old_posX, old_posY)

        # draw rectangle
        pygame.draw.rect(screen, red, rect1)
        pygame.draw.rect(screen, blue, rect2)

        # refresh the window
        pygame.display.update()

    # close the window
    pygame.quit()


# Main
main()
