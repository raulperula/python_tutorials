#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.termcolors import background

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = 200, 200

    def move(self, vel_x, vel_y):
        self.rect.move_ip(vel_x, vel_y)

    def update(self, surface):
        surface.blit(self.image, self.rect)


def main():
    pygame.init()

    # set window size
    screen1 = pygame.display.set_mode([400, 400])

    # clock
    clock1 = pygame.time.Clock()

    # exit (quit)
    quit_cond = False

    image_player = pygame.image.load(
        "../media/images/stick.png").convert_alpha()
    image_bg = pygame.image.load(
        "../media/images/background.png").convert_alpha()

    player1 = Player(image_player)
    vel_x, vel_y = 0, 0
    velocity = 10

    # main loop
    while not quit_cond:
        # check events
        for event in pygame.event.get():
            # detect a QUIT event
            if event.type == pygame.QUIT:
                quit_cond = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vel_x = -velocity
                elif event.key == pygame.K_RIGHT:
                    vel_x = velocity
                elif event.key == pygame.K_UP:
                    vel_y = -velocity
                elif event.key == pygame.K_DOWN:
                    vel_y = velocity
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    vel_x = 0
                elif event.key == pygame.K_RIGHT:
                    vel_x = 0
                elif event.key == pygame.K_UP:
                    vel_y = 0
                elif event.key == pygame.K_DOWN:
                    vel_y = 0

        # update clock
        clock1.tick(20)

        # screen background
        screen1.blit(image_bg, (0, 0))

        # player
        player1.move(vel_x, vel_y)
        player1.update(screen1)

        # refresh the window
        pygame.display.update()

    # close the window
    pygame.quit()


# Main
main()
