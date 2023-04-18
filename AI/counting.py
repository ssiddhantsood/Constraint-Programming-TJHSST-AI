n = int(input())  # read the number of cows

# read the cows' statements and sort them in increasing order
statements = sorted([(input()[1:], 1 if input()[0] == 'L' else -1) for _ in range(n)])

# initialize the variable that will keep track of the number of lying cows
lying_cows = 0

# initialize the variable that will keep track of Bessie's current hiding location
location = None

for statement, direction in statements:
    # if Bessie's hiding location is not known yet, then we can simply update it
    # based on the current cow's statement
    if location is None:
        location = (int(statement), direction)
        continue

    # if the current cow's statement is consistent with the current location, then we
    # don't need to do anything
    if direction == location[1]:
        continue

    # otherwise, we know that at least one of the cows is lying, so we update the
    # number of lying cows and update Bessie's hiding location based on the current
    # cow's statement
    lying_cows += 1
    location = (int(statement), direction)

# print the final result
print(lying_cows)