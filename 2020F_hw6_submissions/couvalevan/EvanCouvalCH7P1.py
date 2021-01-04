def main():
    weight = int(input("please enter your weight in pounds: "))
    height = int(input("please enter your height in inches: "))
    bmi = (weight * 720)/(height**2)
    if bmi >= 19 and bmi <= 25:
        health = "healthy"
    else:
         health = "unhealthy"

    print(bmi)
    print(health)

main()