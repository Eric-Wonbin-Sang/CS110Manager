#I pledge my honor that I have abided by the Stevens Honor Code
#Number 1

def main ():
    list_1 = input("Enter a list of numbers where each are seperated by a space:")
    changed_list = list_1.split ()
    list_2 = []
    for i in changed_list:
        list_2.append(int(i) **2)
    print(list_2)
main()
