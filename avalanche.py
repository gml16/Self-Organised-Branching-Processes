import random
import math
import scipy.integrate as integrate

from node import *


class Avalanche:
    def __init__(self, p=0.5, boundary=10):
        self.p = p # Probability for each site to relax
        self.boundary = boundary # Represents the maximum size of the avalanche
        self.N = 2**(self.boundary+1) - 1 # Maximum size of the avalanche
        self.sigma = 1
        self.s = 1

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
        root = Node()
        self.s, self.sigma = self.relaxation_dynamics(root, 0)
        self.p += (1 - self.sigma)/self.N

    def find_asymptotic_time(self):
        error_margin = 1/10
        t = 0
        while self.p > 0.5+error_margin or self.p < 0.5-error_margin:
             self.add_unit_of_energy()
             t += 1
        return t

'''
    def phi(self, p):
        return (1/(2*math.pi*(0.26/self.N))**0.5) * math.exp(-((p-(0.5 - 0.69/self.N))**2)/(2*(0.26/self.N)))

    def P_n(self, s, p):
        return ((2*(1-p)/(math.pi*p))**0.5)/(s**(3/2)) * math.exp(-s/(-2/math.log(4*p*(1-p))))


    def D(self, s):
        return integrate.quad(lambda p: self.phi(p)*self.P_n(s,p), 1/(10**5), 1)
 '''
