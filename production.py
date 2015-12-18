import mill
import random
import string
import utilities


# set amount of pig iron to produce
def set_pig_iron(old_smelt):

    mill.mill['Spent Coal'] -= (old_smelt)
    mill.mill['Spent Iron Ore'] -= (old_smelt)
    mill.mill['Iron Ore'] += (old_smelt)
    mill.mill['Coal'] += (old_smelt)
    smelters_max = min((min(mill.mill['Iron Ore'], mill.mill['Coal'])), (mill.mill['Smelters'] * 100))
    smelt = 'none'
    utilities.clear()
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

    mill.mill['Spent Coal'] -= (2 * old_forge)
    mill.mill['Spent Pig Iron'] -= (2 * old_forge)
    mill.mill['Pig Iron'] += (2 * old_forge)
    mill.mill['Coal'] += (2 * old_forge)
    forge_max = min(min(int(mill.mill['Pig Iron'] / 2), mill.mill['Coal']), (mill.mill['Blast Furnaces'] * 100))

    forge = 'none'
    utilities.clear()
    while forge == 'none':
        utilities.clear()
        print "Blast Furnaces : %s X 100t" % mill.mill['Blast Furnaces']
        print "1t Steel consumes 2t : Pig Iron  and  2t : Coal"
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
    mill.mill['Spent Coal'] += (2 * mill.orders['Forge'])
    mill.mill['Spent Pig Iron'] += (2 * mill.orders['Forge'])
    mill.mill['Pig Iron'] -= (2 * mill.orders['Forge'])
    mill.mill['Coal'] -= (2 * mill.orders['Forge'])


# allows player to assign production
def production_orders():

    utilities.clear()
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
            utilities.clear()


def salary():

    mill.workers['Salary'] = 0
    for worker in mill.wages:
        mill.workers['Salary'] += mill.workers[worker] * mill.wages[worker]


def print_salary():

    utilities.clear()
    for worker in mill.wages:
        print "%d %s working for %d Rubles per week." % (mill.workers[worker], worker, mill.wages[worker])
    raw_input("> ")


# calculates resources consumed and produced every turn
def production():

    # payroll
    mill.mill['Rubles'] -= mill.workers['Salary']

    # extraction
    mill.mill['Iron Ore'] += mill.orders['Extract']
    mill.mill['Coal'] += int(mill.orders['Extract'] * 2)

    # production

    mill.mill['Spent Iron Ore'] = 0
    mill.mill['Spent Pig Iron'] = 0
    mill.mill['Spent Coal'] = 0
    mill.mill['Steel'] += mill.orders['Forge']
    mill.orders['Forge'] = 0
    mill.mill['Pig Iron'] += mill.orders['Smelt']
    mill.orders['Smelt'] = 0

    if mill.mill['Rubles'] < 0:
        mill.mill['Defunct'] = 1
    else:
        pass
