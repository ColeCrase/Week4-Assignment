"""
Program: Project4
Author: Cole Crase
This program is to let the user enter the initial height from which the ball
is dropped, and the number of times the ball is allowed to continue bouncing.
The output should be the total distance traveled by the ball.
"""
height = int(input("Enter the height from which the ball is dropped: "))
bounce = float(input("Enter the bounce index of the ball: "))
number = float(input("Enter the number of times the ball is allowed to bounce: "))

distance = 0
while number > 0:
    distance=distance + height
    height=height * bounce
    distance=distance + height
    number-=1

print("The total distance traveled is:",distance,"units.")
