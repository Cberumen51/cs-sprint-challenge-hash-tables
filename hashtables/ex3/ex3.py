def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    # list where we add matching numbers
    results = []

    # go through each list in array
    for i in arrays:
        # now we loop through the numbers 
        for j in i:
            # if the num is already in the cache of values we count them
            if j in cache:
                # increase count 
                cache[j] += 1
                # if num equals the length then we add it to results because we know it's in all lists
                if cache[j] == len(arrays):
                    results.append(j)
            # otherwise we set it equal to 1
            else:
                cache[j] = 1
    return results

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
