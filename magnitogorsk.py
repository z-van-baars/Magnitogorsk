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

month = [
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

year = 1920


class village(object):

    def __init__(self):
        pass


def demand():
    return random.randint(0, 100)


def production_check():

    if mill['Steel'] >= turn_demand:
        print "You live to toil another day!"
    else:
        print "You have failed the bureaucrats!"
        break

print "MAGNITOGORSk!"
print "_" * 20

while True:

    year += 1
    turn_demand = demand()
    print "The great leader commands you produce %d tons of steel this month!" % turn_demand
    for w in range(3):
        print "Do what?"
        print "(B)uild // (H)ire workers // (S)ell resources // (B)uy resources // (E)nd turn"
        action = raw_input("Do what?")
        if action == "I":
            pass
        elif action == "H":
            pass
        elif action == "S":
            pass
        elif action == "B":
            pass
    raw_input("> ")