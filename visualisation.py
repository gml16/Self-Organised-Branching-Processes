#visualisation.py

import matplotlib.pyplot as plt
import numpy as np
import itertools

from avalanche import *

def plot_p_over_t(models, t=3000):
    colors = itertools.cycle(["r", "b", "g"])
    plt.title("The value of p as a function of time for a system with n = " + str(models[0].boundary) + " generations")
    plt.xlabel("p(t)")
    plt.ylabel("t")
    for m in models:
        c = next(colors)
        for i in range(t):
            plt.scatter(i, m.p, color=c, s = 0.1)
            m.add_unit_of_energy()
    plt.show()

def reproduce_figure2_paper():
    model1 = Avalanche(p = 0.1, boundary = 10)
    model2 = Avalanche(p = 0.4, boundary = 10)
    model3 = Avalanche(p = 0.6, boundary = 10)
    models = [model1, model2, model3]
    plot_p_over_t(models)

def show_relation_boundary_tstar():
    fig = plt.figure()
    ax = plt.gca()
    plt.title("Time t* at which p(t) reaches the asymptotic value p(t*) ≃ 1/2")
    plt.xlabel("t*")
    plt.ylabel("n")
    ax.set_yscale('log')
    for n in range(4, 22):
        model = Avalanche(p = 0.1, boundary = n)
        t_star = model.find_asymptotic_time()
        ax.scatter(n, t_star, color="r")
    plt.show()

def plot_distribution_avalanche_size(models, trials = 1000000):
    fig = plt.figure()
    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.title("Distribution probability of an avalanche's size")
    plt.xlabel("s")
    plt.ylabel("D(s)")
    colors = itertools.cycle(["r", "b", "g"])
    x = np.linspace(1, 150)
    ax.plot(x, (x**(-3/2))/5)
    for m in models:
        sizes = {}
        c = next(colors)
        for i in range(trials):
            m.add_unit_of_energy()
            m.p = 0.5 # Is that necessary?
            if m.s in sizes:
                sizes[m.s] += 1/trials
            else:
                sizes[m.s] = 1/trials
        for s, Ds in sizes.items():
            ax.scatter(s, Ds, color=c, s = 0.2)
    plt.show()

def reproduce_figure3_paper():
    model1 = Avalanche(boundary = 16)
    model2 = Avalanche(boundary = 20)
    model3 = Avalanche(boundary = 24)
    model4 = Avalanche(boundary = 28)
    models = [model1, model2, model3, model4]
    plot_distribution_avalanche_size(models)

def draw_avalanche_helper(node, x, y):
    plt.scatter(x, y, s=100, c="black")
    depth = 5 * (1-y)
    plt.scatter(x+0.1, y, s=0)
    plt.scatter(x-0.1, y, s=0)
    if node.left:
        nextx = x-(2**(-depth - 2))
        if depth < 4:
            plt.plot(np.arange(nextx, x, (x-nextx) / 185), np.arange(y-0.2, y-0.015, 0.001))
        draw_avalanche_helper(node.left, nextx, y-0.2)
    if node.right:
        nextx = x+(2**(-depth - 2))
        if depth < 8:
            plt.plot(np.arange(x, nextx, (nextx-x) / 185), np.arange(y-0.015, y-0.2, -0.001))
        draw_avalanche_helper(node.right, nextx, y-0.2)

def draw_avalanche(node):
    draw_avalanche_helper(node, 0.5, 1)
    plt.scatter(0, 0, s=0)
    plt.scatter(1, 1, s=0)
    plt.axis('off')
    plt.show()

def slope_at_p0(model, trials = 100):
    base_p0 = model.p
    avr_slope = -base_p0
    for i in range(trials):
        model.p = base_p0
        model.add_unit_of_energy()
        avr_slope += model.p/trials
    return avr_slope

def slopes_at_p0_wrt_n():
    fig = plt.figure()
    ax = plt.gca()
    plt.title("Estimate of the slope of p(t) at t = 0 for a starting probability p(0) = 0.1")
    plt.xlabel("n")
    plt.ylabel("Slope at p(0)")
    ax.set_yscale('log')
    for i in range(1, 40):
        ax.scatter(i, slope_at_p0(Avalanche(0.1, i)), s = 0.8)
    plt.show()
