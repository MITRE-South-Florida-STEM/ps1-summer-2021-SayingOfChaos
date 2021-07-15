total_cost = float(input("Enter the cost of your dream home: "))

annual_salary = float(input("Enter your annual salary: "))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary/12

num_months = 0

while(current_savings < portion_down_payment):
  current_savings += current_savings*(r/12) + monthly_salary*portion_saved
  num_months += 1;
  if(num_months % 6 == 0):
    annual_salary *= (1 + semi_annual_raise)
    monthly_salary = annual_salary/12

print("Number of months: " + str(num_months))

#I know this is incredebly messy, but it works. I am sorry I didn't take the time to clean it up. Have a great day :)