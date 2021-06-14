
def main():
    while True:
        print("Welcome to a sloppy script that calculates interest for you based on parameters you give!")
        c = getC()
        t = getT()
        r = getR()
        comp = getComp()
        output = calculate(c , t , r , comp)
        print("Your resulting value is:\n" + str(output) + "\n")




def getC():
    c = input("Please input your starting amount:\n")
    if not(str(c).isdigit()):
        print("Don't try to break my fucking program")
        getC()
    return float(c)


def getT():
    t = input("How long (in years) would you like interest to accrue for?\n")
    if not (str(t).isdigit()):
        print("Don't try to break my fucking program")
        getT()
    return float(t)


def getR():
    r = input("Please input the nominal interest rate (Decimal):\n")
    if not (str(r).isdigit()):
        print("Don't try to break my fucking program")
        getR()
    return float(r)


def getComp():
    comp = input("How frequently would you like interest to compound? (Enter q for quarterly, a for annually, m for monthly)\n")
    if comp not in "aqm":
        print("Don't try to break my fucking program")
        getComp()
    return comp



def calculate(c , t , r ,comp):
    if comp == "q":
        return c*(1+(r/4))**(4*t)
    if comp == "a":
        return c*(1+r)**t
    if comp == "m":
        return c*(1+(r/12))**(12*t)

#comment

#Interest = C(1+(r/n))^(nt)
#n = number of times compounded per time t
#t = number of years in this case
#r = interest rate
#C = starting value

if __name__ == "__main__":
    main()