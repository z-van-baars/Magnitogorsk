import assets
import mill
import random
import string
import utilities
import pygame


def extraction():

    choice = 'none'
    utilities.clear()
    a = mill.workers['Miners']
    b = mill.workers['Miners'] * mill.orders['Iron Extract']
    c = mill.workers['Miners'] * mill.orders['Coal Extract']
    print("Current focus:")
    print("_" * 80)
    print("%d Miners extracting %d tons of Iron Ore per week, and %d tons of Coal per week." % (a, b, c))
    print("\n" * 4)
    print("(1) Heavy Iron focus / (2) Moderate Iron Focus / (3) Balanced / (4) Moderate Coal Focus / (5) Heavy Coal Focus")
    print("Change mining focus (6 for No)?")
    choice = raw_input("> ")
    if choice == "1":
        mill.orders['Coal Extract'] = 0
        mill.orders['Iron Extract'] = 30
    elif choice == "2":
        mill.orders['Coal Extract'] = 10
        mill.orders['Iron Extract'] = 20
    elif choice == "3":
        mill.orders['Coal Extract'] = 15
        mill.orders['Iron Extract'] = 15
    elif choice == "4":
        mill.orders['Coal Extract'] = 20
        mill.orders['Iron Extract'] = 10
    elif choice == "5":
        mill.orders['Coal Extract'] = 30
        mill.orders['Iron Extract'] = 0
    elif choice == "6":
        pass
    else:
        choice = 'none'


# set amount of pig iron to produce
def set_pig_iron(old_smelt):

    smelters_max = min((min(mill.mill['Iron Ore'], mill.mill['Coal'])), (mill.workers['Smelters'] * 10))
    smelt_chosen = False

    while smelt == 'none':
        print("Smelters : %s X 10t" % mill.workers['Smelters'])
        print("1t Pig Iron consumes 1t : Iron Ore  and  1t : Coal")
        print("Smelt how much pig iron? (max : %s tons)" % smelters_max)
        smelt = raw_input("> ")
        try:
            smelt = int(smelt)
        except ValueError:
            smelt = (smelters_max + 1)
        if smelt > smelters_max or smelt < 0:
            print("Komrade, we cannot produce at that capacity!")
            smelt = 'none'
        else:
            print("Very good Komrade, the smelters will produce %s tons of Pig Iron this week!" % smelt)
            mill.orders['Smelt'] = smelt
        raw_input("> ")
    mill.mill['Spent Coal'] += (mill.orders['Smelt'])
    mill.mill['Spent Iron Ore'] += (mill.orders['Smelt'])
    mill.mill['Iron Ore'] -= (mill.orders['Smelt'])
    mill.mill['Coal'] -= (mill.orders['Smelt'])


def set_steel():

    from assets import menu_font

    forge_chosen = False
    forge_stamp = menu_font.render(str(mill.orders['Steel']), True, assets.blu_grey)
    coal_stamp = menu_font.render(str(mill.orders['Steel']), True, assets.blu_grey)
    pig_iron_stamp = menu_font.render(str(mill.orders['Pig Iron'] * 2), True, assets.blu_grey)

    change_steel = 0
    change_coal = 0
    change_pig = 0
    while not forge_chosen:
        
        mill.orders['Steel'] += change_steel
        mill.spent['Pig Iron'] -= change_pig
        mill.resources['Pig Iron'] += change_pig
        mill.spent['Coal'] -= change_coal
        mill.resources['Coal'] += change_coal

        if mill.orders['Steel'] < 0:
            mill.orders['Steel'] = 0
        forge_stamp = menu_font.render(str(mill.orders['Steel']), True, assets.blu_grey)
        coal_stamp = menu_font.render(str(mill.orders['Steel']), True, assets.blu_grey)
        pig_iron_stamp = menu_font.render(str(mill.orders['Steel'] * 2), True, assets.blu_grey)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                forge_chosen = True
                mill.mill['Defunct'] = 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if mill.resources['Pig Iron'] > 1 and mill.resources['Coal'] > 0:
                        change_steel = 1
                        change_coal = (-1)
                        change_pig = (-2)
                    elif mill.resources['Pig Iron'] <= 1 and mill.resources['Coal'] <= 0:
                        change_steel = 0
                        change_coal = 0
                        change_pig = 0

                if event.key == pygame.K_DOWN and mill.orders['Steel'] > 0:

                    change_steel = (-1)
                    change_coal = 1
                    change_pig = 2

                if event.key == pygame.K_RETURN:
                    forge_chosen = True
                    assets.click_01.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    change_steel = 0
                    change_coal = 0
                    change_pig = 0
                if event.key == pygame.K_DOWN:
                    change_steel = 0
                    change_coal = 0
                    change_pig = 0


        assets.screen.blit(assets.set_steel_bg, [0, 0])
        assets.screen.blit(forge_stamp, [225, 80])
        assets.screen.blit(coal_stamp, [195, 250])
        assets.screen.blit(pig_iron_stamp, [195, 330])
        pygame.display.flip()
        assets.clock.tick(10)


