def convert_length(value, from_unit, to_unit):
    # تعریف مقادیر معادل هر واحد به متر
    units_to_meters = {
        'M': 1,
        'CM': 0.01,
        'KM': 1000
    }
   
    if from_unit not in units_to_meters or to_unit not in units_to_meters:
        return "the unit is not availble."
   
    # تبدیل مقدار به متر و سپس به واحد مقصد
    value_in_meters = value * units_to_meters[from_unit]
    converted_value = value_in_meters / units_to_meters[to_unit]
   
    return converted_value

def main():
    print("lengh conversion program")
   
    while True:
        try:
            value = float(input("enter amount:"))
            from_unit = input("source unit(M,CM,KM): ")
            to_unit = input("destination unit(M,CM,KM): ")
           
            result = convert_length(value, from_unit, to_unit)
           
            if isinstance(result, str):
                print(result)
            else:
                print(f"{value} {from_unit} is equal to {result} {to_unit}")
               
        except ValueError:
            print("pls enter availble unit.")
       
        play_again = input("do you want unit again: ").lower()
        if play_again != 'yes':
            break

main()