class Avalanche:
    def __init__(self, p0=0.5, boundary=10):
        self.p = {p0}
        # If the node is a leaf the value corresponds to the label, otherwise it corresponds to the Wifi strenght at which we separate the sets into 2
        self.boundary = boundary

    def sigma(p, t)
