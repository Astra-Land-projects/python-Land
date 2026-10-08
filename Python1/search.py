def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
       
        # بررسی اینکه آیا عنصر میانه همان هدف است
        if arr[mid] == target:
            return mid
        # اگر هدف بزرگتر از عنصر میانه باشد، به نیمه راست بروید
        elif arr[mid] < target:
            left = mid + 1
        # اگر هدف کوچکتر از عنصر میانه باشد، به نیمه چپ بروید
        else:
            right = mid - 1
           
    return -1  # اگر عنصر پیدا نشود

# مثال استفاده
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11]
    target_value = int(input("pls enter your number: "))
   
    result_index = binary_search(numbers, target_value)
   
    if result_index != -1:
        print(f"number {target_value} at index {result_index} receive.")
    else:
        print("your number is not list.")