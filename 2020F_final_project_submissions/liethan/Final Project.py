import numpy as np
import matplotlib.pyplot as plt

def main():
    print("This program will allow the user to create a bar graph or a pie chart")
    start = input("Please enter 1 for a bar graph, or enter 2 for a pie chart: ")
    if start == "1":
        title = input("Please enter the title of your bar graph: ")
        xaxis = input("Please enter the label for the x axis: ")
        xcat = []
        catnum = int(input("Please enter the number of categories for the x axis: "))
        print("Please enter each category name in the desired order (hit enter after each category name): ")
        for i in range(0, catnum):
            list = input()

            xcat.append(list)
        x_pos = np.arange(len(xcat))
        print("Please enter the corresponding values to the categories previously entered. \nThe values should be in the exact order of that the category names were entered in(hit enter after each category name): ")
        catval = []
        for i in range(0, catnum):
            vallist = input()

            catval.append(vallist)
        yaxis = input("Please enter the label for the y axis: ")
        yscale = float(input("Please enter the increment that the y axis will increase by: "))

        fig, ax = plt.subplots()

        ax.bar(x_pos, [int(x) for x in catval], align='center', alpha=yscale)
        ax.set_title(title)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(yaxis)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(xcat)
        ax.yaxis.grid(True)

        plt.tight_layout()
        plt.savefig('bar_plot.png')
        plt.show()


    elif start == "2":
        title2 = input("Please enter the title of your pie chart: ")
        cat = []
        catnum2 = int(input("Please enter number of categories/pieces that will be on the pie chart: "))
        print("Please enter each category name in the desired order (hit enter after each category name): ")
        for i in range(0, catnum2):
            list = input()

            cat.append(list)
        pieces = []
        print("Please enter the size/percentage for each piece. These should be in the exact order that the categories were entered in (hit enter after each size/percentage) \nFor percentages, use the decimal notation: ")
        for i in range(0, catnum2):
            piecelist = float(input())

            pieces.append(piecelist)

        fig, ax = plt.subplots()
        ax.pie(pieces, labels=cat, autopct='%1.1f%%')
        ax.axis('equal')
        ax.set_title(title2)

        plt.show()


    else:
        print("That is not a valid input")

main()