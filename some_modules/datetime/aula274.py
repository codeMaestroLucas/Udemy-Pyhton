# DATETIME

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# For use other TimeZones u need to install pytz types-pytz
from pytz import timezone

def main() -> None:
    """Function used to run the main code."""
    d1 = datetime(2024, 5, 21, 14, 41, 6)
    print(d1)

    d2 = datetime.now()
    print(d2)


    print('FORMATING DATA')
    date_str = '21/05/2024 14:41:06'
    date_fmt= r'%d/%m/%Y %H:%M:%S'
    d3 = datetime.strptime(date_str, date_fmt)
    print(d3.strftime('%d/%M/%Y %Hh%Mm%Ss'))
    
    print('TIMEZONES')
    d4 = datetime.now(timezone('Asia/Tokyo'))
    print(d4)

    print('DELTA TIME')
    d_init = datetime.strptime('21/05/2023 14:41:06', date_fmt)
    d_end = datetime.strptime('24/07/2024 11:04:00', date_fmt)
    delta = d_end - d_init

    print(delta)
    print('DAYS: ', delta.days)
    print('MICROSEC: ', delta.microseconds)
    print('SECONDS: ', delta.seconds)
    
    delta2 = timedelta(days= 74, hours= 22) # Adding 34 days and 2h
    print(d_init + delta2)
    
    delta3 = relativedelta(d_end, d_init)
    print(delta3)


if __name__ == '__main__':
    main()