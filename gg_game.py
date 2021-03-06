# Glupska grisen
from random import randint
points = []

def rand_dice(n): # generates a random number, remember to put n = 1 when calling
    return randint(n, 6)  # to be able to exclude 1 as a possibility


def one_round():
    total = rand_dice(2)
    print "\nFirst strike: %d" % total
    ans = raw_input("Press ENTER to strike again (anything else to save):\n")
    while ans == "": # loop as long as you want to
        
        n = rand_dice(1) # save return value of one_strike() to n
        if n == 1: # lose if n == 1
            total = 0
            print "You lost. Saving", total
            return 0 # quits the function and returns value 0
        elif n != 1:
            total += n
            print "New total:", total
            ans = raw_input("Press ENTER to strike again (anything else to save):\n")

    return total
        

def save_list(t, points): # called to save the result to list
    print "Adding %d to total sum." % total
    points.append(total)
    s = 0
    #print "You've got %r points" % points
    for count in points:
        #print "Here are your totals: %d" % count
        s += count
    print "Points now: ", points
    print "Overall total: %d\n" % s


i = 0
rounds = int(raw_input("How many rounds? ")) # ask for how many turns to run
points = []
while i < rounds: # runs until specified amount of time
    total = one_round()
    save_list(total, points)
    i += 1

print "You're done, your points are: ", points
s = 0
for count in points:
    s += count
print "You finished with a total of:", s
print "That's great!"