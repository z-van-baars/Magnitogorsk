import random
import string
import mill


class village(object):

    def __init__(self):
        pass


def clear():
    print "\n" * 30


def print_res():

    print "Resource // Available // (Spent This Turn) // (Produced Next Turn)"
    print "_" * 80
    print "Steel ------ %s tons // (+%s)" % (str(mill.mill['Steel']), str(mill.orders['Forge']))
    print "Iron Ore --- %s tons // (-%s) // (+%s)" % (str(mill.mill['Iron Ore']), str(mill.orders['Smelt']), str(mill.orders['Extract']))
    print "Pig Iron --- %s tons // (-%s) // (+%s)" % (str(mill.mill['Pig Iron']), str(mill.orders['Forge'] * 2), str(mill.orders['Smelt']))
    print "Coal ------- %s tons // (-%s) // (+%s)" % (str(mill.mill['Coal']), str(mill.mill['Spent Coal']), str(int((mill.orders['Extract'] * 1.5))))

    print "Rubles: %s" % mill.mill['Rubles']


# calculates the goal for steel and other conditionals for the monthly turn
def demand():
    demand1 = random.randint(20, 45)
    demand2 = random.randint(20, 45)
    print mill.mill['Demand'] / 10
    return ((max(demand1, demand2) * 4) + (mill.mill['Demand'] / 10))


# checks production against goal conditions
def production_check():

    if mill.mill['Steel'] >= mill.mill['Demand']:
        print "You live to toil another day!"
        print "The glorious government takes %s tons of your proud Sovistani Steel" % str(mill.mill['Demand'])
        raw_input("You receive %d Rubles for meeting your quota." % (mill.mill['Demand'] * 100 + 500))
        mill.mill['Rubles'] += (mill.mill['Demand'] * 100 + 500)
        mill.mill['Steel'] -= mill.mill['Demand']
        print_res()
        return False
    else:
        print "You have failed the bureaucrats!"
        print "THIS GAME IS OVER."
        raw_input("")
        print "Long Live SOVIET SOVISTAN!"
        raw_input("")
        return True


# set amount of pig iron to produce
def set_pig_iron(old_smelt):

    mill.mill['Spent Coal'] -= (old_smelt)
    mill.mill['Spent Iron Ore'] -= (old_smelt)
    mill.mill['Iron Ore'] += (old_smelt)
    mill.mill['Coal'] += (old_smelt)
    smelters_max = min((min(mill.mill['Iron Ore'], mill.mill['Coal'])), (mill.mill['Smelters'] * 100))
    smelt = 'none'
    clear()
    while smelt == 'none':
        print "Smelters : %s X 100t" % mill.mill['Smelters']
        print "1t Pig Iron consumes 1t : Iron Ore  and  1t : Coal"
        print "Smelt how much pig iron? (max : %s tons)" % smelters_max
        smelt = raw_input("> ")
        try:
            smelt = int(smelt)
        except ValueError:
            smelt = (smelters_max + 1)
        if smelt > smelters_max or smelt < 0:
            print "Komrade, we cannot produce at that capacity!"
            smelt = 'none'
        else:
            print "Very good Komrade, the smelters will produce %s tons of Pig Iron this week!" % smelt
            mill.orders['Smelt'] = smelt
        raw_input("> ")
    mill.mill['Spent Coal'] += (mill.orders['Smelt'])
    mill.mill['Spent Iron Ore'] += (mill.orders['Smelt'])
    mill.mill['Iron Ore'] -= (mill.orders['Smelt'])
    mill.mill['Coal'] -= (mill.orders['Smelt'])


def set_steel(old_forge):

    mill.mill['Spent Coal'] -= (old_forge)
    mill.mill['Spent Pig Iron'] -= (2 * old_forge)
    mill.mill['Pig Iron'] += (2 * old_forge)
    mill.mill['Coal'] += (old_forge)
    forge_max = min(min(int(mill.mill['Pig Iron'] / 2), mill.mill['Coal']), (mill.mill['Blast Furnaces'] * 100))

    forge = 'none'
    clear()
    while forge == 'none':
        clear()
        print "Blast Furnaces : %s X 100t" % mill.mill['Blast Furnaces']
        print "1t Steel consumes 2t : Pig Iron  and  1t : Coal"
        print "Forge how much Steel? (max : %s tons)" % forge_max
        forge = raw_input("> ")
        try:
            forge = int(forge)
        except ValueError:
            forge = (forge_max + 1)
        if forge > forge_max or forge < 0:
            print "Komrade, we cannot produce at that capacity!"
            forge = 'none'
        elif forge <= forge_max and forge >= 0:
            print "Very good Komrade, the Furnaces will produce %s tons of Steel this week!" % forge
            mill.orders['Forge'] = forge
        raw_input("> ")
    mill.mill['Spent Coal'] += (mill.orders['Forge'])
    mill.mill['Spent Pig Iron'] += (2 * mill.orders['Forge'])
    mill.mill['Pig Iron'] -= (2 * mill.orders['Forge'])
    mill.mill['Coal'] -= (mill.orders['Forge'])


