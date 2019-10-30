#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:29:57 2019

@author: skuarch
"""

import variables


def calculate_rate(row):
    # 0 = equals, 1 = bad, 2 = good
    print(row)
    '''mean = row['mean_by_state_and_level']
    percentage = row['percentage_by_level_and_total_people_by_state_and_year']
    # less than one minimum salary
    if percentage < mean:
        row['rate_level'] = 2
    elif percentage > mean:
        row['rate_level'] = 1
    else:
        row['rate_level'] = 0
    '''


def calculate_rate_another(row):
    # 0 = equals, 1 = bad, 2 = good
    mean = row['mean_by_state_and_level']
    percentage = row['percentage_by_level_and_total_people_by_state_and_year']

    # less than one minimum salary
    if row['level'] == 1:
        if percentage < mean:
            return 2
        elif percentage > mean:
            return 1
        else:
            return 0

    # one_minimum_salary
    if row['level'] == 2:
        if percentage < mean:
            return 2
        elif percentage > mean:
            return 1
        else:
            return 0

    # more_than_1_until_2
    if row['level'] == 3:
        if percentage < mean:
            return 2
        elif percentage > mean:
            return 1
        else:
            return 0

    # more_than_2_until_3
    if row['level'] == 4:
        if percentage < mean:
            return 2
        elif percentage > mean:
            return 1
        else:
            return 0

    # more_than_3_until_5
    if row['level'] == 5:
        if percentage < mean:
            return 2
        elif percentage > mean:
            return 1
        else:
            return 0

    # more_than_5_until_10
    if row['level'] == 6:
        if percentage > mean:
            return 2
        elif percentage < mean:
            return 1
        else:
            return 0

    # more_than_10
    if row['level'] == 7:
        if percentage > mean:
            return 2
        elif percentage < mean:
            return 1
        else:
            return 0

    # no_incoming
    if row['level'] == 8:
        if percentage < mean:
            return 2
        elif percentage > mean:
            return 1
        else:
            return 0

    # not_specified
    if row['level'] == 9:
        return 0


def change_level_value_name(row):
    if row['level'] == variables.less_than_minimum_salary:
        return 1
    elif row['level'] == variables.one_minimum_salary:
        return 2
    elif row['level'] == variables.more_than_1_until_2:
        return 3
    elif row['level'] == variables.more_than_2_until_3:
        return 4
    elif row['level'] == variables.more_than_3_until_5:
        return 5
    elif row['level'] == variables.more_than_5_until_10:
        return 6
    elif row['level'] == variables.more_than_10:
        return 7
    elif row['level'] == variables.no_incoming:
        return 8
    elif row['level'] == variables.not_specified:
        return 9


def save_image(df, image_name):
    df.plot().get_figure().savefig('website/img/' + image_name)


def save_image_bar(df, image_name):
    df.plot.bar().get_figure().savefig('website/img/' + image_name)
