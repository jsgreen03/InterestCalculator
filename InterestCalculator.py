
def main():
    while True:
        print("Welcome to a sloppy script that calculates interest for you based on parameters you give!")
        c = getC()
        t = getT()
        r = getR()
        comp = getComp()
        mode = getMode()
        if mode == False:
            output = calculate(c , t , r , comp)
        else:
            output = dCalculate(c , t , r , comp)
        print("Your resulting value is:\n" + str(output) + "\n")




def getC():
    c = input("Please input your starting amount:\n")
    if not isFloat(c):
        print("Don't try to break my fucking program")
        getC()
    return float(c)


def getT():
    t = input("How long (in years) would you like interest to accrue for?\n")
    if not isFloat(t):
        print("Don't try to break my fucking program")
        getT()
    return float(t)


def getR():
    r = input("Please input the nominal interest rate (Decimal):\n")
    if not isFloat(r):
        print("Don't try to break my fucking program")
        getR()
    return float(r)


def getComp():
    comp = input("How frequently would you like interest to compound? (Enter q for quarterly, a for annually, m for monthly)\n")
    if comp not in "aqm":
        print("Don't try to break my fucking program")
        getComp()
    return comp


def getMode():
    mode = input("Would you like to switch into DCA mode? (y/n)\n")
    if mode == "y":
        return True
    if mode == "n":
        return False
    else:
        print("Don't try to break my fucking program")
        getMode()




def calculate(c , t , r ,comp):
    if comp == "q":
        return c*(1+(r/4))**(4*t)
    if comp == "a":
        return c*(1+r)**t
    if comp == "m":
        return c*(1+(r/12))**(12*t)


def dCalculate(c , t , r , comp):
    tot = 0
    if comp == "q":
        n = 4
    elif comp == "a":
        n = 1
    elif comp == "m":
        n = 12
    numTimes = n*t
    time = 1
    while time <= numTimes:
        tot += c/numTimes
        tot = tot*(1+r/n)
        time += 1
    return tot


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
#Interest = C(1+(r/n))^(nt)
#n = number of times compounded per time t
#t = number of years in this case
#r = interest rate
#C = starting value

if __name__ == "__main__":
    main()