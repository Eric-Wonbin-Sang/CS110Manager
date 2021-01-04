def main():
    print("This program will take a file by the name of Before.txt and reformat the names to be fully capitalized in a new file called After.txt.")
    x = open('Before.txt', "r")
    y = open('After.txt', "w")
    for i in x:
        data = i.upper()
        print(data, file=y)
    x.close()
    y.close()
main()
