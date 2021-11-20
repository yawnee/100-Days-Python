# Don't change the code below
print("Welcome to Python Pizza Delivereis!")
size = input("What size pizza do you want? S, M, OR L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#Don't change the code above

#Example input
# size = L
# add_pepperoni = Y
# extra_cheese = N
#Example Output
#Your final bill is 28

#Write your code below this line

price = 0
s_pizza = 15
m_pizza = 20
l_pizza = 25

small_pepperoni = 2
medium_or_large_pepperoni = 3
extra_cheese = 1

if size == "S":
    price += s_pizza
    if add_pepperoni == "Y" and size == "S":
        price += small_pepperoni
    if extra_cheese == "Y":
        price += extra_cheese
elif size == "M":
    price += m_pizza
    if add_pepperoni == "Y" and size == "M":
        price += medium_or_large_pepperoni
    if extra_cheese == "Y":
        price += extra_cheese
elif size == "L":
    price += l_pizza
    if add_pepperoni == "Y" and size == "L":
        price += medium_or_large_pepperoni
    if extra_cheese == "Y":
        price += extra_cheese
else:
    print("Wrong input son")
print(f"Your final price is ${price}. Thank you!")





