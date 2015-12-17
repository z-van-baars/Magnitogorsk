import random

mill = {
    'Steel': 0,
    'Pig Iron': 0,
    'Iron Ore': 0,
    'Coal': 0,
    'Blast Furnaces': 1,
    'Smelters': 1,
    'Warehouses': 1,
    'Workers': 100,
    'Rubles': 100
}

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

month = months[0]

year = 1920

game_over = False


class village(object):

    def __init__(self):
        pass


def clear():
    print "\n" * 30


def print_res():
    clear()
    print "Steel: %s" % mill['Steel']
    print "Iron Ore: %s" % mill['Iron Ore']
    print "Pig Iron: %s" % mill['Pig Iron']
    print "Coal: %s" % mill['Coal']
    print "Rubles: %s" % mill['Rubles']
    raw_input("> ")


# calculates the goal for steel and other conditionals for the monthly turn
def demand():
    return random.randint(0, 100) + 10000


# checks production against goal conditions
def production_check():

    if mill['Steel'] >= turn_demand:
        mill['Steel'] -= turn_demand
        print "You live to toil another day!"
        raw_input("The glorious government takes %s tons of your proud Sovistani Steel" % str(turn_demand))
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
def set_pig_iron():

    if mill['Iron Ore'] >= mill['Coal']:
        pig_iron_max = (mill['Iron Ore'] - (mill['Iron Ore'] - mill['Coal']))
    else:
        pig_iron_max = (mill['Coal'] - (mill['Coal'] - mill['Iron Ore']))

        smelters_max = mill['Smelters'] * 100

        if pig_iron_max >= smelters_max:
            pig_iron_max -= (pig_iron_max - smelters_max)
        else:
            pig_iron_max -= (smelters_max - pig_iron_max)
        smelt = 'none'

        while smelt == 'none':
            print "Smelters : %s X 100t" % mill['Smelters']
            print "1t Pig Iron consumes 1t : Iron Ore  and  1t : Coal"
            print "Smelt how much pig iron? (max : %stons)" % pig_iron_max
            smelt = raw_input("> ")
            if smelt > smelters_max or smelt < 0:
                print "Komrade, we cannot produce at that capacity!"
            else:
                print "Very good Komrade, the smelters will produce %stons of Pig Iron this week!"
    return smelt

def set_steel():
    if mill['Pig Iron'] >= mill['Coal']:
        forge_max = (mill['Pig Iron'] - (mill['Pig Iron'] - mill['Coal']))
    else:
        forge_max = (mill['Coal'] - (mill['Coal'] - mill['Pig Iron']))

        forge_max = mill['Blast Furnaces'] * 100

        if steel_max >= forge_max:
            steel_max -= (steel_max - forge_max)
        else:
            steel_max -= (forge_max - steel_max)
        forge = 'none'

        while forge == 'none':
            print "Blast Furnaces : %s X 100t" % mill['Blast Furnaces']
            print "1t Steel consumes 2t : Pig Iron  and  1t : Coal"
            print "Forge how much Steel? (max : %stons)" % steel_max
            forge = raw_input("> ")
            if forge > furnaces_max or forge < 0:
                print "Komrade, we cannot produce at that capacity!"
            else:
                print "Very good Komrade, the smelters will produce %stons of Pig Iron this week!"
    return forge

# parses player input into game actions
def action_choice():
    pass


# alters production parameters for the mill every turn according player input
def production():
    ## extraction
    mill['Iron Ore'] += 100
    mill['Coal'] += 100

    ## production
    steel = mill['Blast Furnaces'] * mill['Pig Iron']
    mill['Pig Iron'] -= steel
    mill['Steel'] += steel
    print_res()



# increments workers resource according to player input

def workers():
    pass


# calculates amount of resources consumed and produced per week
def production_orders():
    clear()
    while set_choice == 'none':
        print "Set orders for what?"

        print "(I)ron Ore // (P)ig Iron // (S)teel "
        set_choice = raw_input("> ")
        if set_choice == "I":
            # create function to set iron ore and coal extraction
            pass
        elif set_choice == "S":
            forge = set_steel()
        elif set_choice == "P":
            smelt = set_pig_iron()
        else:
            print "Sorry Komrade, I don't understand that."
            set_choice == 'none'

        # Need function to make sure production orders don't have resource draw conflicts




print "MAGNITOGORSk!"
print "_" * 20

# game loop - iterates 4 * weekly and 12 * monthly with a weekly, monthly, and yearly incrementer
# calls subfunctions to do production and other game tasks

while game_over == False:
    clear()
    print "ENTER GLORIOUS COMMUNIST YEAR: %s!" % str(year)
    print "\n" * 4
    raw_input("> ")
    clear()
    month = 0
    while month < 11 and game_over == False:

        turn_demand = demand()

        print "The great leader commands you produce %d tons of Steel this month!" % turn_demand
        raw_input("> ")
        for w in range(4):
            action = 'none'
            while action == 'none':
                clear()
                print months[month] + " : " + str(year)
                print "Week: %s" % str(w + 1)
                print_res()
                print "_" * 80
                print "(B)uild // (H)ire and Fire workers // Buy and Sell (R)esources // (S)et production"
                action = raw_input("Do what? > ")
                if action == "I":
                    pass
                elif action == "H":
                    pass
                elif action == "S":
                    production()
                elif action == "B":
                    pass
                elif action == "E":
                    pass
            production()
        raw_input("> ")
        game_over = production_check()
        month += 1
    year += 1
