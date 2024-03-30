# A chain is an unbroken row of seats
class Chain:
    def __init__(self, seats):
        self.seats = seats
        self.len = len(seats)


# takes a seat and iterates recursively to each end of the row, returning a list of seats in the chain
# this is done until there are no seats left that are not in a chain. Finally, all the chains are returned.
def calculate_chains(seats):
    chains = []
    unchained_seats = list(seats.values())

    def _seats_to_right(seat):
        seats_to_right = []
        while seat.right_seat is not None:
            seats_to_right.append(seat.right_seat)
            seat = seat.right_seat
        return seats_to_right

    def _seats_to_left(seat):
        seats_to_left = []
        while seat.left_seat is not None:
            seats_to_left.append(seat.left_seat)
            seat = seat.left_seat
        return seats_to_left

    while unchained_seats:
        seat = unchained_seats[0]
        left = list(_seats_to_left(seat))
        left.reverse()
        right = _seats_to_right(seat)
        chain = left + [seat] + right
        for seat in chain:
            unchained_seats.remove(seat)
        chains.append(Chain(chain))

    return chains
