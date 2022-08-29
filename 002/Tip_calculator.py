bill = float(input('Bill: $'))
people = int(input('How many people? '))
tip = int(input('Tax (10, 12 or 15): '))

add_tip = bill * tip / 100
final_bill = (bill + add_tip) / people

print(f'Each person will pay ${final_bill:.2f}')
