from theatre import my_constants
from theatre.consumer.metrics.Metric import Metric


def _row_to_row_number(seat):
    return my_constants.rows_to_row_numbers[seat.row]


# calculates the distance from the seat to the front, in rows
class DistanceFromFront(Metric):

    def value_function(self, seat):
        rows_from_front = _row_to_row_number(seat)
        rows_biased_to_centre = rows_from_front * 1000 + abs(seat.x)  # the more central seat resolves a tie
        return rows_biased_to_centre
