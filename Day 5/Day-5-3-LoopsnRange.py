#range function
# always add a +1 in a range
# a (bneginning, b (end), c (step)

# total = 0
#
# for number in range(1, 101):
#     print(number)
#     total += number
# print(total)
#

### write a program that calculatesd the sum of all even numbers from 1 to 100
# using only even numbers
# there should be ONLY one print statement for the total and every step
# we need to use range

total = 0
for number in range(0, 101, 2):
    total +=number
print(total)