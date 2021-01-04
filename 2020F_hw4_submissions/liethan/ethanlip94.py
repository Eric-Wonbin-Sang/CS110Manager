def main():
    before = open("Before.txt", "r")
    after = open("After.txt", "w")
    for i in before:
        export = i.upper()
        print(export)
        print(export, file=after)
    before.close()
    after.close()
main()