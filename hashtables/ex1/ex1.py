def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # chache for the limit
    cache = {}

    # loop/iterate through list of weights
    for i in range(length):

        if weights[i] not in cache: 
            cache[weights[i]] = i 
        else:
            # if current weight equals limit
            if limit - weights[i] == weights[i]: 
                return (i, cache[weights[i]]) 
        #calulate weight difference
        weight_diff = limit - weights[i] 

        if weight_diff in cache and weight_diff != weights[i]: 
            return sorted((cache[weight_diff], cache[weights[i]]), reverse=True) 

    return None # no solution found
