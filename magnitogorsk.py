import random
import string
import mill
import utilities
import production


# increments workers resource according to player input
def workers():

    choice = 'none'
    while choice == 'none':
        production.print_salary()
        print "_" * 80
        print "Hire New Workers?"
        choice = raw_input("> ")
        if choice == "y":
            pass
        elif choice == "n":
            pass
        else:
            print "Sorry Komrade, I don't understand that."
            raw_input("")
            choice = 'none'



# iterates 4 * weekly and 12 * monthly
# weekly, monthly, and yearly incrementer
# calls subfunctions to do production and other game tasks
def month_loop():
    month = 0
    while month < 11 and mill.mill['Defunct'] == 0:

        mill.mill['Demand'] = utilities.demand()

        print "The great leader commands you produce %s tons of Steel this month!" % str(mill.mill['Demand'])

        raw_input("> ")

        for w in range(4):
            action = 'none'
            while action == 'none':
                utilities.clear()
                print mill.months[month] + " : " + str(mill.mill['Year']) + " - - - - - - - - - " + "Quota: " + str(mill.mill['Demand'])
                print "Week: %s" % str(w + 1)
                print "\n" * 4
                production.salary()
                utilities.print_res()
                print "_" * 80
                print "(B)uild // Manage (P)ersonnel // Buy and Sell (R)esources // (M)anage production // (E)nd Turn"
                action = raw_input("Do what? > ")
                action = string.lower(action)
                if action == "r" or action == "resources":
                    action = 'none'
                elif action == "p" or action == "personnel":
                    workers()
                    action = 'none'
                elif action == "m" or action == "production":
                    production.production_orders()
                    action = 'none'
                elif action == "b" or action == "build":
                    build()
                    action = 'none'
                elif action == "e" or action == "end":
                    pass
                else:
                    print "Sorry Komrade, I don't understand that."
                    raw_input("> ")
                    action = 'none'
            production.production()
            utilities.turn_timer()
        utilities.production_check()
        month += 1


def game_loop():
    while mill.mill['Defunct'] == 0:
        utilities.clear()
        print "ENTER GLORIOUS COMMUNIST YEAR: %s!" % str(mill.mill['Year'])
        print " ~~{~~{ Long Live SOVIET SOVISTAN! }~~}~~"
        print "\n" * 4
        raw_input("> ")
        utilities.clear()
        month_loop()
        mill.mill['Year'] += 1
        utilities.lose()

print "MAGNITOGORSk!"
print "_" * 20

game_loop()

