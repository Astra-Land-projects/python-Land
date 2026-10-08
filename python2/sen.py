def decimal_to_base(decimal_num, base):
    if decimal_num == 0:
        return "0"

    digits = []
    while decimal_num:
        digit = int(decimal_num % base)
        if digit < 10:
            digits.append(str(digit))
        else:
            digits.append(chr(ord('A') + digit - 10))
        decimal_num //= base

    return ''.join(digits[::-1])

def base_to_decimal(number, base):
    decimal_num = 0
    power = 0
    for digit in reversed(number):
        if '0' <= digit <= '9':
            digit_value = int(digit)
        else:
            digit_value = ord(digit) - ord('A') + 10
        decimal_num += digit_value * (base ** power)
        power += 1
    return decimal_num

def convert_base(number, from_base, to_base):
    decimal_value = base_to_decimal(number, from_base)
    converted_number = decimal_to_base(decimal_value, to_base)
    return converted_number

if __name__ == "__main__":
    number = input("enter number: ")
    from_base = int(input("enter start from...(16-2): "))
    to_base = int(input("enter end from...(16-2): "))

    converted_number = convert_base(number, from_base, to_base)
    print("the cheange number:", converted_number)