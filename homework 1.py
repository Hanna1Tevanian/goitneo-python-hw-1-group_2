from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    birthdays = defaultdict(list)

    for user in users:
        name, bday = user["name"], user["birthday"].date()
        bday_this_year = bday.replace(year=today.year)

        if bday_this_year < today:
            bday_this_year = bday.replace(year=today.year + 1)

        delta_days = (bday_this_year - today).days

        if 0 <= delta_days <= 14:
            weekday = (today + timedelta(days=delta_days)).strftime('%A')
            weekday = 'Monday' if weekday in ('Saturday', 'Sunday') else weekday
            birthdays[weekday].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

    return birthdays

users = [
    {"name": "Bill Gates", "birthday": datetime(2023, 12, 20)},  # Within next two weeks
    {"name": "Jan Koum", "birthday": datetime(1995, 4, 24)},  # Outside next two weeks
]

print(get_birthdays_per_week(users))