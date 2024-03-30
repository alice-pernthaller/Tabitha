import unittest

from theatre.bookings import Chain
from theatre.bookings.Availability import Availability
from theatre.consumer.Query import Query
from theatre.consumer.Selection import Selection
from theatre.consumer.metrics.DistanceToAisle import DistanceToAisle
from theatre.layout.TheatreLoader import load_theatre

stage, seats = load_theatre("../resources/TestStage.csv", "../resources/TestSeats.csv")
chains = Chain.calculate_chains(seats)
availability = Availability(chains, stage)
qualifiers = None

# book every seat in the test theatre that is on the aisle EXCEPT seat A1
selections_to_book = []
selections_to_book.append(Selection(None, [seats[3]], None))
selections_to_book.append(Selection(None, [seats[4]], None))
selections_to_book.append(Selection(None, [seats[7]], None))
selections_to_book.append(Selection(None, [seats[8], seats[9]], None))
selections_to_book.append(Selection(None, [seats[10]], None))
selections_to_book.append(Selection(None, [seats[12]], None))
selections_to_book.append(Selection(None, [seats[13], seats[14]], None))
selections_to_book.append(Selection(None, [seats[15], seats[16]], None))
selections_to_book.append(Selection(None, [seats[17], seats[18]], None))

for selection in selections_to_book:
    availability.remove_selection_from_availability(selection)


class Testing(unittest.TestCase):

    # asks for the seat closest to the aisle and checks that the only available aisle seat is returned
    def test_distance_to_aisle(self):
        query = Query(1, float('inf'), DistanceToAisle(), None)
        best_selection = availability.find_best_selection(query)[0][2].seats
        self.assertEqual(best_selection, [seats[1]])
