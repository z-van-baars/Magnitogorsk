import random
import mill


class village(object):

    def __init__(self):
        pass


def clear():
    print "\n" * 30


def print_res():

    print "Steel ------ %s tons - (+%s)" % (str(mill.mill['Steel']), str(mill.orders['Forge']))
    print "Iron Ore --- %s tons - (+%s)" % (str(mill.mill['Iron Ore']), str(mill.orders['Extract']))
    print "Pig Iron --- %s tons - (+%s)" % (str(mill.mill['Pig Iron']), str(mill.orders['Smelt']))
    print "Coal ------- %s tons - (-%s, +%s)" % (str(mill.mill['Coal']), str(mill.mill['Spent Coal']), str(mill.orders['Extract']))

    print "Rubles: %s" % mill.mill['Rubles']


# calculates the goal for steel and other conditionals for the monthly turn
def demand():
    return random.randint(0, 100) + 10000


# checks production against goal conditions
def production_check():

    if mill.mill['Steel'] >= mill.mill['Demand']:
        mill.mill['Steel'] -= mill.mill['Demand']
        print "You live to toil another day!"
        raw_input("The glorious government takes %s tons of your proud Sovistani Steel" % str(mill.mill['Demand']))
        print_res()
        return False
    else:
        print "You have failed the bureaucrats!"
        print "THIS GAME IS OVER."
        raw_input("")
        print "Long Live SOVIET SOVISTAN!"
        raw_input("")


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
        print "Smelt how much pig iron? (max : %stons)" % smelters_max
        smelt = raw_input("> ")
        if smelt > smelters_max or smelt < 0:
            print "Komrade, we cannot produce at that capacity!"
            smelt = 'none'
        else:
            print "Very good Komrade, the smelters will produce %stons of Pig Iron this week!" % smelt
        raw_input("> ")
    mill.mill['Spent Coal'] += (smelt)
    mill.mill['Spent Iron Ore'] += (smelt)
    mill.mill['Iron Ore'] += (smelt)
    mill.mill['Coal'] += (smelt)
    return smelt


def set_steel(old_forge):

    mill.mill['Spent Coal'] -= (old_forge)
    mill.mill['Spent Pig Iron'] -= (old_forge)
    mill.mill['Pig Iron'] += (old_forge)
    mill.mill['Coal'] += (2 * old_forge)
    forge_max = min(min(mill.mill['Pig Iron'], int(mill.mill['Coal'] / 2)), (mill.mill['Blast Furnaces'] * 100))

    forge = 'none'
    clear()
    while forge == 'none':
        clear()
        print "Blast Furnaces : %s X 100t" % mill.mill['Blast Furnaces']
        print "1t Steel consumes 2t : Pig Iron  and  1t : Coal"
        print "Forge how much Steel? (max : %stons)" % forge_max
        forge = raw_input("> ")
        if forge > forge_max or forge < 0:
            print "Komrade, we cannot produce at that capacity!"
            forge = 'none'
        else:
            print "Very good Komrade, the smelters will produce %stons of Pig Iron this week!" % forge
        raw_input("> ")
    mill.mill['Spent Coal'] += (forge)
    mill.mill['Spent Pig Iron'] += (forge)
    mill.mill['Pig Iron'] += (forge)
    mill.mill['Coal'] += (2 * forge)
    return forge


# parses player input into game actions


def action_choice():
    pass


# calculates resources consumed and produced every turn

def production():
    pass
    # extraction

    # production


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
        print "\tconsuming %s tons of Pig Iron and %s tons of Coal" % (mill.orders['Forge'], (mill.orders['Forge'] * 2))
        print "\nSet orders for what?"
        print "(I)ron Ore // (P)ig Iron // (S)teel "
        set_choice = raw_input("> ")
        if set_choice == "I":
            # create function to set iron ore and coal extraction
            pass
        elif set_choice == "S":
            mill.orders['Forge'] = set_steel((mill.orders['Forge']))
        elif set_choice == "P":
            mill.orders['Smelt'] = set_pig_iron((mill.orders['Smelt']))
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
                print mill.months[month] + " : " + str(mill.mill['Year'])
                print "Week: %s" % str(w + 1)
                print "\n" * 4
                print_res()
                print "_" * 80
                print "(B)uild // (H)ire and Fire workers // Buy and Sell (R)esources // (S)et production"
                action = raw_input("Do what? > ")
                if action == "I":
                    pass
                elif action == "H":
                    pass
                elif action == "S":
                    production_orders()
                elif action == "B":
                    pass
                elif action == "E":
                    pass
            production()
        raw_input("> ")
        game_over = production_check()
        month += 1


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
        month_loop()
        mill.mill['Year'] += 1

print "MAGNITOGORSk!"
print "_" * 20

game_loop()

