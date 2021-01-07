import pandas as pd

import arrow
from datetime import date

import datetime

class Timer():

    def __init__(self):
        self.start_time = self.now()
        self.end_time = None
        self.elapse = None

    def now(self):
        return arrow.now().format('YYYY-MM-DD hh:mm')

    def elapse_time(self, unit='minute'):
        unit_list = ['minute', 'second', 'hours']
        if unit not in unit_list:
            raise ValueError('unit_list : {} '.format(unit_list))
        self.end_time = self.now()
        self.elapse = (self.end_time - self.start_time)

        if unit == 'second':
            return self.elapse.seconds
        elif unit == 'minute':
            return self.elapse.seconds / 60
        else:
            return self.elapse.seconds / 3600

def days_between(d1, d2):
    delta = d1 - d2
    return delta.days


def check_freq(freq):
    freqs = ['D', 'W', 'M']
    if freq not in freqs:
        raise ValueError('freq :{} must in {}'.format(freq, freqs))
    pass


def shift_week_start(date):
    date = arrow.get(date)
    week_day = date.weekday()
    date = date.shift(days=-week_day)
    date = date.format('YYYY-MM-DD')
    return date


def shift_week_end(date):
    date = arrow.get(date)
    # shift to next week
    r = pd.date_range(start=date.format('YYYY-MM-DD'), periods=1, freq='W')
    # get date
    r = pd.to_datetime(r)
    date = arrow.get(r[0]).format('YYYY-MM-DD')
    return date


def shift_week_periods_end(peroids, date):
    date = arrow.get(date)
    # shift to next week
    r = pd.date_range(start=date.shift(weeks=peroids).format('YYYY-MM-DD'), periods=1, freq='W')
    # get date
    r = pd.to_datetime(r)
    date = arrow.get(r[0]).format('YYYY-MM-DD')
    return date


def shift_month_periods_end(peroids, date):
    date = arrow.get(date)
    # cur month
    date = date.format('YYYY-MM')
    date = arrow.get(date)
    date = date.shift(months=peroids + 1)
    # shift to month last day
    return date.shift(days=-1).format('YYYY-MM-DD')


def shift_month_end(date):
    date = arrow.get(date)
    # shift to next month
    date = date.shift(months=1).format('YYYY-MM')
    date = arrow.get(date)
    # shift to month last day
    return date.shift(days=-1).format('YYYY-MM-DD')


def shift_month_start(date):
    date = arrow.get(date)
    # shift to next month
    date = date.format('YYYY-MM')
    date = arrow.get(date)
    # shift to month last day
    return date.format('YYYY-MM-DD')


def shift_yesterday():
    date = arrow.now()
    date = date.shift(days=-1)
    return date.format('YYYY-MM-DD')
