#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

total = input("Welcome to the tip calculator! \nWhat was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
pay = (float(total) / int(people)) * (1 + (int(tip) / 100))
# print(pay)
# round(pay,2) #Round the result to 2 decimal places
# print(pay)
# print(f"Each person should pay ${pay}")
print("Each person should pay: ${:.2f}".format(pay))