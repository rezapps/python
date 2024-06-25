# pylint: disable=bad-option-value, missing-function-docstring, inconsistent-return-statements, invalid-name, line-too-long, too-many-nested-blocks, missing-module-docstring
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import emission_data as eData

land = {}
for k, v in eData.country_data.items():
    land[v['id']] = k

capita = {}

for y in eData.country_data.values():
    capita[y['id']] = y['population']

area = {}
for z in eData.country_data.values():
    area[z['id']] = z['area']


def func12():
    sokOrd = input(
        'Enter country name or part of country name to see if exist: ')
    found = []
    for x in land:
        if sokOrd.lower() in x.lower():
            found.append(x)
    if len(found) >= 1:
        for country in found:
            print(country)
    else:
        print('No country matches your search!')


def func13():
    userInput = input(
        'Enter year and number of countries to show CO2 emissions: ')
    while userInput:
        choice = userInput.split(' ')
        userInput = ''
        if len(choice) == 2 and choice[0].isdigit() and choice[1].isdigit():
            year = choice[0]
            landNum = int(float(choice[1]))
            cap = 0
            printEmission(year, landNum, cap)
        elif len(choice) == 1 and choice[0].isdigit():
            cap = 0
            year = choice[0]
            landNum = 0
            printEmission(year, landNum, cap)
        else:
            func13()
            break


def func14():
    userInput = input(
        'Enter year and eventuell number of countries to show CO2 emissions per capita: ')
    while userInput:
        choice = userInput.split(' ')
        userInput = ''
        if len(choice) > 1 and choice[1].isdigit():
            landNum = int(float(choice[1]))
        else:
            landNum = 0
        cap = 0
        if choice[0].isdigit() and isinstance(landNum, int):
            year = choice[0]

            if year == '1990':
                cap = 1
            if year == '2005':
                cap = 2
            if year == '2017':
                cap = 3
            printEmission(year, landNum, cap)


def func15():
    userInput = input(
        'Enter year and eventuell number of countries to show CO2 emissions per area: ')
    while userInput:
        choice = userInput.split(' ')
        userInput = ''
        if len(choice) > 1 and choice[1].isdigit():
            landNum = int(float(choice[1]))
        else:
            landNum = 0

        sort_em_1 = {}
        sorted_cap = []
        i = 0
        if choice[0].isdigit() and isinstance(landNum, int):
            year = choice[0]

            target = 'emission_'+year
            if target == 'emission_1990':
                if landNum == 0:
                    for x in eData.emission_1990.items():
                        ind = x[0]
                        co2 = x[1]
                        if area[ind]:
                            sort_em_1[land[ind]] = (co2 * 1000000) / area[ind]
                        else:
                            sort_em_1[land[ind]] = 0.0
                    sorted_cap = []
                    sorted_cap = sorted(sort_em_1.items(),
                                        key=lambda x: x[1], reverse=True)
                    for lanCap in sorted_cap:
                        print(lanCap[0], ': ', lanCap[1])
                elif landNum > 0:
                    for x in eData.emission_1990.items():
                        ind = x[0]
                        co2 = x[1]
                        if area[ind]:
                            sort_em_1[land[ind]] = (co2 * 1000000) / area[ind]
                        else:
                            sort_em_1[land[ind]] = 0.0
                    sorted_cap = []
                    sorted_cap = sorted(sort_em_1.items(),
                                        key=lambda x: x[1], reverse=True)
                    while i < landNum:
                        print(sorted_cap[i][0], ': ', sorted_cap[i][1])
                        i += 1

            if target == 'emission_2005':
                if landNum == 0:
                    for x in eData.emission_2005.items():
                        ind = x[0]
                        co2 = x[1]
                        if area[ind]:
                            sort_em_1[land[ind]] = (co2 * 1000000) / area[ind]
                        else:
                            sort_em_1[land[ind]] = 0.0
                    sorted_cap = []
                    sorted_cap = sorted(sort_em_1.items(),
                                        key=lambda x: x[1], reverse=True)
                    for lanCap in sorted_cap:
                        print(lanCap[0], ': ', lanCap[1])
                elif landNum > 0:
                    for x in eData.emission_2005.items():
                        ind = x[0]
                        co2 = x[1]
                        if area[ind]:
                            sort_em_1[land[ind]] = (co2 * 1000000) / area[ind]
                        else:
                            sort_em_1[land[ind]] = 0.0
                    sorted_cap = []
                    sorted_cap = sorted(sort_em_1.items(),
                                        key=lambda x: x[1], reverse=True)
                    while i < landNum:
                        print(sorted_cap[i][0], ': ', sorted_cap[i][1])
                        i += 1

            if target == 'emission_2017':
                if landNum == 0:
                    for x in eData.emission_2017.items():
                        ind = x[0]
                        co2 = x[1]
                        if area[ind]:
                            sort_em_1[land[ind]] = (co2 * 1000000) / area[ind]
                        else:
                            sort_em_1[land[ind]] = 0.0
                    sorted_cap = []
                    sorted_cap = sorted(sort_em_1.items(),
                                        key=lambda x: x[1], reverse=True)
                    for lanCap in sorted_cap:
                        print(lanCap[0], ': ', lanCap[1])
                elif landNum > 0:
                    for x in eData.emission_2017.items():
                        ind = x[0]
                        co2 = x[1]
                        if area[ind]:
                            sort_em_1[land[ind]] = (co2 * 1000000) / area[ind]
                        else:
                            sort_em_1[land[ind]] = 0.0
                    sorted_cap = []
                    sorted_cap = sorted(sort_em_1.items(),
                                        key=lambda x: x[1], reverse=True)
                    while i < landNum:
                        print(sorted_cap[i][0], ': ', sorted_cap[i][1])
                        i += 1


