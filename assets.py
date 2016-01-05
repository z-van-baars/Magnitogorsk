import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (25, 255, 50)
red = (255, 0, 0)
blue = (0, 0, 255)

key = (255, 0, 128)

size = [800, 600]
screen = pygame.display.set_mode(size)

game_bg = pygame.image.load("art/ui_bg.png").convert()
menu_bg = pygame.image.load("art/menu_splash.png").convert()
factory_bg = pygame.image.load("art/factory_bg.png").convert()
box_bg = pygame.image.load("art/box_bg.png").convert()
pipes_bg = pygame.image.load("art/pipes.png").convert()
workers_bg = pygame.image.load("art/workers_bg.png").convert()
lavatrain = pygame.image.load("art/lavatrain.png").convert()

