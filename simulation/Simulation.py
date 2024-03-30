import random

from theatre.consumer.Query import Query
from theatre.consumer.metrics.DistanceFromCentre import DistanceFromCentre
from theatre.consumer.metrics.DistanceFromFront import DistanceFromFront
from theatre.consumer.metrics.DistanceToAisle import DistanceToAisle
from theatre.consumer.metrics.ViewOfStage import ViewOfStage

# the simulation generates random parties to book up the theatre
# when the conversation begins, there is a believable distribution of available seats
class Simulation:

    def __init__(self, availability, price_list):
        self.availability = availability
        self.price_list = price_list

    def __next__(self):
        if self.availability.calculate_remaining_seats() > 0:
            query = self._generate_random_query()
            best_selections = self.availability.find_best_selection(query)
            if best_selections:
                choice = self.availability.find_best_selection(query)[0][2] # chooses the best selection within budget
                self.availability.remove_selection_from_availability(choice)
            else:
                choice = None
            return choice

    def _generate_random_query(self):

        # weighted party size distribution, favouring smaller party sizes
        party_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        party_size = random.choices(party_sizes, weights=[0.05, 0.44, 0.2, 0.15, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.005])[0]

        # weighted budget distribution, favouring smaller budgets
        budgets = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 160]
        budget_per_person = random.choices(budgets, weights=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.075, 0.075, 0.02, 0.02, 0.01])[0]
        budget = party_size * budget_per_person

        # customer preference is most likely to be view of the stage
        metrics = [ViewOfStage(self.availability.stage), DistanceFromCentre(), DistanceFromFront(), DistanceToAisle()]
        preferred_metric = random.choices(metrics, weights=[0.5, 0.15, 0.15, 0.2])[0]

        query = Query(party_size, budget, preferred_metric, self.price_list)
        return query
