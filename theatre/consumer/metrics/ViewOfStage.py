from theatre.consumer.metrics.Metric import Metric


class ViewOfStage(Metric):
    def __init__(self, stage):
        self.stage = stage

    # mean squared distance from the seat to any point on the stage
    def value_function(self, seat):
        a = abs(seat.x)
        b = seat.y
        w = self.stage.width

        return (w**3)/12 + w*(a**2 + b**2)
