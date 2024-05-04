# 1 year = 52 weeks
# 1 year = 12 months
# 1 year = 365 days

current_age = input("What is your current age? ")
have_age = 90 - int(current_age)
days = have_age* 365
weeks = have_age * 52
months = have_age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left until you turn 90.")
