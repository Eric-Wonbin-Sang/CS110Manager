# Catherine Maloney - CS110 HW4
# I pledge my honor that I have abided by the Stevens Honor System.

def main():
    
    print("This program converts a list of lowercase names to uppercase.")
    file1Name = input("What is the file containing the list of names? ")
    # file: Before.txt
    file2Name = input("Name the file for the uppercase names: ")
    # file: After.txt

    file1 = open(file1Name, "r")
    file2 = open(file2Name, "w")

    for  i in file1:
        ucase = i.upper()
        print(ucase, file=file2)
        
    file1.close
    file2.close
    print("The capitalized names have been place in: ",file2Name)
    
main()
