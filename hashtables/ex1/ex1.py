def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # chache for the limit
    cache = {}

    # loop/iterate through list of weights
    for i in range(length):
        # if weight limit - weight at index i is in dictionary then we set key equal to it
        if limit - weights[i] in cache:
            max = limit - weights[i]
            # then we set j to be the cache value at key
            j = cache[max]
            # return the tuple (i, j)
            return [i, j]
        # set cache at weight index to i
        cache[weights[i]] = i

    return None # no solution found
