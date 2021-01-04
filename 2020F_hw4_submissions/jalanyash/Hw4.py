#I pledge that I have abided by the Stevens Honors System-Yash Jalan


def main():
    first = open("Before.txt", "r")
    revised = open("After.txt", "w")
    for l in first:
        names = l.upper()
        print(names,file=revised)
    first.close()
    revised.close()
main()