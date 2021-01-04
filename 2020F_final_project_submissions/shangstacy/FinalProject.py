# Stacy Shang
# Final Project
# I pledge my honor that I have abided by the Stevens Honor System. - Stacy Shang
# This python project tracks COVID-19 cases in the top most populous European countries

import pandas as pd
import matplotlib.pyplot as plt

COVID19_dataset = r"https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(COVID19_dataset)

def countrymenu():
    print("Country Menu:\n")
    print("The following program will show the amount of deaths due to COVID-19 in the top 10 most populated European countries.")
    print("To view Russia, Enter 1")
    print("To view Turkey, Enter 2")
    print("To view Germany, Enter 3")
    print("To view France, Enter 4")
    print("To view the United Kingdom, Enter 5")
    print("To view Italy, Enter 6")
    print("To view Spain, Enter 7")
    print("To view Ukraine, Enter 8")
    print("To view Poland, Enter 9")
    print("To view Romania, Enter 10")
countrymenu()

itemselect = int(input("Enter the desired option number:"))

if itemselect == 1:

    print("\nSubMenu for Russia:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Russia = df[df['Country'] == 'Russia']
        axis1 = plt.gca()
        df_Russia.plot(kind='line', x='Date', y='Deaths', color='red', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Russia = df[df['Country'] == 'Russia']
        print(df_Russia.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 2:

    print("\nSubMenu for Turkey:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Turkey = df[df['Country'] == 'Turkey']
        axis1 = plt.gca()
        df_Turkey.plot(kind='line', x='Date', y='Deaths', color='blue', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Turkey = df[df['Country'] == 'Turkey']
        print(df_Turkey.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 3:

    print("\nSubMenu for Germany:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Germany = df[df['Country'] == 'Germany']
        axis1 = plt.gca()
        df_Germany.plot(kind='line', x='Date', y='Deaths', color='purple', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Germany = df[df['Country'] == 'Germany']
        print(df_Germany.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 4:

    print("\nSubMenu for France:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_France = df[df['Country'] == 'France']
        axis1 = plt.gca()
        df_France.plot(kind='line', x='Date', y='Deaths', color='purple', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_France = df[df['Country'] == 'France']
        print(df_France.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 5:

    print("\nSubMenu for the UK:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_UK = df[df['Country'] == 'United Kingdom']
        axis1 = plt.gca()
        df_UK.plot(kind='line', x='Date', y='Deaths', color='pink', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_UK = df[df['Country'] == 'United Kingdom']
        print(df_UK.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 6:

    print("\nSubMenu for Italy:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Italy = df[df['Country'] == 'Italy']
        axis1 = plt.gca()
        df_Italy.plot(kind='line', x='Date', y='Deaths', color='green', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Italy = df[df['Country'] == 'Italy']
        print(df_Italy.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 7:

    print("\nSubMenu for Spain:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Spain = df[df['Country'] == 'Spain']
        axis1 = plt.gca()
        df_Spain.plot(kind='line', x='Date', y='Deaths', color='orange', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Spain = df[df['Country'] == 'Spain']
        print(df_Spain.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 8:

    print("\nSubMenu for Ukraine:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Ukraine = df[df['Country'] == 'Ukraine']
        axis1 = plt.gca()
        df_Ukraine.plot(kind='line', x='Date', y='Deaths', color='yellow', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Ukraine = df[df['Country'] == 'Ukraine']
        print(df_Ukraine.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 9:

    print("\nSubMenu for Poland:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Poland = df[df['Country'] == 'Poland']
        axis1 = plt.gca()
        df_Poland.plot(kind='line', x='Date', y='Deaths', color='indigo', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Poland = df[df['Country'] == 'Poland']
        print(df_Poland.tail(1))
    else:
        print("Error: Invalid Entry")

elif itemselect == 10:

    print("\nSubMenu for Romania:")
    print("To view a graph of the desired European country, Enter 1")
    print("To view the number of most recent confirmed cases, recovered, and deaths for the desire European country, Enter 2")
    itemselect1 = int(input("Enter the desired viewing option:"))

    if itemselect1 == 1:
        df_Romania = df[df['Country'] == 'Romania']
        axis1 = plt.gca()
        df_Romania.plot(kind='line', x='Date', y='Deaths', color='brown', ax=axis1)
        plt.show()
    elif itemselect1 == 2:
        df_Romania = df[df['Country'] == 'Romania']
        print(df_Romania.tail(1))
    else:
        print("Error: Invalid Entry")

else:
    print("Error: Invalid Entry")