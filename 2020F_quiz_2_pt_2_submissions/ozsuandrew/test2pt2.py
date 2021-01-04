# I pledge my honor that I have abided by the Stevens Honor System. Andrew Ozsu

def main():
    print("For Mathematical Functions, Please Enter the Number 1")
    print("For String Operations, Please Enter the Number 2")
    x=int(input("Enter Value: "))
    if x==1:
        print ("For Addition, Please Enter the Number 1")
        print ("For Subtraction, Please Enter the Number 2")
        print ("For Multiplication, Please Enter the Number 3")
        print ("For Division, Please Enter the Number 4")
        y=int(input("Enter Value: "))
        if y==1:
            a=(input("Enter 2 numbers seperated by a comma: "))
            a=a.split(",")
            a[0]=int(a[0])
            a[1]=int(a[1])
            b=a[0]+a[1]
            return (b)
        if y==2:
            c=(input("Enter 2 numbers seperated by a comma: "))
            c=c.split(",")
            c[0]=int(c[0])
            c[1]=int(c[1])
            d=c[0]-c[1]
            return (d)
        if y==3:
            e=(input("Enter 2 numbers seperated by a comma: "))
            e=e.split(",")
            e[0]=int(e[0])
            e[1]=int(e[1])
            f=e[0]*e[1]
            return (f)
        if y==4:
            g=(input("Enter 2 numbers seperated by a comma: "))
            g=g.split(",")
            g[0]=int(g[0])
            g[1]=int(g[1])
            h=g[0]/g[1]
            return (h)
        else:
            return ("Invalid Input")

    elif x==2:
        print ("To Determine the Number of Vowels in a String; Enter the Number 1")
        print ("To Encrypt a String; Enter the Number 2")
        z= int(input("Enter Value: "))
        if z==1:
            q=input("Enter String: ")
            count=0
            for i in q:
                if i=="a":
                    count+=1
                if i=="e":
                    count+=1
                if i=="i":
                    count+=1
                if i=="o":
                    count+=1
                if i=="u":
                    count+=1
            return (count)
        if z==2:
            j=input("Enter String: ")
            for i in j:
                x=ord(i)
                print(" ",x-4, end = " ")
        else:
            return ("Invalid Input")

    else:
        print ("Invalid Input")

