from datetime import datetime, timedelta

users = [
    {'name': 'Bill', 'birthday': datetime(2023, 8, 14)},
    {'name': 'Jill', 'birthday': datetime(2023, 8, 19)},
    {'name': 'Kim', 'birthday': datetime(2023, 8, 18)},
    {'name': 'Jan', 'birthday': datetime(2023, 8, 20)},
    {'name': 'Alex', 'birthday': datetime(2023, 8, 21)},
]

def get_birthdays_per_week(users):

    current_day = datetime.now().date()
    next_week_start = current_day + timedelta(days=(7 - current_day.weekday()))
    next_week_end = next_week_start + timedelta(days=7)

    b_day_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    for user in users:
        name = user.get("name")
        birthday = user.get("birthday").date()

        if current_day <= birthday < next_week_end:
            if birthday.weekday() >= 5:
                birthday = birthday + timedelta(days=(7 - birthday.weekday()))

            weekday = birthday.strftime("%A")
            b_day_dict[weekday].append(name)

    for weekday, names in b_day_dict.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

get_birthdays_per_week(users)