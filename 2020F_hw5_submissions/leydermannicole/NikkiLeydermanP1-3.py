#I pledge my honor that I have abided by the Stevens Honor System
def squareValues(values):
    squared_values= int(values)**2
    return squared_values
def main():
    values= input("Enter a list of values separated by a comma:")
    new_values=values.split(',')
    for num in new_values:
        print(squareValues(num))
main()