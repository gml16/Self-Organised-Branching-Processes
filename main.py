#main.py

from visualisation import *

def main():
    print("Visualise: ")
    print("[1] Probability of relaxing a site over time")
    print("[2] Relationship between boundary of the avalanche and time at which the probability has reached critical value 0.5")
    print("[3] Probability distribution of avalanches' size")
    print("[4] A customised avalanche")
    choice = input()
    if choice == "1":
        reproduce_figure2_paper()
    elif choice == "2":
        show_relation_boundary_tstar()
    elif choice == "3":
        reproduce_figure3_paper()
    elif choice == "4":
        p = input("Probability for any site to relax: ")
        boundary = input("Boundary of your avalanche: ")
        model = Avalanche(float(p), int(boundary))
        model.add_unit_of_energy()
        draw_avalanche(model.root)
        print(str(model.sigma) + " units of energy left the site")
        print("The new probability for each site to relax is: " + str(model.p))
        while (input("Would you like to run next iteration?: ").lower() == "y"):
            model.add_unit_of_energy()
            draw_avalanche(model.root)
            print(str(model.sigma) + " units of energy left the site")
            print("The new probability for each site to relax is: " + str(model.p))
    else:
        print("Please type 1, 2 or 3")
        main()

if __name__ == '__main__':
    main()
