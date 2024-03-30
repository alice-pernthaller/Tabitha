from theatre.layout.TheatreCSVReader import parse_stage, parse_seats

def _shift_seats(physical_seats, shift):
    for s in physical_seats.values():
        s.shift(shift)

# shift seat and stage x-coordinates to make the stage the origin
def load_theatre(stage_filename, seats_filename):
    stage = parse_stage(stage_filename)
    shift = (stage.x0 + stage.x1) / 2
    stage.shift(shift)
    seats = parse_seats(seats_filename)
    _shift_seats(seats, shift)

    return stage, seats
