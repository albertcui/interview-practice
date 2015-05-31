def findSteps(n, choices):
    """
    Finds the number of permuations to make n steps, given
    a set of possible choices for each move
    @param n - number of steps to achive/remaining
    @param choices - set of possible moves
    """
    count = 0
    for step in choices:
        remain = n - step
        if remain == 0:
            count += 1
        elif remain > 0:
            count += findSteps(remain, choices)
    return count

choices = {1, 2, 3}

print findSteps(3, choices)