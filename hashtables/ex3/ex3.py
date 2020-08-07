def intersection(arrays):
    cache = {}
    intersections = []

    # 0: [1, 2, 3]
    # 1: [2, 5, 6]
    # 2: [1, 2, 7, 8, 9]
    # 3: [1, 2, 5]

    # {
    #     1: [0, 2, 3]
    #     2: [0, 1, 2, 3]
    #     3: [0]
    #     5: [1, 3]
    #     6: [1]
    #     7: [2]
    #     8: [2]
    #     9: [2]
    # }

    # set up mapping of list values to each array index they are contained in
    # i.e. above, 1 is in the 0th array and the 2nd and 3rd array
    # enumerate allows us to access both the index and the value
    for i, array in enumerate(arrays):
        for num in array:
            if num not in cache:
                cache[num] = [i]
            else:
                cache[num].append(i)

    # to determine if its an intersection we see if the cache list length for a specific number is the same as the arrays length
    # this means the number is present in all arrays
    for c in cache:
        if (len(cache[c]) == len(arrays)):
            intersections.append(c)

    return intersections

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
