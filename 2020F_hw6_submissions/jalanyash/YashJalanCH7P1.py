# I pledge my honor that I have abided by the Stevens Honors System
def main():
    print("This program will calculate your Body Mass Index")
    weight =float(input("Enter your weight in pounds:"))
    height =float(input("Enter your height in inches:"))
    body_mass_index = (weight*720)/(height**2)
    if body_mass_index>= 19 and body_mass_index<= 25:
        print("Your Body Mass Index of",body_mass_index, "is healthy")
    elif body_mass_index<19:
        print("Your Body Mass Index of", body_mass_index, "is below a healthy level")
    else:
        print("Your Body Mass Index is", body_mass_index, "above a healthy level")
main()