#i pledge my honor that I have abided by the Stevens Honor System :)
# Benjamin Otto

#HW 4

def main():
    before=open("Before.txt","r")
    after=open("After.txt","w")
    for line in before:
        after.write(line.upper() + "\n")
    before.close()
    after.close()
main()