def check_water_temperature(temperature):
    if temperature <= 0:
        return "water will ice."
    elif 0 < temperature < 100:
        return "water is mild."
    else:
        return "water will boils."

def main():
    print("program water")
   
    try:
        temperature = float(input("pls enter water degree in silicus: "))
       
        result = check_water_temperature(temperature)
        print(result)

    except ValueError:
        print("pls enter posstive number:.")

if __name__ == "__main__":
    main()