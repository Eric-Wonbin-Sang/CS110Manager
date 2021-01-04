#final project
def main():

    def done():
        try:
            print()    
            done = int(input("If you are done with this program, please enter 1. If you would like to rerun it, enter 2: "))
        except ValueError:
            error()
        if done ==1:
            print()
            print("Thank you for using this program, have a great day! :)")
        elif done ==2:
            main()
            print()
        else:
            error()
            
    def error():
        print()
        print("Error: You entered something that was not one of the menu options")
        print("Please trying running the code from the beginning")
        main()

    try:
        print()
        print("Do you use Netflix or Hulu?")
        NorH = int(input("Enter 1 for Netflix and 2 for Hulu: "))
    except ValueError:
        error()
        
    if NorH ==1:
        try:
            print()
            ntime = int(input("How many months have you had Netflix for? "))
            print()
        except ValueError:
            error()
            
        if ntime == 0:
            print("Congrats! You have not spent any money on Netflix")
            done()
            
        else:
            try:
                print("Are you subscribed to the Basic, Standard, or Premium Plan?")
                netf = int(input("Enter 1 for Basic, 2 for Standard, and 3 for Premium: "))
                Bcost = 8.99 * ntime #cost of Netflix's basic plan
                Scost = 13.99 * ntime #cost of Netflix's standard plan
                Pcost = 17.99 * ntime #cost of Netflix's premium plan
                BBcost = 5.99 * ntime #cost of Hulu's basic plan
                PPcost = 11.99 * ntime #cost of Hulu's premium plan
            except ValueError:
                error()
                
            if netf == 1: #user is subscriber to Netflix's Basic plan
                print()
                print("In the time that you have been subscribed to the Basic plan, you have paid ${0:0.2f}".format(Bcost))
                print("If you had been subscribed to the Standard plan, you would have paid an extra ${0:0.2f}".format(Scost - Bcost), "bringing the total to ${0:0.2f}".format(Scost))
                print("If you had been subscribed to the Premium plan, you would have paid an extra ${0:0.2f}".format(Pcost - Bcost), "bringing the total to ${0:0.2f}".format(Pcost))
                print()
                print("Compared to Hulu:")
                print("If you had been subscribed to Hulu's Basic plan, you would have saved ${0:0.2f}".format(Bcost - BBcost), "lowering the total to ${0:0.2f}".format(BBcost))
                print("If you had been subscribed to Hulu's Premium plan, you would have paid an extra ${0:0.2f}".format(PPcost - Bcost), "bringing the total to ${0:0.2f}".format(PPcost))
                done()
                
            elif netf ==2:
                print()
                print("In the time that you have been subscribed to the Standard plan, you have paid ${0:0.2f}".format(Scost))
                print("If you had been subscribed to the Premium plan, you would have paid an extra ${0:0.2f}".format(Pcost - Scost), "bringing the total to ${0:0.2f}".format(Pcost))
                print("If you had been subscribed to the Basic plan, you would have saved ${0:0.2f}".format(Scost - Bcost), "lowering the total to ${0:0.2f}".format(Bcost))
                print()
                print("Compared to Hulu:")
                print("If you had been subscribed to Hulu's Basic plan, you would have saved ${0:0.2f}".format(Scost - BBcost), "lowering the total to ${0:0.2f}".format(BBcost))
                print("If you had been subscribed to Hulu's Premium plan, you would have saved ${0:0.2f}".format(Scost - PPcost), "lowering the total to ${0:0.2f}".format(PPcost))
                done()
            elif netf ==3:
                print()
                print("In the time that you have been subscribed to the Premium plan, you have paid ${0:0.2f}".format(Pcost))
                print("If you had been subscribed to the Basic plan, you would have saved ${0:0.2f}".format(Pcost - Bcost), "lowering the total to ${0:0.2f}".format(Bcost))
                print("If you had been subscribed to the Standard plan, you would have saved ${0:0.2f}".format(Pcost - Scost), "lowering the total to ${0:0.2f}".format(Scost))
                print()
                print("Compared to Hulu:")
                print("If you had been subscribed to Hulu's Basic plan, you would have saved ${0:0.2f}".format(Pcost - BBcost), "lowering the total to ${0:0.2f}".format(BBcost))
                print("If you had been subscribed to Hulu's Premium plan, you would have saved ${0:0.2f}".format(Pcost - PPcost), "lowering the total to ${0:0.2f}".format(PPcost))
                done()
            else:
                error()         
    elif NorH ==2:
        try:
            print()
            ntime = int(input("How many months have you had Hulu for? "))
            print()
        except ValueError:
            error()
        if ntime == 0:
            print("Congrats! You have not spent any money on Hulu")
            done()
        else:
            try:
                print("Are you subscribed to the Basic or Premium Plan?")
                hulu = int(input("Enter 1 for Basic and 2 for Premium: "))
                Bcost = 8.99 * ntime
                Scost = 13.99 * ntime
                Pcost = 17.99 * ntime
                BBcost = 5.99 * ntime
                PPcost = 11.99 * ntime
            except ValueError:
                error()
            if hulu == 1:
                print()
                print("In the time that you have been subscribed to the Basic plan, you have paid ${0:0.2f}".format(BBcost))
                print("If you had been subscribed to the Premium plan, you would have paid an extra ${0:0.2f}".format(PPcost - BBcost), "bringing the total to ${0:0.2f}".format(PPcost))
                print()
                print("Compared to Netflix:")
                print("If you had been subscribed to the Netflix's Basic plan, you would have paid an extra ${0:0.2f}".format(Bcost - BBcost), "bringing the total to ${0:0.2f}".format(Bcost))
                print("If you had been subscribed to the Netflix's Standard plan, you would have paid an extra ${0:0.2f}".format(Scost - BBcost), "bringing the total to ${0:0.2f}".format(Scost))
                print("If you had been subscribed to the Netflix's Premium plan, you would have paid an extra ${0:0.2f}".format(Pcost - BBcost), "bringing the total to ${0:0.2f}".format(Pcost))
                done()
            elif hulu ==2:
                print()
                print("In the time that you have been subscribed to the Premium plan, you have paid ${0:0.2f}".format(PPcost))
                print("If you had been subscribed to the Basic plan, you would have saved ${0:0.2f}".format(PPcost - BBcost), "lowering the total to ${0:0.2f}".format(BBcost))
                print()
                print("Compared to Netflix:")
                print("If you had been subscribed to Netflix's Basic plan, you would have saved ${0:0.2f}".format(Bcost - BBcost), "lowering the total to ${0:0.2f}".format(Bcost))
                print("If you had been subscribed to Netflix's Standard plan, you would have paid an extra ${0:0.2f}".format(Scost - PPcost), "bringing the total to ${0:0.2f}".format(Scost))
                print("If you had been subscribed to Netflix's Premium plan, you would have paid an extra ${0:0.2f}".format(Pcost - PPcost), "bringing the total to ${0:0.2f}".format(Pcost))
                done()
            else:
                error()
    else:
        error()  
main()

