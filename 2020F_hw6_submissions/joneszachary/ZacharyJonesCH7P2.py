#I pledge my honor that I have abided by the Stevens Honor System.
#Zachary Jones
#HW6 Problem 2

import datetime


def get_date():
    date = str(input('Enter date M/D/YYYY: '))
    return date


def validate_date(date):
    format = '%m/%d/%Y'
    try:
        datetime.datetime.strptime(date, format)
        print('{} is a valid date.'.format(date))

    except ValueError:
        print('{} is an invalid date.'.format(date))


validate_date(
    get_date()
)