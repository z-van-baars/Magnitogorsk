import assets
import random
import mill
import time


def demand():
    demand1 = random.randint(20, 45)
    demand2 = random.randint(20, 45)
    print(mill.mill['Demand'] / 10)
    return ((max(demand1, demand2) * 4) + (mill.mill['Demand'] / 10))

















































#### Old Stuff ###
def clear():
    print("\n" * 50)


def turn_timer():
    for n in range(10):
        time.sleep(0.05)
        clear()
        print(str(n + 1))


def lose():

    print("You have failed the bureaucrats!")
    print("THIS GAME IS OVER.")
    raw_input("")


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


def print_res():

    print("Resource // Available // (Spent This Week) // (Produced This Week)")
    print("_" * 80)
    print("Steel ------ %s tons // (+%s)" % (str(mill.mill['Steel']), str(mill.orders['Forge'])))
    print("Iron Ore --- %s tons // (-%s) // (+%s)" % (str(mill.mill['Iron Ore']), str(mill.orders['Smelt']), str(int(mill.workers['Miners'] * 10))))
    print("Pig Iron --- %s tons // (-%s) // (+%s)" % (str(mill.mill['Pig Iron']), str(mill.orders['Forge'] * 2), str(mill.orders['Smelt'])))
    print("Coal ------- %s tons // (-%s) // (+%s)" % (str(mill.mill['Coal']), str(mill.mill['Spent Coal']), str(int((mill.workers['Miners'] * 20)))))

    print("Rubles ----- %d // (-%d)" % (mill.mill['Rubles'], mill.workers['Salary']))
