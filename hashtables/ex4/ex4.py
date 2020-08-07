def has_negatives(a):
    cache = {}
    negatives = []

    # [1, 1, ,1, 2, 3, 5, -1, -2]

    # { 
    #     1: [1, 1, 1, -1]
    #     2: [2, -2],
    #     3: [3],
    #     5: [5]
    # }

    # set up dict with absolute value of each number as keys
    for number in a:
        abs_value = abs(number)
        # if it doesnt exist yet we will create a new list
        if abs_value not in cache:
            cache[abs_value] = [number]
        # otherwise we can add on to existing list
        else:
            cache[abs_value].append(number)

    for num in cache:
        # does the list contain both a postive and a negative
        if any(x < 0 for x in cache[num]) and any(x > 0 for x in cache[num]):
            negatives.append(num)

    return negatives


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