# parses player input into game actions


def action_choice():
    pass


# calculates resources consumed and produced every turn

def production():

    # extraction
    mill.mill['Iron Ore'] += mill.orders['Extract']
    mill.mill['Coal'] += int(mill.orders['Extract'] * 1.5)

    # production

    mill.mill['Spent Iron Ore'] = 0
    mill.mill['Spent Pig Iron'] = 0
    mill.mill['Spent Coal'] = 0
    mill.mill['Steel'] += mill.orders['Forge']
    mill.orders['Forge'] = 0
    mill.mill['Pig Iron'] += mill.orders['Smelt']
    mill.orders['Smelt'] = 0

# increments workers resource according to player input

def workers():
    pass


# allows player to assign production
def production_orders():

    clear()
    set_choice = 'none'
    while set_choice == 'none':

        print "%stons of Iron Ore will be produced this turn" % mill.orders['Extract']
        print "\n"
        print "%stons of Pig Iron will be produced this turn" % mill.orders['Smelt']
        print "\tconsuming %s tons of Iron Ore and %s tons of Coal" % (mill.orders['Smelt'], mill.orders['Smelt'])
        print "\n"
        print "%stons of Steel will be produced this turn" % mill.orders['Forge']
        print "\tconsuming %s tons of Pig Iron and %s tons of Coal" % ((mill.orders['Forge'] * 2), mill.orders['Forge'])
        print "\nSet orders for what?"
        print "(I)ron Ore // (P)ig Iron // (S)teel "
        set_choice = raw_input("> ")
        set_choice = string.lower(set_choice)
        if set_choice == "i":
            # create function to set iron ore and coal extraction
            pass
        elif set_choice == "s":
            set_steel((mill.orders['Forge']))
        elif set_choice == "p":
            set_pig_iron((mill.orders['Smelt']))
        else:
            print "Sorry Komrade, I don't understand that."
            raw_input("> ")
            set_choice = 'none'
            clear()

        # Need function to make sure production orders don't have resource draw conflicts


def month_loop():
    month = 0
    while month < 11:

        mill.mill['Demand'] = demand()

        print "The great leader commands you produce %s tons of Steel this month!" % str(mill.mill['Demand'])
        
        raw_input("> ")

        for w in range(4):
            action = 'none'
            while action == 'none':
                clear()
                print mill.months[month] + " : " + str(mill.mill['Year']) + " - - - - - - - - - " + "Quota: " + str(mill.mill['Demand'])
                print "Week: %s" % str(w + 1)
                print "\n" * 4
                print_res()
                print "_" * 80
                print "(B)uild // (H)ire and Fire workers // Buy and Sell (R)esources // (M)anage production // (E)nd Turn"
                action = raw_input("Do what? > ")
                action = string.lower(action)
                if action == "r" or action == "resources":
                    pass
                elif action == "h" or action == "hire":
                    pass
                elif action == "m" or action == "manage":
                    production_orders()
                    action = 'none'
                elif action == "b" or action == "build":
                    pass
                elif action == "e" or action == "end":
                    pass
                else:
                    print "Sorry Komrade, I don't understand that."
                    raw_input("> ")
                    action = 'none'
            production()
        raw_input("> ")
        game_over = production_check()
        month += 1
    return game_over


# game loop - iterates 4 * weekly and 12 * monthly with a weekly, monthly, and yearly incrementer
# calls subfunctions to do production and other game tasks
def game_loop():
    game_over = False
    while game_over == False:
        clear()
        print "ENTER GLORIOUS COMMUNIST YEAR: %s!" % str(mill.mill['Year'])
        print "\n" * 4
        raw_input("> ")
        clear()
        game_over = month_loop()
        mill.mill['Year'] += 1

print "MAGNITOGORSk!"
print "_" * 20

game_loop()

