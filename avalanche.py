#avalanche.py

import random
import math
import scipy.integrate as integrate

from node import *

class Avalanche:
    def __init__(self, p=0.5, boundary=10):
        self.p = p                        # Probability for each site to relax
        self.boundary = boundary          # Represents the maximum size of the avalanche
        self.N = 2**(self.boundary+1) - 1 # Maximum size of the avalanche
        self.sigma = 1                    # Number of sites leaving the system
        self.s = 1                        # Number of sites relaxing
        self.root = Node()

    def relaxation_dynamics(self, parent, depth):
        if depth < self.boundary:
            if random.uniform(0, 1) < self.p:
                left = Node()
                right = Node()
                parent.set_left(left)
                parent.set_right(right)
                s_left, sigma_left = self.relaxation_dynamics(left, depth + 1)
                s_right, sigma_right = self.relaxation_dynamics(right, depth + 1)
                return (s_left + s_right + 1, sigma_left + sigma_right)
            else:
                return (1, 0)
        else:
            return (1, 1)

    def add_unit_of_energy(self):
        self.root = Node()
        self.s, self.sigma = self.relaxation_dynamics(self.root, 0)
        self.p += (1 - self.sigma)/self.N

    def find_asymptotic_time(self):
        error_margin = 1/10
        t = 0
        while self.p > 0.5+error_margin or self.p < 0.5-error_margin:
             self.add_unit_of_energy()
             t += 1
        return t
