# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for modular_increase in range(2, n + 1):
        if number % modular_increase == 0:
            #Not a prime number
            is_prime = True
        else:
            #Number is a prime number
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



