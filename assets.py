import pygame

pygame.init()

clock = pygame.time.Clock()

main_menu_music = pygame.mixer.Sound("sound/USSR_anthem.ogg")

menu_font = pygame.font.SysFont('Calibri', 30, True, False)
year_font = pygame.font.SysFont('Calibri', 40, True, False)

black = (0, 0, 0)
white = (255, 255, 255)
green = (25, 255, 50)
red = (255, 0, 0)
blue = (0, 0, 255)
gold = (205, 155, 13)
gray = (64, 83, 97)

key = (255, 0, 128)

size = [800, 600]
screen = pygame.display.set_mode(size)

year_splash = pygame.image.load("art/yearsplash.png").convert()
demand_splash = pygame.image.load("art/demand_splash.png").convert()
game_bg = pygame.image.load("art/ui_bg.png").convert()
menu_bg = pygame.image.load("art/menu_splash.png").convert()
factory_bg = pygame.image.load("art/factory_ui.png").convert()
box_bg = pygame.image.load("art/box_bg.png").convert()
resource_screen = pygame.image.load("art/resources_ui.png").convert()
pipes_bg = pygame.image.load("art/pipes.png").convert()
workers_bg = pygame.image.load("art/workers_bg.png").convert()
lose_splash = pygame.image.load("art/lose_splash.png").convert()
lavatrain = pygame.image.load("art/lavatrain.png").convert()
pointer = pygame.image.load("art/pointer.png").convert()

pointer.set_colorkey(key)