# allows player to assign production
def production_orders():

    prod_chosen = False
    pointer_pos = 0
    pointer_locs = [[80, 175], [80, 250], [80, 335], [80, 425]]
    while not prod_chosen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                prod_chosen = True
                mill.mill['Defunct'] = 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and pointer_pos > 0:
                    pointer_pos -= 1
                if event.key == pygame.K_DOWN and pointer_pos < 3:
                    pointer_pos += 1
                if event.key == pygame.K_RETURN:
                    prod_chosen = True
                    assets.click_01.play()

        # print("%s tons of Iron Ore will be produced this turn" % (mill.workers['Miners'] * mill.orders['Iron Extract']))
        # print("%s tons of Coal will be produced this turn" % (mill.workers['Miners'] * mill.orders['Coal Extract']))
        # print("\n")
        # print("%s tons of Pig Iron will be produced this turn" % mill.orders['Smelt'])
        # print("\tconsuming %s tons of Iron Ore and %s tons of Coal" % (mill.orders['Smelt'], mill.orders['Smelt']))
        # print("\n")
        # print("%s tons of Steel will be produced this turn" % mill.orders['Forge'])
        # print("\tconsuming %s tons of Pig Iron and %s tons of Coal" % ((mill.orders['Forge'] * 2), mill.orders['Forge']))
        # print("\nSet orders for what?")
        # print("(I)ron and Coal Extraction // (P)ig Iron Smelting // (S)teel Forging")
        # set_choice = raw_input("> ")
        # set_choice = string.lower(set_choice)

        assets.screen.blit(assets.production_menu, [0, 0])
        assets.screen.blit(assets.pointer, pointer_locs[pointer_pos])
        pygame.display.flip()
        assets.clock.tick(20)

    if pointer_pos == 0:
        extraction()
    if pointer_pos == 2:
        set_steel()
    if pointer_pos == 1:
        set_pig_iron((mill.orders['Pig Iron']))


# calculates resourcs consumed and produced every turn
def production():

    # payroll
    mill.resources['Rubles'] -= mill.spent['Rubles']

    # extraction
    mill.resources['Iron Ore'] += int(mill.workers['Miners'] * mill.orders['Iron Ore'])
    mill.resources['Coal'] += int(mill.workers['Miners'] * mill.orders['Coal'])

    # production
    mill.resources['Pig Iron'] += mill.orders['Pig Iron']
    mill.resources['Steel'] += mill.orders['Steel']

    mill.spent['Iron Ore'] = 0
    mill.spent['Pig Iron'] = 0
    mill.spent['Coal'] = 0
    mill.orders['Steel'] = 0
    mill.orders['Smelt'] = 0

    if mill.resources['Rubles'] < 0:
        mill.mill['Defunct'] = 1
