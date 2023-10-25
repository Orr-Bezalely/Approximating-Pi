from turtle import *
import random, time, math
r = 600
counter = 0
pi = math.pi
is_valid = False 
while is_valid == False:
    number_of_trials = input("How many trials would you like there to be (between 100 and 100,000)? ") 
    if not number_of_trials.isdigit() or int(number_of_trials) < 100 or int(number_of_trials) > 100000: 
        print("Please enter an INTEGER between 100 and 100,000: ")
    else:
        is_valid = True
        number_of_trials = int(number_of_trials)
def setup_grid():
    delay(0)
    speed(0) 
    penup()
    left(90)
    forward(r / 2)
    left(90)
    backward(r / 2)
    right(90) 
    pendown() 
    for x in range(0,4):
        left(90)
        forward(r)
    backward(r)
    circle(r, 90)
    
def testing(counter, number_of_trials): 
    for x in range(0,number_of_trials):
        coordinate_x = random.randint(-r / 2 + 1, r / 2 - 1)
        coordinate_y = random.randint(-r / 2 + 1, r / 2 - 1)
        penup()
        goto(coordinate_x, coordinate_y)
        dot(2.35, "blue")
        a_squared = ((coordinate_x) - (-r / 2)) ** 2
        b_squared = ((coordinate_y) - (-r / 2)) ** 2
        c_squared = a_squared + b_squared
        distance = c_squared ** 0.5
        if distance < r:
            counter = counter + 1
    return counter

tracer(0, 0)
setup_grid()
counter = testing(counter, number_of_trials)
pi_test = counter / number_of_trials * 4
update()
print(pi_test)
if pi > pi_test:
    a = pi
    b = pi_test
elif pi < pi_test:
    a = pi_test
    b = pi
if pi == pi_test:
    print("You have exactly hit pi!")
else:
    print("The experimental calculation was", a - b, "away from the theoretical pi")
#7.346410206832132e-06 closest - 130,000 trials

