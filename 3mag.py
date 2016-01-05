import pygame
import random


pygame.init()
done = False

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
green = (25, 255, 50)
red = (255, 0, 0)
blue = (0, 0, 255)

key = (255, 0, 128)

size = [800, 600]
screen = pygame.display.set_mode(size)

pygame.mouse.set_visible(1)

game_bg = pygame.image.load("art/ui_bg.png").convert()
menu_bg = pygame.image.load("art/menu_splash.png").convert()
pygame.display.set_caption("magnitogorsk")

main_menu_music = pygame.mixer.Sound("sound/USSR_anthem.ogg")

menu_font = pygame.font.SysFont('Calibri', 30, True, False)


def main_menu():

    quit_text = menu_font.render("Quit Game", True, white)
    new_text = menu_font.render("New Game", True, green)
    menu_item = new_text
    menu_up = True

    while menu_up:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_up = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if menu_item != new_text:
                        menu_item = new_text
                        new_text = menu_font.render("New Game", True, green)
                        quit_text = menu_font.render("Quit Game", True, white)

                if event.key == pygame.K_RIGHT:
                    if menu_item != quit_text:
                        menu_item = quit_text
                        quit_text = menu_font.render("Quit Game", True, green)
                        new_text = menu_font.render("New Game", True, white)

                if event.key == pygame.K_RETURN:
                    menu_up = False

        screen.blit(menu_bg, [0, 0])

        screen.blit(new_text, [100, 500])
        screen.blit(quit_text, [500, 500])
        main_menu_music.play()

        pygame.display.flip()
        clock.tick(60)

    return menu_item

while not done:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    menu_item = main_menu()
    done = True

pygame.quit()
