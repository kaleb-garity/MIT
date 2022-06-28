annual_salary = print("Enter your annual salary: ")
annual_salary = float(annual_salary)
portion_saved = print("Enter the portion of salary to be saved: ")
portion_saved = float(portion_saved)
total_cost = print("Enter the cost of your dream home: ")
total_cost = float(total_cost)

portion_down_payment = 0.25
current_savings = 0
r = 0.04

while current_savings < total_cost:
    