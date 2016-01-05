import pygame
import random
import assets

pygame.init()
done = False

clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
pygame.display.set_caption("magnitogorsk")

main_menu_music = pygame.mixer.Sound("sound/USSR_anthem.ogg")

menu_font = pygame.font.SysFont('Calibri', 30, True, False)


def main_menu():

    quit_text = menu_font.render("Quit Game", True, assets.white)
    new_text = menu_font.render("New Game", True, assets.green)
    menu_item = "New"
    menu_up = True

    while menu_up:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_up = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if menu_item != new_text:
                        menu_item = "New"
                        new_text = menu_font.render("New Game", True, assets.green)
                        quit_text = menu_font.render("Quit Game", True, assets.white)

                if event.key == pygame.K_RIGHT:
                    if menu_item != quit_text:
                        menu_item = "Quit"
                        quit_text = menu_font.render("Quit Game", True, assets.green)
                        new_text = menu_font.render("New Game", True, assets.white)

                if event.key == pygame.K_RETURN:
                    menu_up = False

        assets.screen.blit(assets.menu_bg, [0, 0])

        assets.screen.blit(new_text, [100, 500])
        assets.screen.blit(quit_text, [500, 500])
        main_menu_music.play()

        pygame.display.flip()
        clock.tick(60)

    return menu_item

while not done:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    menu_item = main_menu()
    while menu_item == "New":
        pass
    done = True

pygame.quit()
