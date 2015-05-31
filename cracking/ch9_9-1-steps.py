def findStepsNaive(n, choices):
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
            count += findStepsNaive(remain, choices)
    return count

choices = {1, 2, 3}
target_steps = 5
print findStepsNaive(target_steps, choices)

def findStepsEfficient(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    # Can use variables
    # prev1 = 4
    # prev2 = 2
    # prev3 = 1
    # Or a list/array
    pi = [1, 2, 4]
    for i in range (4, n + 1):
        # steps = prev1 + prev2 + prev3
        # prev3 = prev2
        # prev2 = prev1
        # prev1 = steps

        # What is the complexity of the data structure?
        steps = sum(pi)
        pi.pop(0)
        pi.append(steps)

    return pi[2]

print findStepsEfficient(target_steps)