# Write a program that reads five numbers from the user.  You must calculate and output following statistics:
#
# 1) The sum of all the positive numbers.
# 2) The sum of all the non-positive numbers (≤ 0).
# 3) The sum of all five numbers.
# 4) The average of all the positive numbers.
# 5) The average of all the non-positive numbers (≤ 0).
# 6) The average of all five numbers.
#
# Note that your program must accept the five numbers in any order and cannot
# ask the user to enter the positive and non-positive numbers separately. You
# should start by calculating the sum and average of all five numbers. Be sure
# you get that working correctly and then move on to doing the calculations for
# the positive and non-positive numbers. You will need many variables to keep
# track of all the values, sums, and averages.
#
# Don't forget that to calculate the average of a set of numbers you sum them
# all up then divide by the number of values you added together. For example,
# if your program gets 3 positive numbers and 2 non-positive numbers, then you
# will divide the sum of the positive numbers by 3 to get that average and then
# divide the sum of the non-positive numbers by 2 to get the average of those 2
# numbers. This means you will have to keep track of how many positive numbers
# you read in and how many non-positive numbers you read in, which is separate
# from the numbers themselves.  Also, be sure to consider special cases, e.g.,
# what happens when you have no positive or no non-positive numbers.
#
# Also note that you will need to write a lot of very similar looking pieces of
# code. Think about how to solve the problem for one or two numbers and then go
# from there to calculating the statistics for all five numbers.
#
# All sums and averages must be displayed to two decimal places.
#
# Your input and output messages must conform to the following examples:
#
# Enter the first number: 1
# Enter the second number: 2
# Enter the third number: 3
# Enter the fourth number: -1
# Enter the fifth number: -2
# The sum of the 3 positive numbers: 6.00
# The sum of the 2 non-positive numbers: -3.00
# The sum of the 5 numbers: 3.00
# The average of the 3 positive numbers: 2.00
# The average of the 2 non-positive numbers: -1.50
# The average of the 5 numbers: 0.60
#
# Enter the first number: 10
# Enter the second number: 423.65
# Enter the third number: -312
# Enter the fourth number: 2.6
# Enter the fifth number: 15
# The sum of the 4 positive numbers = 451.25
# The sum of the 1 non-positive numbers = -312.00
# The sum of the 5 numbers = 139.25
# The average of the 4 positive numbers = 112.81
# The average of the 1 non-positive numbers = -312.00
# The average of the 5 numbers = 27.85
#
# Enter the first number: -1
# Enter the second number: -1
# Enter the third number: 0
# Enter the fourth number: 0
# Enter the fifth number: 0
# The sum of the 0 positive numbers = 0.00
# The sum of the 5 non-positive numbers = -2.00
# The sum of the 5 numbers = -2.00
# The average of the 0 positive numbers = 0.00
# The average of the 5 non-positive numbers = -0.40
# The average of the 5 numbers = -0.40
#
# Note the order of outputs, capitalization of messages, spacing, etc.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
d = float(input("Enter the fourth number: "))
e = float(input("Enter the fifth number: "))

pos_tot = 0
neg_tot = 0
num_pos_vars = 0
num_neg_vars = 0

if a>0:
    pos_tot = a
    num_pos_vars += 1
else:
    neg_tot = a
    num_neg_vars += 1
if b>0:
    pos_tot += b
    num_pos_vars += 1
else:
    neg_tot += b
    num_neg_vars += 1
if c>0:
    pos_tot += c
    num_pos_vars += 1
else:
    neg_tot += c
    num_neg_vars += 1
if d>0:
    pos_tot += d
    num_pos_vars += 1
else:
    neg_tot += d
    num_neg_vars += 1
if e>0:
    pos_tot += e
    num_pos_vars += 1
else:
    neg_tot += e
    num_neg_vars += 1

print(f"The sum of the {num_pos_vars} positve numbers: {pos_tot:.2f}")
print(f"The sum of the {num_neg_vars} non-positve numbers: {neg_tot:.2f}")
total_sum = a+b+c+d+e
print(f"the sum of the 5 numbers = {total_sum:.2f}")

if num_pos_vars == 0:
    print("The average of the 0 positve numbers: 0.00")
else:
    print(f"The average of the {num_pos_vars} positve numbers: {pos_tot / num_pos_vars:.2f}")
if num_neg_vars == 0:
    print("The average of the 0 non-positve numbers: 0.00")
else:
    print(f"The average of the {num_neg_vars} non-positve numbers: {neg_tot / num_neg_vars:.2f}")

total_avg = (a+b+c+d+e) / 5
print(f"the average of the 5 numbers = {total_avg:.2f}")







