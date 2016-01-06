import pygame
import random
import assets
import mill
import utilities


pygame.init()
done = False

pygame.mouse.set_visible(1)
pygame.display.set_caption("magnitogorsk")


def main_menu():

    quit_text_g = assets.menu_font.render("Quit Game", True, assets.gold)
    quit_text_w = assets.menu_font.render("Quit Game", True, assets.white)
    new_text_g = assets.menu_font.render("New Game", True, assets.gold)
    new_text_w = assets.menu_font.render("New Game", True, assets.white)

    new_text = new_text_g
    quit_text = quit_text_w

    menu_item = "New"
    menu_up = True

    while menu_up:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_up = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if menu_item != "New":
                        menu_item = "New"
                        mill.mill['Defunct'] = 0
                        new_text = new_text_g
                        quit_text = quit_text_w

                if event.key == pygame.K_RIGHT:
                    if menu_item != "Quit":
                        menu_item = "Quit"
                        mill.mill['Defunct'] = 2
                        quit_text = quit_text_g
                        new_text = new_text_w

                if event.key == pygame.K_RETURN:
                    menu_up = False

        assets.screen.blit(assets.menu_bg, [0, 0])

        assets.screen.blit(new_text, [100, 500])
        assets.screen.blit(quit_text, [500, 500])
        # assets.main_menu_music.play()

        pygame.display.flip()
        assets.clock.tick(20)

    return menu_item


def month_loop():
    month = 0
    while month < 11 and mill.mill['Defunct'] == 0:

        mill.mill['Demand'] = utilities.demand()

        utilities.demand_splash(mill.mill['Demand'])

        week = 1

        while week < 5:
            turn_over = False
            while not turn_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        action = "Quit"
                        mill.mill['Defunct'] = 2

                pointer_locs = [[25, 550], [147, 550], [315, 550], [475, 550], [655, 550], [655, 450]]
                pointer_pos = 0
                action = 'none'
                while action == 'none':
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            action = "Quit"
                            mill.mill['Defunct'] = 2
                            week += 5
                            turn_over = True

                        if event.type == pygame.KEYDOWN:

                            if event.key == pygame.K_LEFT:
                                pointer_pos -= 1
                                if pointer_pos < 0:
                                    pointer_pos = 0
                            if event.key == pygame.K_RIGHT:
                                pointer_pos += 1
                                if pointer_pos > 4:
                                    pointer_pos = 4
                            if event.key == pygame.K_RETURN:
                                action = pointer_pos

                    print(pointer_pos)
                    month_stamp = assets.year_font.render(str(mill.months[month]), True, assets.gray)
                    quota_stamp = assets.year_font.render(str(mill.mill['Demand']), True, assets.gray)
                    year_stamp = assets.year_font.render(str(mill.mill['Year']), True, assets.gray)
                    assets.screen.blit(assets.factory_bg, [0, 0])
                    assets.screen.blit(month_stamp, [10, 8])
                    assets.screen.blit(year_stamp, [252, 8])
                    assets.screen.blit(quota_stamp, [700, 8])
                    assets.screen.blit(assets.pointer, pointer_locs[pointer_pos])
                    pygame.display.flip()
                    assets.clock.tick(20)

                if action == 0:
                    print("BUILD")
                if action == 1:
                    print("PERSONNEL")
                    # workers()
                    # personnel
                if action == 2:
                    print("RESOURCES")
                    utilities.salary()
                    utilities.print_res()
                    # resources
                if action == 3:
                    print("PRODUCTION")
                    # production
                    # production.production_orders()
                if action == 4:
                    print("END TURN")
                    turn_over = True
                    # end turn
                if action == 5:
                    print("QUIT")
                    turn_over = True
                    week += 5

                
                # print("Week: %s" % str(w + 1))
                
                # production.salary()
                # utilities.print_res()
                # action = raw_input("Do what? > ")
                # action = string.lower(action)
                # if action == "r" or action == "resources":
                #     action = 'none'
                # elif action == "p" or action == "personnel":
                #     workers()
                #     action = 'none'
                # elif action == "m" or action == "production":
                #     production.production_orders()
                #     action = 'none'
                # elif action == "b" or action == "build":
                #     build()
                #     action = 'none'
                # elif action == "e" or action == "end":
                #     pass
            # production.production()
            # utilities.turn_timer()
            week += 1
        # utilities.production_check()
        month += 1


def game_loop():

    while mill.mill['Defunct'] == 0:

        year_stamp = assets.year_font.render(str(mill.mill['Year']), True, assets.gold)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_item = "Quit"
        year_disp = True
        while year_disp:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        year_disp = False

            assets.screen.blit(assets.year_splash, [0, 0])
            assets.screen.blit(year_stamp, [425, 150])
            pygame.display.flip()
            assets.clock.tick(20)

        month_loop()
        mill.mill['Year'] += 1

    if mill.mill['Defunct'] == 1:
        utilities.lose()



        # mill.mill['Year'] += 1



while not done:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    main_menu()
    game_loop()

    done = True

pygame.quit()
