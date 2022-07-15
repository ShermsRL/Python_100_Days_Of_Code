# Data Types

# Pulling out a character from a string is called subscript, number in sq bracket start from 0
# (simply put, dissecting a string)
print("Hello"[4])

# Integer (no decimals)
print(123 + 345)
# can add underscore to make it easier to see, computer will ignore
print(123_456_789)

# Float (decimal numbers)
print(3.14159)

# Boolean (only got 2 value)
True
False

# Day 2 exercise ------------------------------------------------------------------------------------------
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print ("Welcome to the tip calculator.")
# Stored as String
total_bill = input("What was the total bill? $")
float_total_bill = float(total_bill)

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
int_tip = int(tip)
percent_tip = 1 + (int_tip / 100)

pax = input("How many people to split the bill? ")
int_pax = int(pax)

to_pay = "%.2f" % round(float_total_bill * percent_tip / int_pax , 2)

print(f"Each person should pay {to_pay}")
