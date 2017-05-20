#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import datetime
import numpy    as np
import pandas   as pd
import myutils
'''
This script is to be run by pytest module.
'''

def main():
    pass


def test_find_month():
    d1 = datetime.date(2015, 1, 1)
    # assert myutils.find_month(''    ) == ValueError
    assert myutils.find_month(d1,  0) == datetime.date(2015,  1,  1)
    assert myutils.find_month(d1,  3) == datetime.date(2015,  4,  1)
    assert myutils.find_month(d1, -3) == datetime.date(2014, 10,  1)

    d2 = datetime.datetime(2016, 3, 1, 7, 15, 30)
    assert myutils.find_month(d2,  0) == datetime.datetime(2016,  3,  1, 7, 15, 30)
    assert myutils.find_month(d2,  3) == datetime.datetime(2016,  6,  1, 7, 15, 30)
    assert myutils.find_month(d2, -3) == datetime.datetime(2015, 12,  1, 7, 15, 30)


def test_first_date_of_month():
    d1 = datetime.date(2015, 2, 28)
    assert myutils.first_date_of_month(d1) == datetime.date(2015, 2, 1)

    d2 = datetime.date(2016, 2, 29)
    assert myutils.first_date_of_month(d2) == datetime.date(2016, 2, 1)


def test_last_date_of_month():
    d1 = datetime.date(2015, 2, 1)
    assert myutils.last_date_of_month(d1) == datetime.date(2015, 2, 28)

    d2 = datetime.date(2016, 2, 1)
    assert myutils.last_date_of_month(d2) == datetime.date(2016, 2, 29)


def test_pd_ts():
    d1  = datetime.date(2015, 2, 28)
    ts1 = pd.Timestamp(datetime.date(year=2015, month=2, day=28), freq='M')

    assert myutils.pd_ts(d1) == ts1


def test_is_ymd():
    assert myutils.is_ymd('2015-03-01') == datetime.date(2015, 3, 1)
    assert myutils.is_ymd('2015/03/01') == datetime.date(2015, 3, 1)
    assert myutils.is_ymd('20170519')   == datetime.date(2017, 5, 19)
    assert myutils.is_ymd('170519')     == datetime.date(2017, 5, 19)
    assert myutils.is_ymd('something')  == False


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0])[:-3] + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    # main()
