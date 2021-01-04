def main():
    bef = open("Before.txt", "r")
    aft = open("After.txt", "w")
    for i in bef:
        Uname = i.upper()
        print(Uname, file=aft)
    bef.close()
    aft.close()
main()
