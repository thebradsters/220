"""
Bradley Jones
Lab 3
"""

def traffic():
    roads_surveyed = eval(input("How many roads were surveyed? "))
    total_traveled = 0
    for i in range(1, roads_surveyed + 1):
        print("How many days was road", i, "surveyed?", end=" ")
        days = eval(input())
        road_acc = 0
        for j in range(1, days + 1):
            print("How many cars traveled on day ", j, "?", sep="", end=" ")
            cars_traveled = eval(input())
            road_acc = road_acc + cars_traveled
        average = road_acc / days
        total_traveled = total_traveled + road_acc
        print("Road", i, "average vehicles per day:", average)
    total = total_traveled / roads_surveyed
    total_round = round(total, 2)
    print("Total number of vehicles traveled on all roads:", total_traveled)
    print("Average number of vehicles per road:", total_round)

traffic()