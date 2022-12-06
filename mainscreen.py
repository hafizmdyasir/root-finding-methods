from datafile import methods


def showScreen():
    print("\n\n")
    print("NUMERICAL ROOT FINDING PROGRAMS")
    print("Developed by Mohammad Yasir")

    print("\nThe following root finding methods are supported:")
    index = 1
    for method in methods:
        print("\t{0}. {1}".format(index, method.name))
        index += 1
    print("\n")
    choice = int(input("Please enter a choice --> "))
    methods[choice-1].call()


showScreen()