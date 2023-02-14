# Write a program to calculate the area of a triangle given the lengths of its
# sides using Heron’s Formula.  Here is an overview of what you need to do:
#
# 1) Prompt the user to give each of the three side lengths, a, b, and c.
# 2) Check to ensure that the side lengths are all positive.  If not, print an
# error message and stop the program.
# 3) Check to ensure that the sides represent a valid triangle.  In particular,
# the sum of the lengths of any two sides must be larger than the length of the
# third side.  Your program will have to check that all three sides meet this
# criteria.  If not, print an error message and stop the program.
# 4) Calculate the semiperimeter, s.  See assignment for details.
# 5) Finally, calculate the area.  See assignment for details.
#
# You must display the area to two decimal places.  Your input and output
# messages must conform to the following examples:
#
# Enter side A’s length: 3
# Enter side B’s length: 4
# Enter side C’s length: 5
# Area = 6.00
#
# Enter side A’s length: 1.2
# Enter side B’s length: 100
# Enter side C’s length: 1
# Side B is too long!
#
# Enter side A’s length: 0
# Enter side B’s length: 4
# Enter side C’s length: 5
# Must have positive side lengths!
#
# Note the order of inputs, capitalization of messages, spacing, etc.

import sys
import math

a = float(input("Enter side A's length: "))
b = float(input("Enter side B's length: "))
c = float(input("Enter side C's length: "))

if a <= 0 or b<= 0 or c <= 0:
    print("Must have positive side lengths!")
    sys.exit()

if a+b < c:
    print("Side C is too long!")
    sys.exit()
elif b+c < a:
    print("Side A is too long!")
    sys.exit()
elif a+c < b:
    print("Side B is too long!")
    sys.exit()
    

s = (a+b+c) / 2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"Area = {area:.2f}")




