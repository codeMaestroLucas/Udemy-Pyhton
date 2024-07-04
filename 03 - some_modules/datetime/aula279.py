# CALENDARS

def main() -> None:
    """Function used to run the main code."""
    import calendar
    
    print(calendar.month(2024, 1)) # January

    print(calendar.monthrange(2024, 12))
    # The fist value represents the day of the week
    # The second value represents the day
    
    print(calendar.weekday(2024, 12, 4))
    




if __name__ == '__main__':
    main()