def printEmission(year, landNum, cap):
    target = 'emission_'+year
    i = 0
    sort_em_1 = {}
    sorted_cap = []

    if target == 'emission_1990':
        sort_em = sorted(eData.emission_1990.items(),
                         key=lambda x: x[1], reverse=True)
        if landNum == 0 and cap == 0:
            for x in sort_em:
                print(land[x[0]], ':', x[1])
        elif landNum > 0 and cap == 0:
            while i < landNum:
                print(land[sort_em[i][0]], ':', sort_em[i][1])
                i += 1
        elif landNum == 0 and cap > 0:
            for x in eData.emission_1990.items():
                ind = x[0]
                co2 = x[1]
                if len(capita[ind]) > 0:
                    sort_em_1[land[ind]] = (
                        co2 * 1000000) / capita[ind][cap - 1]
                else:
                    sort_em_1[land[ind]] = 0.0
            sorted_cap = []
            sorted_cap = sorted(sort_em_1.items(),
                                key=lambda x: x[1], reverse=True)
            for lanCap in sorted_cap:
                print(lanCap[0], ': ', lanCap[1])
        elif landNum > 0 and cap > 0:
            for x in eData.emission_1990.items():
                ind = x[0]
                co2 = x[1]
                if len(capita[ind]) > 0:
                    sort_em_1[land[ind]] = (
                        co2 * 1000000) / capita[ind][cap - 1]
                else:
                    sort_em_1[land[ind]] = 0.0
            sorted_cap = []
            sorted_cap = sorted(sort_em_1.items(),
                                key=lambda x: x[1], reverse=True)
            while i < landNum:
                print(sorted_cap[i][0], ': ', sorted_cap[i][1])
                i += 1
    if target == 'emission_2005':
        sort_em = sorted(eData.emission_2005.items(),
                         key=lambda x: x[1], reverse=True)
        if landNum == 0 and cap == 0:
            for x in sort_em:
                print(land[x[0]], ':', x[1])
        elif landNum > 0 and cap == 0:
            while i < landNum:
                print(land[sort_em[i][0]], ':', sort_em[i][1])
                i += 1
        elif landNum == 0 and cap > 0:
            for x in eData.emission_2005.items():
                ind = x[0]
                co2 = x[1]
                if len(capita[ind]) > 0:
                    sort_em_1[land[ind]] = (
                        co2 * 1000000) / capita[ind][cap - 1]
                else:
                    sort_em_1[land[ind]] = 0.0
            sorted_cap = []
            sorted_cap = sorted(sort_em_1.items(),
                                key=lambda x: x[1], reverse=True)
            for lanCap in sorted_cap:
                print(lanCap[0], ': ', lanCap[1])
        elif landNum > 0 and cap > 0:
            for x in eData.emission_2005.items():
                ind = x[0]
                co2 = x[1]
                if len(capita[ind]) > 0:
                    sort_em_1[land[ind]] = (
                        co2 * 1000000) / capita[ind][cap - 1]
                else:
                    sort_em_1[land[ind]] = 0.0
            sorted_cap = []
            sorted_cap = sorted(sort_em_1.items(),
                                key=lambda x: x[1], reverse=True)
            while i < landNum:
                print(sorted_cap[i][0], ': ', sorted_cap[i][1])
                i += 1

    if target == 'emission_2017':
        sort_em = sorted(eData.emission_2017.items(),
                         key=lambda x: x[1], reverse=True)
        if landNum == 0 and cap == 0:
            for x in sort_em:
                print(land[x[0]], ':', x[1])
        elif landNum > 0 and cap == 0:
            while i < landNum:
                print(land[sort_em[i][0]], ':', sort_em[i][1])
                i += 1
        elif landNum == 0 and cap > 0:
            for x in eData.emission_2017.items():
                ind = x[0]
                co2 = x[1]
                if len(capita[ind]) > 0:
                    sort_em_1[land[ind]] = (
                        co2 * 1000000) / capita[ind][cap - 1]
                else:
                    sort_em_1[land[ind]] = 0.0
            sorted_cap = []
            sorted_cap = sorted(sort_em_1.items(),
                                key=lambda x: x[1], reverse=True)
            for lanCap in sorted_cap:
                print(lanCap[0], ': ', lanCap[1])
        elif landNum > 0 and cap > 0:
            for x in eData.emission_2017.items():
                ind = x[0]
                co2 = x[1]
                if len(capita[ind]) > 0:
                    sort_em_1[land[ind]] = (
                        co2 * 1000000) / capita[ind][cap - 1]
                else:
                    sort_em_1[land[ind]] = 0.0
            sorted_cap = []
            sorted_cap = sorted(sort_em_1.items(),
                                key=lambda x: x[1], reverse=True)
            while i < landNum:
                print(sorted_cap[i][0], ': ', sorted_cap[i][1])
                i += 1
