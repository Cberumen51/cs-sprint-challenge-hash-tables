#  Hint:  You may not need all of these.  Remove the unused functions.


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code 
    # cache for tickets
    cache = {}
    # list of routes
    route = []

    # go through tickets
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    
    # trip route starting with none
    route.append(cache["NONE"])
    # next location and go through ticket list
    for i in range(1, length): 
        route.append(cache[route[i-1]])

    return route
