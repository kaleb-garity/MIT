annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
total_months = 0

while current_savings < down_payment:
    total_months += 1
    current_savings += (annual_salary / 12 * portion_saved) + (current_savings * r / 12)

print("Number of months:", total_months)