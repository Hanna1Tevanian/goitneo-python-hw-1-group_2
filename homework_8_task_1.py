from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthday_d = defaultdict(list)
    
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_year = birthday.replace(year=today.year)
        
        if birthday_year < today:
            birthday_year = birthday_year.replace(year=today.year + 1)
        
        delta_days = (birthday_year - today).days
        
        if delta_days < 7:
            day_week = (today + timedelta(days=delta_days)).strftime("%A")
        else:
            continue
        
        birthday_d[day_week].append(name)
    
    for day, names in birthday_d.items():
        print(f"{day}: {', '.join(names)}")


