def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_user_data(user_number):
    print(f" enter information user {user_number}:")
   
    try:
        weight = float(input("pls enter your weight in kg: "))
        height = float(input("pls enter your height in m: "))
       
        if height <= 0 or weight <= 0:
            print("weight and height must be posstive.")
            return None, None
       
        return weight, height
   
    except ValueError:
        print("your body mass index.")
        return None, None

def main():
    print("bmi 2 user")
   
    for user in range(1, 3):  # برای دو کاربر
        weight, height = get_user_data(user)
       
        if weight is not None and height is not None:
            bmi = calculate_bmi(weight, height)
            print(f"your body mass index {user}: {bmi:.2f}")
           
            if bmi < 18.5:
                print("you are underweight.")
            elif 18.5 <= bmi < 24.9:
                print("your weight is normal.")
            elif 25 <= bmi < 29.9:
                print("you are overweight.")
            else:
                print("you are obese.")

if __name__ == "__main__":
    main()