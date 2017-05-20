#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import datetime
import calendar

import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt


def find_month(source_month=None, months_increment=None):
    '''
    2017-05-04 21:55:27
    Find n months after source month.
    '''
    if source_month is None or (type(source_month) is not datetime.date and type(source_month) is not datetime.datetime):
        raise ValueError('Source month given is not either datetime.date or datetime.datetime. It is {}.'.format(type(source_month)))
    elif months_increment is None or type(months_increment) is not int:
        raise ValueError('Months increment given is not an int. It is {}.'.format(type(months_increment)))
    else:
        tmp = source_month
        count = 0
        if months_increment==0:
            return tmp
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


def first_date_of_month(source_month=None):
    if source_month is None or (type(source_month) is not datetime.date and type(source_month) is not datetime.datetime):
        raise ValueError('Source month given is not either datetime.date or datetime.datetime. It is {}.'.format(type(source_month)))
    else:
        # first_day, last_day = calendar.monthrange(source_month.year, source_month.month)
        return source_month.replace(day=1)


def last_date_of_month(source_month=None):
    if source_month is None or (type(source_month) is not datetime.date and type(source_month) is not datetime.datetime):
        raise ValueError('Source month given is not either datetime.date or datetime.datetime. It is {}.'.format(type(source_month)))
    else:
        _, last_day = calendar.monthrange(source_month.year, source_month.month)
        return source_month.replace(day=last_day)


def pd_ts(source_month):
    if type(source_month) is not datetime.date and type(source_month) is not datetime.datetime:
        raise ValueError('Argument must be datetime.date or datetime.datetime. Given argument {} is a {}.'.format(
            source_month,
            type(source_month)
        ))
    else:
        # _, last_day = calendar.monthrange(source_month.year, source_month.month)
        return pd.Timestamp(datetime.date(year=source_month.year, month=source_month.month, day=source_month.day), freq='M')


def is_ymd(tmp):
    tmp=str(tmp)
    if len(tmp)==10:
        try:
            m = datetime.datetime.strptime(tmp, '%Y-%m-%d')
            return datetime.date(
                year  = m.year,
                month = m.month,
                day   = m.day,
            )
        except:
            try:
                m = datetime.datetime.strptime(tmp, '%Y/%m/%d')
                return datetime.date(
                    year  = m.year,
                    month = m.month,
                    day   = m.day,
                )
            except:
                return False
    elif len(tmp)==8:
        try:
            m = datetime.datetime.strptime(tmp, '%Y%m%d')  # e.g. '20170519'
            return datetime.date(
                year  = m.year,
                month = m.month,
                day   = m.day,
            )
        except:
            return False
    elif len(tmp)==6:
        try:
            m = datetime.datetime.strptime(tmp, '%y%m%d')  # e.g. '170519'
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
