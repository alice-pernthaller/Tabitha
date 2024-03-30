import csv

from theatre.layout import TheatreLoadingError
from theatre.layout.Linkage import Linkage
from theatre.layout.Seat import Seat
from theatre.layout.Stage import Stage


# reads stage csv and returns a Stage object
def parse_stage(filename):
    try:
        with open(filename) as file:
            csvreader = csv.reader(file)
            next(csvreader)

            for record in csvreader:
                x0 = int(record[0])
                y0 = int(record[1])
                x1 = int(record[2])
                y1 = int(record[3])
                stage = Stage(x0, y0, x1, y1)  # original layout stage coordinates

                return stage
    except:  # error handling - raise error if file cannot be read
        raise TheatreLoadingError


# reads seats csv and returns map of Seat objects
def parse_seats(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    next(csvreader)  # skip header
    seats = {}
    linkages = []

    for record in csvreader:
        id = int(record[0])
        row_label = record[1]
        number_label = record[2]
        section = record[3]
        x = int(record[4])
        y = int(record[5])

        seats[id] = Seat(id, row_label, number_label, section, x, y)

        '''all seats must be created before linking with neighbours
        otherwise links will be made to seat objects that do not yet exist'''
        left_id = None
        right_id = None
        if record[6] != "None":
            left_id = int(record[6])
        if record[7] != "None":
            right_id = int(record[7])
        linkages.append(Linkage(id, left_id, right_id))

    file.close()

    # seat objects are linked to their left and right neighbours
    for linkage in linkages:
        left_seat = None
        right_seat = None

        if linkage.left_id is not None:
            left_seat = seats[linkage.left_id]

        if linkage.right_id is not None:
            right_seat = seats[linkage.right_id]

        seat = seats[linkage.seat_id]
        seat.link_neighbours(left_seat, right_seat)

    return seats
