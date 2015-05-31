def findNum(n, coin):
    """
    Returns the number of combinations to create n cents in change.
    Init with quarter
    @param n - number of cents to create change for
    @param coin - the current coin to create change with
    """
    if coin == "quarter":
        return makeSets(n, 25, "dime")
    elif coin == "dime":
        return makeSets(n, 10, "nickle")
    elif coin == "nickle":
        return makeSets(n, 5, "penny")
    elif coin == "penny":
        return makeSets(n, 1, None)


def makeSets(n, val, next):
    """
    Auxillary function to create change
    """
    count = 0
    for i in range(0, n/val + 1):
        change = n - val*i
        if change == 0:
            count += 1
        elif change > 0 and next != None:
            count += findNum(change, next)
    return count

print findNum(15, "quarter")