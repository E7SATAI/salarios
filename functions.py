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


def calculate_level_rate(row):
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


def change_level_to_numbers(row):
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


def change_state_to_number(row):
    if row['state'] == 'Aguascalientes':
        return 1
    elif row['state'] == 'Baja California':
        return 2
    elif row['state'] == 'Baja California Sur':
        return 3
    elif row['state'] == 'Campeche':
        return 4
    elif row['state'] == 'Chiapas':
        return 5
    elif row['state'] == 'Chihuahua':
        return 6
    elif row['state'] == 'Ciudad de Mxico':
        return 7
    elif row['state'] == 'Coahuila':
        return 8
    elif row['state'] == 'Colima':
        return 9
    elif row['state'] == 'Durango':
        return 10
    elif row['state'] == 'Estado de Mxico':
        return 11
    elif row['state'] == 'Guanajuato':
        return 12
    elif row['state'] == 'Guerrero':
        return 13
    elif row['state'] == 'Hidalgo':
        return 14
    elif row['state'] == 'Jalisco':
        return 15
    elif row['state'] == 'Michoac\xa0n' or row['state'] == 'Michoac n' or row['state'] == 'Michoac�n' or row['state'] == 'Michoacán':
        return 16
    elif row['state'] == 'Morelos':
        return 17
    elif row['state'] == 'Nayarit':
        return 18
    elif row['state'] == 'Nuevo Le¢n':
        return 19
    elif row['state'] == 'Oaxaca':
        return 20
    elif row['state'] == 'Puebla':
        return 21
    elif row['state'] == 'Queretaro':
        return 22
    elif row['state'] == 'Quintana Roo':
        return 23
    elif row['state'] == 'San Luis Potos¡':
        return 24
    elif row['state'] == 'Sinaloa':
        return 25
    elif row['state'] == 'Sonora':
        return 26
    elif row['state'] == 'Tabasco':
        return 27
    elif row['state'] == 'Tamaulipas':
        return 28
    elif row['state'] == 'Tlaxcala':
        return 29
    elif row['state'] == 'Veracruz':
        return 30
    elif row['state'] == 'Yucat\xa0n' or row['state'] == 'Yucat n' or row['state'] == 'Yucat�n' or row['state'] == 'Yúcatan':
        return 31
    elif row['state'] == 'Zacatecas':
        return 32
    elif row['state'] == 'Nacional':
        return 33


def change_year_to_number(row):
    if row['year'] == 2005:
        return 5
    elif row['year'] == 2006:
        return 6
    elif row['year'] == 2007:
        return 7
    elif row['year'] == 2008:
        return 8
    elif row['year'] == 2009:
        return 9
    elif row['year'] == 2010:
        return 10
    elif row['year'] == 2011:
        return 11
    elif row['year'] == 2012:
        return 12
    elif row['year'] == 2013:
        return 13
    elif row['year'] == 2014:
        return 14
    elif row['year'] == 2015:
        return 15
    elif row['year'] == 2016:
        return 16
    elif row['year'] == 2017:
        return 17
    elif row['year'] == 2018:
        return 18
    elif row['year'] == 2019:
        return 19


def save_image(df, image_name):
    df.plot().get_figure().savefig('website/img/' + image_name)


def save_image_bar(df, image_name):
    df.plot.bar().get_figure().savefig('website/img/' + image_name)
