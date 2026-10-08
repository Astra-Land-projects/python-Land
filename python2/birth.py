birthdays = {
    "علی": "1370/07/15",
    "مریم": "1375/03/20",
    "رضا": "1380/11/05"
}

import datetime

today = datetime.date.today()

for name, birthday in birthdays.items():
    year, month, day = map(int, birthday.split("/"))
    birthday_date = datetime.date(year, month, day)

    if birthday_date.month == today.month and birthday_date.day == today.day:
        print(f"امروز تولد {name} هست! 🎉")