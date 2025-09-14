monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12
projected_savings =annual_savings + (annual_savings * 0.05)

print("Your monthly savings are #" + str(monthly_savings) + ".")
print("Your projected savings after one year, with interest, is: #" + str(projected_savings) + ".")