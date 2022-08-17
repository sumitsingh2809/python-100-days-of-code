print('Welcome to the tip calculator')

total_bill = float(input('what was the total bill? $'))
percentage = int(
    input('what percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

total = (total_bill + (total_bill * percentage / 100)) / people
print(f'Each person should pay: ${round(total, 2)}')
