#I pledge that I have abided by the Stevens Honor System
#This program will offer a Fair Lawn, NJ resident the historical property tax in the town
#It will then give them the option to calculate their total tax payment
#per that year 
#Assessed Value x General Tax Rate = Tax Bill
#It will then compare that tax bill to the town, state or national average 



def main():
    print("This program will calculate the annual tax payment")
    print("Of a Fair Lawn, New Jersey resident based on the year of their choice\n")

    x = int(input("Enter the year(between 1998-2019)for which you want to calculate property tax:"))
    y = int(input("Enter the assessed value of your home, with no commas: "))
            
    if x == 1998: 
            taxbill = y * .02680
            print("Your tax bill in", x, "was:$", taxbill)
            
    elif x == 1999:
        taxbill = y * .02750
        print("Your tax bill in", x, "was:$", taxbill)
        
    elif x == 2000:
        taxbill = y * .02850
        print("Your tax bill in", x, "was:$", taxbill)
        
    elif x == 2001:
        taxbill = y * .03040
        print("Your tax bill in", x, "was:$", taxbill)
        
    elif x == 2002:
        taxbill = y * .03260
        print("Your tax bill in", x, "was:$", taxbill)
        
    elif x == 2003:
        taxbill = y * .03370
        print("Your tax bill in", x, "was:$", taxbill)
        
    elif x == 2004:
        taxbill = y * .03670
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2005:
        taxbill = y * .03890
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2006:
        taxbill = y * .04260
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2007:
        taxbill = y * .02030
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2008:
        taxbill = y * .02103
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2009:
        taxbill = y * .02153
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2010:
        taxbill = y * .02283
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2011:
        taxbill = y * .02337
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2012:
        taxbill = y * .02942
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2013:
        taxbill = y * .02989
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2014:
        taxbill = y * .03026
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2015:
        taxbill = y * .03078
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2016:
        taxbill = y * .03137
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2017:
        taxbill = y * .03226
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2018:
        taxbill = y * .03308
        print("Your tax bill in", x, "was:$", taxbill)
    elif x == 2019:
        taxbill = y * .03370
        print("Your tax bill in", x, "was:$", taxbill)
    else:
        print("This year is not in the specified range of historical property tax data\n")

    print("Now you can compare your tax bill to the town, state, or national average\n")

    o = int(input("Enter 1 for town, 2 for state, or 3 for national: "))

    if o == 1:
        average = taxbill / 11140
        final = average * 100
        print("Your taxbill is", final, "% of the town's average taxbill of $11,140")
    elif o == 2:
        average = taxbill / 7800
        final = average * 100
        print("Your taxbill is", final, "% of the state's average taxbill of $7,800")
    elif o == 3:
        average = taxbill / 2279
        final = average * 100
        print("Your taxbill is", final, "% of the country's average taxbill of $2,279")
    else:
        print("Wrong input")
        
    print("Now this program will encode your tax bill so that it can remain secret\n")

    encode = (taxbill - 100 * 2) / 3
    print("Your encoded tax bill is:", encode)

    l = int(input("If you are done with this program simply enter 0, if you wish to see your taxbill once more enter 1: \n"))
    if l == 0:
        print("Have a great day thank you for using this program")
    elif l == 1:
        print("Your taxbill:", taxbill,"/ Your encoded taxbill:", encode)
    else:
        print("Wrong NUMBER")
main()



   


    
