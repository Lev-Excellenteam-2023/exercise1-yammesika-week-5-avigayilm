from datetime import datetime


def days_until_future_date(future_date):
    """
    This function receives a future date in the format YYYY-MM-DD and
    prints the number of days remaining until we reach the expected date.
    """
    future_date_obj = datetime.strptime(dateObject,"%Y/%m/%d").date()
    today = datetime.today().date()
    remaining_days = (future_date_obj - today).days

    if remaining_days > 0:
        print(f"There are {remaining_days} days until {future_date}")
    elif remaining_days == 0:
        print(f"Today is {future_date}!")
    else:
        print(f"{future_date} has already passed.")


dateObject=input("enter date (in YYYY/MM/DD)\n")
days_until_future_date(dateObject)