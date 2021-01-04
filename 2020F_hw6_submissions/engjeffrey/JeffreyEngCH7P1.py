# I pledge my honor that I have abided by the Stevens Honor System.
# Jeffrey Eng

def bmicalc(w, h):
    bmi = w * 720 / (h ** 2)
    return bmi

def main():
    weight = float(input("What is your weight in pounds? "))
    height = float(input("What is your height in inches? "))
    x = bmicalc(weight, height)
    if x >= 19 and x <= 25:
        print("You are within the healthy range.")
    elif x < 19:
        print("You are below the healthy range.")
    else:
        print("You are above the healthy range.")
main()
