import itertools

def count_three_digit_numbers():
    """
    Calculates the total count of 3-digit numbers formed using
    exactly two distinct digits chosen from 1 to 9.
    Both selected digits must appear in the number.
    """
   
    digits = list(range(1, 10))  # Digits 1 through 9
    valid_numbers = set()        # Use a set to store unique valid numbers
   
    # Step 1: Select two distinct digits from the list
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            num1 = digits[i]
            num2 = digits[j]
           
            # Step 2: Generate all 3-digit combinations using these two digits
            # itertools.product creates all permutations with repetition
            for combo in itertools.product([num1, num2], repeat=3):
               
                # Construct the 3-digit integer
                number = combo[0] * 100 + combo[1] * 10 + combo[2]
               
                # Condition: The number must contain BOTH selected digits
                # (e.g., exclude 111 or 222 if we picked 1 and 2)
                if num1 in combo and num2 in combo:
                    valid_numbers.add(number)
   
    return len(valid_numbers), sorted(list(valid_numbers))

# Execute the project
total_count, numbers_list = count_three_digit_numbers()

print(f"Total count of valid 3-digit numbers: {total_count}")
print(f"Sample of generated numbers: {numbers_list[:10]}...")