import datetime

def jalali_to_gregorian(jalali_year, jalali_month, jalali_day):
    """
    Converts a Jalali (Persian) date to a Gregorian date.

    Args:
        jalali_year (int): The Jalali year.
        jalali_month (int): The Jalali month (1-12).
        jalali_day (int): The Jalali day (1-31).

    Returns:
        tuple: A tuple containing the Gregorian year, month, and day.
    """
    jd = jalali_to_jd(jalali_year, jalali_month, jalali_day)
    return jd_to_gregorian(jd)

def gregorian_to_jalali(gregorian_year, gregorian_month, gregorian_day):
    """
    Converts a Gregorian date to a Jalali (Persian) date.

    Args:
        gregorian_year (int): The Gregorian year.
        gregorian_month (int): The Gregorian month (1-12).
        gregorian_day (int): The Gregorian day (1-31).

    Returns:
        tuple: A tuple containing the Jalali year, month, and day.
    """
    jd = gregorian_to_jd(gregorian_year, gregorian_month, gregorian_day)
    return jd_to_jalali(jd)

def jalali_to_jd(jalali_year, jalali_month, jalali_day):
    """
    Converts a Jalali date to Julian Day Number.
    """
    # ... (Calculations for converting Jalali to Julian Day Number) ...
    # This section requires complex calculations and is outlined briefly here.
    # You can use existing libraries for this purpose, such as jdatetime.
    # This code is just an example and may need adjustments.
    jd = (jalali_year - 622) * 365 + (jalali_year - 622) // 4 - (jalali_year - 622) // 100 + (jalali_year - 622) // 400 + \
         ((jalali_month + 9) * 306) // 10 + (jalali_month + 9) // 10 + jalali_day - 1720
    return jd

def jd_to_gregorian(jd):
    """
    Converts Julian Day Number to a Gregorian date.
    """
    # ... (Calculations for converting Julian Day Number to Gregorian) ...
    # This section also requires complex calculations and is outlined briefly here.
    # You can use existing libraries for this purpose.
    a = (jd + 1721425) // 365
    b = 4 * a + 3
    c = ((jd + 1721425) % 365) // 30
    d = (jd + 1721425) % 30
    m = c + 1 if c >= 9 else c + 3
    y = a - 4716 if m > 12 else a - 4715
    return y, m, d

def jd_to_jalali(jd):
    """
    Converts Julian Day Number to a Jalali (Persian) date.
    """
    # ... (Calculations for converting Julian Day Number to Jalali) ...
    # This section also requires complex calculations and is outlined briefly here.
    # You can use existing libraries for this purpose.
    jd -= 3652425
    jd += 1
    h = jd / 3652425
    j = 365 * h
    j = j + (int(j) % 365)
    g = int(j / 30)
    r = j % 30
    m = g + 1 if g < 12 else g - 12
    y = 1600 + int((78 + m) / 12)
    y = y + (int(j) / 365) - (int(j) / 365)
    return y, m, r

if __name__ == "__main__":
    # Example: Converting Jalali to Gregorian
    jalali_year = 1402
    jalali_month = 7
    jalali_day = 27
    gregorian_year, gregorian_month, gregorian_day = jalali_to_gregorian(jalali_year, jalali_month, jalali_day)
    print(f"Jalali Date: {jalali_year}-{jalali_month}-{jalali_day}")
    print(f"Gregorian Date: {gregorian_year}-{gregorian_month}-{gregorian_day}")

    # Example: Converting Gregorian to Jalali
    gregorian_year = 2023
    gregorian_month = 10
    gregorian_day = 27
    jalali_year, jalali_month, jalali_day = gregorian_to_jalali(gregorian_year, gregorian_month, gregorian_day)
    print(f"Gregorian Date: {gregorian_year}-{gregorian_month}-{gregorian_day}")
    print(f"Jalali Date: {jalali_year}-{jalali_month}-{jalali_day}")