def search_file(file_path, keyword):
    """
    فایل متنی رو جستجو می‌کنه و خطوطی که شامل کلمه کلیدی هستن رو نمایش می‌ده.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        results = []
        for line in lines:
            if keyword.lower() in line.lower():
                results.append(line.strip())

        if results:
            print("result search:")
            for line in results:
                print(line)
        else:
            print("any result not find.")

    except FileNotFoundError:
        print("file not find.")
    except Exception as e:
        print(f"error: {e}")

# مثال استفاده
file_path = 'sample.txt'  # مسیر فایل متنی
keyword = 'python'  # کلمه کلیدی مورد نظر

search_file(file_path, keyword)