def main():
    x=input("Enter a date:" )
    x=x.split("/")
    if int(x[0]) <= 12 :
        if int (x[0]) > 0:
            if int(x[1]) <=29 :
                if int (x[1]) > 0 :
                    if int (x[2]) > 0 :
                        return("this date is valid")
    elif int(x[1]) == 1 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 3 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 5 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 6 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 7 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 8 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 10 :
        if int(x[1])> 0 :
            return("this date is valid")
    elif int(x[1]) == 12 :
        if int(x[1])> 0 :
            return("this date is valid")

    return("this date is not valid")
            
                

          
