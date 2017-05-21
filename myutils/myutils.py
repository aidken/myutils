#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import datetime
import calendar

import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt


def find_month(source_month, months_increment):
    '''
    Find n months after source month. Be careful: the day value of the `datetime <https://docs.python.org/3/library/datetime.html>`_ object that is to be returned is always set to day 1.

    Examples:
        find_month( datetime.date(2015, 1, 1), 1 ) => datetime.date(2015, 2, 1)

        find_month( datetime.date(2015, 1, 1), 3 ) => datetime.date(2015, 4, 1)

        find_month( datetime.date(2015, 1, 1), -3 ) => datetime.date(2014, 10, 1)

        find_month( datetime.date(2015, 1, 1), 0 ) => datetime.date(2015, 1, 1)

        find_month( datetime.date(2015, 1, 28), 0 ) => datetime.date(2015, 1, 1)

        find_month( datetime.date(2015, 1, 28), 3 ) => datetime.date(2015, 4, 1)

        find_month( datetime.datetime(2016, 3, 1, 7, 15, 30), -3 ) => datetime.datetime(2015, 12,  1, 7, 15, 30)

    Parameters:
        source_month (datetime.date or datetime.datetime): The starting point.
        months_increment (int): Set 1 if you want to find a month 1 months after source_month.

    Returns:
        A datetime.date object, or a datetime.datetime.object. If you give a datetime.date object as source_month, this function returns a datetime.date object. If you give a datetime.datetime.object, this function returns a datetime.datetime object.

        The day value is always set to 1, no matter what day you give as source_month.

    '''
    if source_month is None or (type(source_month) is not datetime.date and type(source_month) is not datetime.datetime):
        raise ValueError('Source month given is not either datetime.date or datetime.datetime. It is {}.'.format(type(source_month)))
    elif months_increment is None or type(months_increment) is not int:
        raise ValueError('Months increment given is not an int. It is {}.'.format(type(months_increment)))
    else:
        tmp = source_month
        count = 0
        if months_increment==0:
            return source_month.replace(day=1)
        elif months_increment > 0:
            while count < months_increment:
                # find last date of the month
                first_day, last_day = calendar.monthrange(tmp.year, tmp.month)
                tmp = tmp.replace(day=last_day)
                tmp = tmp + datetime.timedelta(days=1)
                count += 1
            return tmp
        elif months_increment < 0:
            while count > months_increment:
                # find last date of the month
                first_day, last_day = calendar.monthrange(tmp.year, tmp.month)
                tmp = tmp.replace(day=1)
                tmp = tmp - datetime.timedelta(days=1)
                tmp = tmp.replace(day=1)
                count -= 1
            return tmp


def first_date_of_month(source_month):
    if source_month is None or (type(source_month) is not datetime.date and type(source_month) is not datetime.datetime):
        raise ValueError('Source month given is not either datetime.date or datetime.datetime. It is {}.'.format(type(source_month)))
    else:
        # first_day, last_day = calendar.monthrange(source_month.year, source_month.month)
        return source_month.replace(day=1)


def last_date_of_month(source_month):
    if source_month is None or (type(source_month) is not datetime.date and type(source_month) is not datetime.datetime):
        raise ValueError('Source month given is not either datetime.date or datetime.datetime. It is {}.'.format(type(source_month)))
    else:
        _, last_day = calendar.monthrange(source_month.year, source_month.month)
        return source_month.replace(day=last_day)


def pd_ts(source_month):
    '''
    This function converts a datetime.date object to a pandas.Timestamp with freq being 'M'.

    The reason I created this function is that I have a lot of text files of monthly data, and convert and combine them to one large time series over many months.

        pd_ts( datetime.date(2015, 2, 28) ) => pandas.Timestamp(datetime.date(year=2015, month=2, day=28), freq='M')


    Okay, now I'm thinking I don't have to create a function like this. The following simple expression achieves the exact same goal I wanted to achieve.

        pandas.Timestamp(datetime.date(2015, 2, 28), freq='M')

    Parameters:
        source_month (datetime.date or datetime.datetime):

    '''
    if type(source_month) is not datetime.date and type(source_month) is not datetime.datetime:
        raise ValueError('Argument must be datetime.date or datetime.datetime. Given argument {} is a {}.'.format(
            source_month,
            type(source_month)
        ))
    else:
        # _, last_day = calendar.monthrange(source_month.year, source_month.month)
        return pd.Timestamp(datetime.date(year=source_month.year, month=source_month.month, day=source_month.day), freq='M')


def is_ymd(tmp_str):
    '''
    Determines if given argument is a string that seems to be a date value.
    If it is, then this function returns datetime.date object. If not, it returns False.

    Following strings are understood as a valid date value by this function.

    Examples:
        '2017-05-19' => datetime.date(2017, 5, 19)

        '2017/05/19' => datetime.date(2017, 5, 19)

        '20170519'   => datetime.date(2017, 5, 19)

        '170519'     => datetime.date(2017, 5, 19)

        'hello!'     => False

    Parameters:
        tmp_str (str): a string that you want to determine if it's a date value.

    Returns:
        A datetime.date object if this function finds tmp_str it's given is understood as a date value.
        False is returned if the function finds it's not understood as a date value.

    '''
    tmp_str=str(tmp_str)
    if len(tmp_str)==10:
        try:
            m = datetime.datetime.strptime(tmp_str, '%Y-%m-%d')
            return datetime.date(
                year  = m.year,
                month = m.month,
                day   = m.day,
            )
        except:
            try:
                m = datetime.datetime.strptime(tmp_str, '%Y/%m/%d')
                return datetime.date(
                    year  = m.year,
                    month = m.month,
                    day   = m.day,
                )
            except:
                return False
    elif len(tmp_str)==8:
        try:
            m = datetime.datetime.strptime(tmp_str, '%Y%m%d')  # e.g. '20170519'
            return datetime.date(
                year  = m.year,
                month = m.month,
                day   = m.day,
            )
        except:
            return False
    elif len(tmp_str)==6:
        try:
            m = datetime.datetime.strptime(tmp_str, '%y%m%d')  # e.g. '170519'
            return datetime.date(
                year  = m.year,
                month = m.month,
                day   = m.day,
            )
        except:
            return False
    else:
        return False


def main():
    pass


def test():
    pass


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0])[:-3] + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    main()
