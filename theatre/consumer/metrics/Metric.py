# A metric models consumer preference. This class is used polymorphically to produce multiple preferences
class Metric:

    # a metric must have a mechanism for scoring a seat
    def value_function(self, seat):
        return
