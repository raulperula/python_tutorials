#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raul Perula-Martinez"
__date__ = "2015-01"
__version__ = "$ Revision: 1.0 $"

import pygame

pygame.init()

# set window size
screen = pygame.display.set_mode((480, 500))

# exit (quit)
quit_cond = False

# timer
clock = pygame.time.Clock()

# image
image1 = pygame.image.load("../media/images/stick.png")
(x, y) = (100, 100)
vel_x = 0

rect1 = pygame.Rect(250, 50, 20, 200)

# create new sprite
spr1 = pygame.sprite.Sprite()
spr1.image = image1
spr1.rect = image1.get_rect()
spr1.rect.top = 50
spr1.rect.left = 50

# main loop
while not quit_cond:
    # check events
    for event in pygame.event.get():
        # detect a QUIT event (window cross)
        if event.type == pygame.QUIT:
            quit_cond = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel_x -= 10
            elif event.key == pygame.K_RIGHT:
                vel_x += 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vel_x = 0
            elif event.key == pygame.K_RIGHT:
                vel_x = 0

    # move sprite in velocity
    x += vel_x
    old_x = spr1.rect.left
    spr1.rect.move_ip(vel_x, 0)

    # check collisions
    if spr1.rect.colliderect(rect1):
        # no move if collision
        spr1.rect.left = old_x

    # 20 frames per second
    clock.tick(20)

    # fill background with a color
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), rect1)
    screen.blit(spr1.image, spr1.rect)

    # refresh the window
    pygame.display.update()

# close the window
pygame.quit()
