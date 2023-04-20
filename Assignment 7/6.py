def calculate_time(days):
    years = days // 365
    months = (days % 365) // 30
    remaining_days = (days % 365) % 30
    print(years, "years,", months, "months and", remaining_days, "days")

days = int(input("Enter number of days: "))
calculate_time(days)
