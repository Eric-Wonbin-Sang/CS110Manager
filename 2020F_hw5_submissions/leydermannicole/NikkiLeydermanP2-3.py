#I pledge my honor that I have abided by the Stevens Honor System
def sumValues(values):
    total=0
    for i in values:
        total+=int(i)
    return total
def main():
    values=input("Enter a list of values separated by a comma:")
    new_values=values.split(',')
    print(sumValues(new_values))
main()