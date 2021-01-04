#I, Serena Migdal, pledge to have abided by Stevens Honor Code
import csv

def main():
    print('This Program will let you compare the top preforming stocks of the S&P 500')
    print('over the past decade.')
    print('Years that can be compared: 2013, 2015, 2017, 2020')
    print('enter 2 years seperated by just a comma, with the older year first: ')
    ans1 = input()
    if ans1 == "2015,2020":
        with open('SP500_2020.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2020names = []
            for row in reader:
                SP2020names.append(row[1])

        with open('SP500_2015.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2015names = []
            for row in reader:
               SP2015names.append(row[1])


            SP2020names = set(SP2020names)
            SP2015names = set(SP2015names)
            the2020names = SP2020names.difference(SP2015names)

            print(the2020names)
          
    elif ans1 == "2015,2017":
        with open('SP500_2017.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2017names = []
            for row in reader:
                SP2017names.append(row[1])

        with open('SP500_2015.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2015names = []
            for row in reader:
               SP2015names.append(row[1])


            SP2017names = set(SP2017names)
            SP2015names = set(SP2015names)
            the2017names = SP2017names.difference(SP2015names)
            print('These stocks were top preformers in 2017, but not 2015:')
            print(the2017names)

    elif ans1 == "2017,2020":
        with open('SP500_2020.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2020names = []
            for row in reader:
                SP2020names.append(row[1])
        with open('SP500_2017.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2017names = []
            for row in reader:
                SP2017names.append(row[1])

            
            SP2020names = set(SP2020names)
            SP2017names = set(SP2017names)
            the2020names = SP2020names.difference(SP2017names)
            print('These stocks were top preformers in 2020, but not 2017:')
            print(the2020names)

    elif ans1 == "2013,2015":
            with open('SP500_2015.csv', newline= '') as csvfile:
                reader = csv.reader(csvfile)
                SP2015names = []
                for row in reader:
                   SP2015names.append(row[1])
            with open('SP500_2013.csv', newline= '') as csvfile:
                reader = csv.reader(csvfile)
                SP2013names = []
                for row in reader:
                    SP2013names.append(row[1])

            SP2015names = set(SP2015names)
            SP2013names = set(SP2013names)
            the2015names = SP2015names.difference(SP2013names)
            print('These stocks were top preformers in 2015, but not 2013:')
            print(the2015names)
    elif ans1 == "2013,2017":
        with open('SP500_2017.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2017names = []
            for row in reader:
                SP2017names.append(row[1])
        with open('SP500_2013.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2013names = []
            for row in reader:
                SP2013names.append(row[1])
        SP2017names = set(SP2017names)
        SP2013names = set(SP2013names)
        the2017names = SP2017names.difference(SP2013names)
        print('These stocks were top preformers in 2017, but not 2013:')
        print(the2017names)
    elif ans1 == "2013,2020":
        with open('SP500_2020.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2020names = []
            for row in reader:
                SP2020names.append(row[1])
        with open('SP500_2013.csv', newline= '') as csvfile:
            reader = csv.reader(csvfile)
            SP2013names = []
            for row in reader:
                SP2013names.append(row[1])
        SP2020names = set(SP2020names)
        SP2013names = set(SP2013names)
        the2020names = SP2020names.difference(SP2013names)
        print('These stocks were top preformers in 2020, but not 2013:')
        print(the2020names)                   

main()

def main1():
    print(' to view the stock info for any year, enter the year below. enter no if you do not want to:')
    ans2 = input()
    if ans2 == "2013":
        x = open('SP500_2013.csv')
        csv_x = csv.reader(x)
        for row in csv_x:
            print(row)

    elif ans2 == "2015":
        x = open('SP500_2015.csv')
        csv_x = csv.reader(x)
        for row in csv_x:
            print (row)

    elif ans2 == "2017":
        x = open('SP500_2017.csv')
        csv_x = csv.reader(x)
        for row in csv_x:
            print (row)
    elif ans2 == "2020":
        x = open('SP500_2020.csv')
        csv_x = csv.reader(x)
        for row in csv_x:
            print (row)
    elif ans2 == "no":
        print('thanks for trying my program')
    
main1()

print('Happy Holidays')










