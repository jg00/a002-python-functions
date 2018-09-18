total_amount = float(input("Enter total amount: "))
tip_percentage_amount = float(input("Enter tip percentage amount: "))

def calculate_tip_amount(total_amount, tip_percentage_amount):
    print((tip_percentage_amount/100) * total_amount)

calculate_tip_amount(total_amount, tip_percentage_amount)