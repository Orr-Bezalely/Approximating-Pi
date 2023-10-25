from turtle import *
import random, time, math

spaced_lines = 30
big_square = 660
number_of_spaced_lines = int(big_square / spaced_lines)
needle = int(spaced_lines / 2)
is_valid = False 
while is_valid == False:
    number_of_trials = input("How many trials would you like there to be (between 100 and 100,000)? ") 
    if not number_of_trials.isdigit() or int(number_of_trials) < 100 or int(number_of_trials) > 100000: 
        print("Please enter an INTEGER between 100 and 100,000: ")
    else:
        is_valid = True
        number_of_trials = int(number_of_trials)
counter = 0
pi = math.pi

def background(spaced_lines, big_square, number_of_spaced_lines):
    delay(0)
    speed(0)
    penup()
    for x in range(0, 2): 
        left(90)
        forward(big_square / 2)
    right(180)
    pendown()
    for x in range(0, 4):
        forward(big_square)
        right(90)
    for x in range(0, number_of_spaced_lines): 
        right(90)
        forward(spaced_lines)
        left(90)
        forward(big_square)
        backward(big_square)
    color("blue")

def random_lines(spaced_lines, needle, number_of_trials, counter):
    for x in range(0, number_of_trials):
        seth(90)
        x_coord = random.uniform(-big_square / 2, big_square / 2)
        y_coord = random.uniform(-big_square / 2, big_square / 2)
        penup()
        goto(x_coord, y_coord)
        pendown()
        coord_1 = position()
        y_coord_1 = ycor()
        angle = random.randint(0, 359)
        right(angle)
        forward(needle)
        coord_2 = position()
        y_coord_2 = ycor()
        if (y_coord_1 % spaced_lines) >= spaced_lines / 2 and spaced_lines / 2 >= (y_coord_2 % spaced_lines) or (y_coord_2 % spaced_lines) >= spaced_lines / 2 and spaced_lines / 2 >= (y_coord_1 % spaced_lines):
            counter = counter + 1
    return counter

tracer(0, 0)
background(spaced_lines, big_square, number_of_spaced_lines)
counter = random_lines(spaced_lines, needle, number_of_trials, counter)
update()
experimental_pi = (number_of_trials / counter) * 2
print(experimental_pi)
if pi > experimental_pi:
    a = pi
    b = experimental_pi
elif pi < experimental_pi:
    a = experimental_pi
    b = pi
if pi == experimental_pi:
    print("You have exactly hit pi!")
else:
    print("The experimental calculation was", a - b, "away from the theoretical pi")

#0.006796415345279083 - 1000
