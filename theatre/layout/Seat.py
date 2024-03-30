class Seat:
    def __init__(self, id, row, number, section, x, y):
        self.id = id
        self.row = row
        self.number = number
        self.section = section
        self.x = x
        self.y = y
        self.left_seat = None
        self.right_seat = None

    def shift(self, shift):
        self.x -= shift

    def link_neighbours(self, left_seat, right_seat):
        self.left_seat = left_seat
        self.right_seat = right_seat
