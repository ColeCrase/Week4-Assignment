"""
Program: Project5
Author: Cole Crase
This program is to let the user enter the initial number of organisms, the rate
of the growth(greater than 0), number of hours it takes to achieve the rate of
growth, and the number of hours during which the population grows. The output
would display a prediction of the total population.
"""
organisms = int(input("Enter the initial number of organisms: "))
rate = int(input("Enter the rate of growth(greater than 0): "))
hour_rate = int(input("Enter the number of hours it takes to achieve the rate of growth: "))
hour_population = int(input("Enter the number of hours during which the population grows: "))

tp = organisms
hours = 1
while (hours < hour_population):
    tp *=rate
    hours += hour_rate

print("The total population is:" +str(int(tp)))
