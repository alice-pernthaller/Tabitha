class Stage:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.width = self.x1 - self.x0

    def shift(self, shift):
        self.x0 -= shift
        self.x1 -= shift
