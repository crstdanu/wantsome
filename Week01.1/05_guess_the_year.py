import datetime
# am importat modulul "datetime"

today_date = datetime.date.today() 

age = int(input("Enter your age: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

birth_year = today_date.year - age

if (birth_month > today_date.month) or (birth_month == today_date.month and birth_day > today_date.day): birth_year -= 1

print(f"Your birth year is {birth_year}")
