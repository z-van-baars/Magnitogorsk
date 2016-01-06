import assets
import random
import pygame
import mill
import time


def demand():
    demand1 = random.randint(20, 45)
    demand2 = random.randint(20, 45)
    return round((max(demand1, demand2) * 4) + (mill.mill['Demand'] / 10))


def demand_splash(demand):
    demand_stamp = assets.year_font.render(str(mill.mill['Demand']), True, assets.white)
    demand_disp = True
    while demand_disp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                demand_disp = False
                mill.mill['Defunct'] = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    assets.click_01.play()
                    demand_disp = False

        assets.screen.blit(assets.demand_splash, [0, 0])
        assets.screen.blit(demand_stamp, [380, 85])
        pygame.display.flip()
        assets.clock.tick(20)
        pos = pygame.mouse.get_pos()
        print(pos)


def print_res():

    res_xpos = {
        'Rubles': 95,
        'Steel': 500,
        'Coal': 160,
        'Iron Ore': 250,
        'Pig Iron': 330,
    }

    current_stamp = {}
    alloc_stamp = {}
    prod_stamp = {}

    for res_kind in res_xpos:
        current_stamp[res_kind] = menu_font.render(str(mill.workers[stat_kind]), True, assets.black)
        wage_stamp[res_kind] = menu_font.render(str(mill.wages[stat_kind]), True, assets.black)
        total_stamp[res_kind] = menu_font.render(str(mill.workers[stat_kind] * mill.wages[stat_kind]), True, assets.black)

    total_wages_stamp = menu_font.render(str(mill.workers['Salary']), True, assets.gold)

    while disp_wages:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    disp_wages = False
        assets.screen.blit(assets.wages_bg, [0, 0])

        for stat_kind in stat_xpos:
            assets.screen.blit(num_stamp[stat_kind], [195, stat_xpos[stat_kind]])
            assets.screen.blit(wage_stamp[stat_kind], [375, stat_xpos[stat_kind]])
            assets.screen.blit(total_stamp[stat_kind], [630, stat_xpos[stat_kind]])



        pygame.display.flip()
        assets.clock.tick(20)

 # old code
    current_steel_stamp = assets.menu_font.render(str(mill.mill['Steel']), True, assets.black)
    current_iron_ore_stamp = assets.menu_font.render(str(mill.mill['Iron Ore']), True, assets.black)
    current_coal_stamp = assets.menu_font.render(str(mill.mill['Coal']), True, assets.black)
    current_rubles_stamp = assets.menu_font.render(str(mill.mill['Rubles']), True, assets.black)
    current_pig_iron_stamp = assets.menu_font.render(str(mill.mill['Pig Iron']), True, assets.black)

    alloc_steel_stamp = assets.menu_font.render("N/A", True, assets.black)
    alloc_iron_ore_stamp = assets.menu_font.render(str(mill.orders['Smelt']), True, assets.black)
    alloc_coal_stamp = assets.menu_font.render(str(mill.mill['Spent Coal']), True, assets.black)
    alloc_rubles_stamp = assets.menu_font.render(str(mill.workers['Salary']), True, assets.black)
    alloc_pig_iron_stamp = assets.menu_font.render(str(mill.orders['Forge'] * 2), True, assets.black)

    prod_steel_stamp = assets.menu_font.render(str(mill.orders['Forge']), True, assets.black)
    prod_iron_ore_stamp = assets.menu_font.render(str(int(mill.workers['Miners'] * 10)), True, assets.black)
    prod_coal_stamp = assets.menu_font.render(str(int(mill.workers['Miners'] * 20)), True, assets.black)
    prod_rubles_stamp = assets.menu_font.render("N/A", True, assets.black)
    prod_pig_iron_stamp = assets.menu_font.render(str(mill.orders['Forge'] * 2), True, assets.black)

    resource_look = True
    while resource_look:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    resource_look = False

        assets.screen.blit(assets.resource_screen, [0, 0])

        # current
        assets.screen.blit(current_rubles_stamp, [195, 95])
        assets.screen.blit(current_coal_stamp, [195, 160])
        assets.screen.blit(current_iron_ore_stamp, [195, 250])
        assets.screen.blit(current_pig_iron_stamp, [195, 330])
        assets.screen.blit(current_steel_stamp, [195, 500])

        # allocated
        assets.screen.blit(alloc_rubles_stamp, [375, 95])
        assets.screen.blit(alloc_coal_stamp, [375, 160])
        assets.screen.blit(alloc_iron_ore_stamp, [375, 250])
        assets.screen.blit(alloc_pig_iron_stamp, [375, 330])
        assets.screen.blit(alloc_steel_stamp, [375, 500])

        # to be produced
        assets.screen.blit(prod_rubles_stamp, [630, 95])
        assets.screen.blit(prod_coal_stamp, [630, 160])
        assets.screen.blit(prod_iron_ore_stamp, [630, 250])
        assets.screen.blit(prod_pig_iron_stamp, [630, 330])
        assets.screen.blit(prod_steel_stamp, [630, 500])

        pygame.display.flip()
        assets.clock.tick(20)


