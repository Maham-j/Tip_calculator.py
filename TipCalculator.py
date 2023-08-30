# Get total bill amount from user
total_bill = float(input('Enter total bill? Rs.'))

# Get total number of people from user
people = int(input('Enter total people:'))

# Get tip percentage from user
tip = int(input('how much you want to give? (%)'))

# Calculate amount per person including tip
amount_per_person = round((total_bill / people) * ((tip / 100) + 1))

# Display calculated amount per person
print("amount_per_person: Rs.", amount_per_person)
