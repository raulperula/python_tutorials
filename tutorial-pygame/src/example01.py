#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame


def main():
    pygame.init()

    # set window size
    pygame.display.set_mode([300, 300])
    # set window title
    pygame.display.set_caption("Tutorial number 1")

    # exit (quit)
    q = False

    # main loop
    while not q:
        # check events
        for event in pygame.event.get():
            # detect a QUIT event
            if event.type == pygame.QUIT:
                q = True

        # refresh the window
        pygame.display.update()

    # close the window
    pygame.quit()


# Main
main()