def lose():

    for i in range(100):

        assets.screen.blit(assets.lose_splash, [0, 0])
        pygame.display.flip()
        assets.clock.tick(20)


# for debugging
def show_mouse():
    pos = pygame.mouse.get_mouse()
    print(pos)


def print_salary():

    from assets import menu_font

    disp_wages = True
    salary()

    stat_xpos = {
        'Untrained': 95,
        'Clerks': 175,
        'Miners': 250,
        'Smelters': 330,
        'Forgers': 420,
    }

    num_stamp = {}
    wage_stamp = {}
    total_stamp = {}

    for stat_kind in stat_xpos:
        num_stamp[stat_kind] = menu_font.render(str(mill.workers[stat_kind]), True, assets.black)
        wage_stamp[stat_kind] = menu_font.render(str(mill.wages[stat_kind]), True, assets.black)
        total_stamp[stat_kind] = menu_font.render(str(mill.workers[stat_kind] * mill.wages[stat_kind]), True, assets.black)

    total_wages_stamp = menu_font.render(str(mill.workers['Salary']), True, assets.gold)

    while disp_wages:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    disp_wages = False
        assets.screen.blit(assets.wages_bg, [0, 0])

        for stat_kind in stat_xpos:
            assets.screen.blit(num_stamp[stat_kind], [195, stat_xpos[stat_kind]])
            assets.screen.blit(wage_stamp[stat_kind], [375, stat_xpos[stat_kind]])
            assets.screen.blit(total_stamp[stat_kind], [630, stat_xpos[stat_kind]])

        # total wages
        assets.screen.blit(total_wages_stamp, [654, 510])

        pygame.display.flip()
        assets.clock.tick(20)


def salary():

    mill.workers['Salary'] = 0
    for worker in mill.wages:
        mill.workers['Salary'] += mill.workers[worker] * mill.wages[worker]







































#### Old Stuff ###
def turn_timer():
    for n in range(10):
        time.sleep(0.05)
        clear()
        print(str(n + 1))


# calculates the goal for steel and other conditionals for the monthly turn



# checks production against goal conditions
def production_check():

    if mill.mill['Steel'] >= mill.mill['Demand']:
        print("You live to toil another day!")
        print("The glorious government takes %s tons of your proud Sovistani Steel" % str(mill.mill['Demand']))
        raw_input("You receive %d Rubles for meeting your quota." % (mill.mill['Demand'] * 100 + 500))
        mill.mill['Rubles'] += (mill.mill['Demand'] * 100 + 500)
        mill.mill['Steel'] -= mill.mill['Demand']
        print_res()
        mill.mill['Defunct'] = 0
    else:
        mill.mill['Defunct'] = 1


