from theatre import my_constants
from theatre.consumer.Selection import Selection


def _calculate_seat_price(seat):
    seat_price = my_constants.price_list[seat.section]
    if seat.row == my_constants.front_rows[seat.section]:
        seat_price *= 1.5
    return seat_price

# a query contains all the customer's constraints and preferences.
class Query:
    def __init__(self, party_size, budget, metric, price_list):
        self.party_size = party_size
        self.budget = budget
        self.metric = metric
        self.price_list = price_list

    # the best selection is the one with the best score for the worst seat in the selection
    def _best_selection(self, seats, scores, prices):

        if len(seats) == 1:
            return Selection(scores[0], [seats[0]], prices[0])

        selections = []

        # 'Sliding window' algorithm
        possible_leftmost_party_positions = range(len(seats) - self.party_size + 1)
        for leftmost_party_position in possible_leftmost_party_positions:

            worst_score_in_party = float('-inf')
            selection_price = 0
            for position_in_party in range(self.party_size):
                index = leftmost_party_position + position_in_party

                price = prices[index]
                selection_price += price

                score = scores[index]
                if score > worst_score_in_party:
                    worst_score_in_party = score
            seats_in_selection = seats[leftmost_party_position:leftmost_party_position + self.party_size]

            if selection_price <= self.budget:
                selection = Selection(worst_score_in_party, seats_in_selection, selection_price)
                selections.append(selection)

        if len(selections) == 0:
            best_selection_so_far = None
        elif len(selections) == 1:
            best_selection_so_far = selections[0]
        else:
            head, *tail = selections
            best_selection_so_far = head
            for selection in tail:
                if selection.score == best_selection_so_far.score:
                    if selection.seats[0].id < best_selection_so_far.seats[0].id:
                        best_selection_so_far = selection
                if selection.score < best_selection_so_far.score:
                    best_selection_so_far = selection

        return best_selection_so_far

    # calculates the scores and prices of all the seats in the chain, and finds the best selection
    def find_best_selection_in_chain(self, chain):
        scores = []
        prices = []
        for seat in chain.seats:
            score = self.metric.value_function(seat)
            scores.append(score)

            seat_price = _calculate_seat_price(seat)
            prices.append(seat_price)

        return self._best_selection(chain.seats, scores, prices)
