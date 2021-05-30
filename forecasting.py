import json
from math import log, sqrt, pow, fabs, e


with open('corona_situation.json') as f:
    json_file = json.load(f)


def current_day_array_data(file):
    current_day_data = file['28 мая']
    return current_day_data


def day_before_array_data(file):
    day_before_data = file['27 мая']
    return day_before_data


def day_before_yesterday_array_data(file):
    day_before_yesterday = file['26 мая']
    return day_before_yesterday


def current_active_cases_array():
    current_day_array = current_day_array_data(json_file)
    current_active_cases = []
    for d in current_day_array:
        active_cases = d['NoI'] - d['NoR']
        current_active_cases.append({d['city']: active_cases})
    return current_active_cases


def day_before_active_cases_array():
    day_before_array = day_before_array_data(json_file)
    day_before_active_cases = []
    for d in day_before_array:
        active_cases = d['NoI'] - d['NoR']
        day_before_active_cases.append({d['city']: active_cases})
    return day_before_active_cases


def day_before_yesterday_active_cases_array():
    day_before_yesterday = day_before_yesterday_array_data(json_file)
    day_before_yesterday_active_cases = []
    for d in day_before_yesterday:
        active_cases = d['NoI'] - d['NoR']
        day_before_yesterday_active_cases.append({d['city']: active_cases})
    return day_before_yesterday_active_cases


def current_growth_rate():
    active_cases_current = current_active_cases_array()
    active_cases_day_before = day_before_active_cases_array()

    growth_rate_arr = []
    counter = 0

    for row1 in active_cases_current:
        for key1, value1 in row1.items():
            for row2 in active_cases_day_before[counter:counter + 1]:
                for key2, value2 in row2.items():
                    g = (value1 - value2) / value2
                    growth_rate_arr.append({key1: g})
            counter += 1

    return growth_rate_arr


def past_growth_rate():
    active_cases_day_before = day_before_active_cases_array()
    active_cases_day_before_yesterday = day_before_yesterday_active_cases_array()

    growth_rate_arr = []
    counter = 0

    for row1 in active_cases_day_before:
        for key1, value1 in row1.items():
            for row2 in active_cases_day_before_yesterday[counter:counter + 1]:
                for key2, value2 in row2.items():
                    g = (value1 - value2) / value2
                    growth_rate_arr.append({key1: g})
            counter += 1

    return growth_rate_arr


def rate_of_change_in_growth_rate():
    a_current = current_active_cases_array()
    a_day_before = day_before_active_cases_array()
    a_day_before_yesterday = day_before_yesterday_active_cases_array()

    count = 0
    c_list = []

    for row1 in a_current:
        for key1, value1 in row1.items():
            for row2 in a_day_before[count:count+1]:
                for key2, value2 in row2.items():
                    for row3 in a_day_before_yesterday[count:count+1]:
                        for key3, value3 in row3.items():
                            div = sqrt(pow(log(fabs(value2)) - log(fabs(value3)), 2))
                            if div == 0:
                                div += 1
                            c = -((log(fabs(value1)) - log(fabs(value2))) - (log(fabs(value2)) - log(fabs(value3)))) / div
                            c_list.append({key1: c})
            count += 1
    return c_list


def calculate_coefficients():
    """
    in order to calculate expected value, I decided to use coefficients between
    days 1,2 and 3 such that
    (day1 / day2) / (day2 / day3) or (day1 * day3) / (day2 * day2)
    It allows me to predict tomorrow's day coefficient of increase/decrease of active cases
    :return: coefficient_list
    """
    a_current = current_active_cases_array()
    a_day_before = day_before_active_cases_array()
    a_day_before_yesterday = day_before_yesterday_active_cases_array()
    coefficient_list = []
    counter = 0

    for row1 in a_current:
        for k1, v1 in row1.items():
            for row2 in a_day_before[counter:counter+1]:
                for k2, v2 in row2.items():
                    for row3 in a_day_before_yesterday[counter:counter+1]:
                        for k3, v3 in row3.items():
                            coefficient_list.append({k1: ((v1 * v3) / (v2 * v2))})
                counter += 1

    return coefficient_list


def expected_value():
    a_current = current_day_array_data(json_file)
    coefficients = calculate_coefficients()
    a_forecasted = []
    counter = 0
    for row1 in a_current:
        for row2 in coefficients[counter:counter+1]:
            for k2, v2 in row2.items():
                predicted_infected = int(int(row1['NoI'])*v2)
                if 1000 > abs(predicted_infected) > 100:
                    predicted_infected //= 10
                elif abs(predicted_infected) > 1000:
                    predicted_infected //= 100
                elif 100 > abs(predicted_infected) > 70:
                    predicted_infected //= 2

                row1['NoI'] += predicted_infected

                predicted_recovered = int(int(row1['NoR']) * v2)
                if 1000 > abs(predicted_recovered) > 100:
                    predicted_recovered //= 10
                elif abs(predicted_recovered) > 1000:
                    predicted_recovered //= 100
                elif 100 > abs(predicted_recovered) > 70:
                    predicted_recovered //= 2

                row1['NoR'] += predicted_recovered

        counter += 1
    return a_current


print('forecasted: ', expected_value(), '\n')
