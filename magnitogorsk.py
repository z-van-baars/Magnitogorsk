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


class village(object):

    def __init__(self):
        pass

# calculates the goal for steel and other conditionals for the monthly turn
def demand():
    return random.randint(0, 100)


# checks production against goal conditions
def production_check():

    if mill['Steel'] >= turn_demand:
        print "You live to toil another day!"
    else:
        print "You have failed the bureaucrats!"

def workers():
    pass

# calculates amount of resources consumed and produced per week
def production():
    pass

print "MAGNITOGORSk!"
print "_" * 20

# game loop - iterates 4 * weekly and 12 * monthly with a weekly, monthly, and yearly incrementer
# calls subfunctions to do production and other game tasks
while True:

    print "ENTER GLORIOUS COMMUNIST YEAR: %s!" % str(year)
    month = 0
    for m in range(12):


        turn_demand = demand()

        print "The great leader commands you produce %d tons of steel this month!" % turn_demand
        for w in range(3):
            print months[month] + " : " + str(year)
            print "_" * 80
            print "Do what?"
            print "(B)uild // (H)ire and Fire workers // Buy and Sell (R)esources // (E)nd turn"
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
        month += 1
    year += 1