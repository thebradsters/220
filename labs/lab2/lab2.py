import math


def calculating_mean():
    print("Methods to calculate mean!")
    var = eval(input("enter the values to be entered: "))
    rms_sum = 0
    har_sum = 0
    geo_sum = 1
    for i in range(1, var + 1):
        values = eval(input("enter value"))
        rms_exp = math.pow(values, 2)
        rms_sum = rms_sum + rms_exp

        har_mean = 1 / values
        har_sum = har_sum + har_mean

        geo_sum = geo_sum * values

    numbers = rms_sum / var
    rms = math.sqrt(numbers)
    round_rms = round(rms, 3)

    har_total = var / har_sum

    geo_total = math.pow(geo_sum, 1 / var)
    geo_round = round(geo_total, 3)

    print(round_rms)
    print(har_total)
    print(geo_round)
