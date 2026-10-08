def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("BMI")
   
    try:
        weight = float(input("pls enter your weight in kg: "))
        height = float(input("pls enter your height in m: "))
       
        if height <= 0 or weight <= 0:
            print("weight and height must be posstive.")
            return
       
        bmi = calculate_bmi(weight, height)
       
        print(f"your body mass index: {bmi:.2f}")
       
        if bmi < 18.5:
            print("you are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("your weight is normal.")
        elif 25 <= bmi < 29.9:
            print("you are overweight.")
        else:
            print("you are obese.")

    except ValueError:
        print("pls enter posstive number.")

if __name__ == "__main__":
    main()