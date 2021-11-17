from datetime import datetime, timedelta
from random import randint

def lie_date(to_format=True):
    '''
    '''

    today = datetime.today().date().strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
    r = today - timedelta(days=randint(20, 400))
    return r if not to_format else r.strftime('%Y-%m-%d %H:%M:%S')

def lie_time(to_format=True):
    '''
    '''

    r = lie_date(False)
    r += timedelta(
        hours= randint(7, 23),
        minutes=randint(0, 60),
        seconds=randint(0, 60)
    )
    return r if not to_format else r.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print(lie_date())
    print(lie_time())