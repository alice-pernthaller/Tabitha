import math

from theatre.consumer.metrics.Metric import Metric

# calculates the number of seats between the seat and the aisle
class DistanceToAisle(Metric):
    def value_function(self, seat):
        s = seat
        seats_to_left = 0
        while s.left_seat:
            seats_to_left += 1
            s = s.left_seat

        s = seat
        seats_to_right = 0
        while s.right_seat:
            seats_to_right += 1
            s = s.right_seat

        minimum_distance = min(seats_to_right, seats_to_left)
        pythag_distance = math.sqrt(seat.x**2 + seat.y**2)

        minimum_distance = minimum_distance * 10000 + pythag_distance # bias towards better seats to resolve a tie
        return minimum_distance
