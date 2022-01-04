#Your program should print each number from 1 to 100 in turn
#when the number is visibible by 3 then instead of printing the number it says Fizz
#when divisible by 5, print Buzz
# and when both 3 and 5 say Fizzbuzz

#I could have easily done as  if number % 3 == 0
#I could also have the and on the top and don't need to include the top.
for number in range(1, 101):
    three_divisible = number % 3
    five_divisible = number % 5
    if three_divisible == 0 and not five_divisible == 0:
        print("Fizz")
    elif five_divisible == 0 and not three_divisible == 0:
        print('Buzz')
    elif three_divisible == 0 and five_divisible == 0:
        print('FizzBuzz')
    else:
        print(number)

#I could have easily done as  if number % 3 == 0

