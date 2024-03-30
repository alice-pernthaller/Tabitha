from theatre.consumer.metrics.Metric import Metric


# calculates the distance of the seat from the central axis
class DistanceFromCentre(Metric):
    def value_function(self, seat):
        distance_from_centre = abs(seat.x)
        return distance_from_centre
