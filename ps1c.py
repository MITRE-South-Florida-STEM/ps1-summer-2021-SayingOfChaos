total_cost = 1000000
annual_salary = float(input("Enter your annual salary: "))
base_salary = annual_salary
portion_saved = 0.5
high = 1.0
low = 0.0
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary/12
num_months = 0
cnt = 0

while(current_savings > portion_down_payment + 100 or current_savings < portion_down_payment - 100):
  cnt += 1
  current_savings = 0.0
  annual_salary = base_salary
  monthly_salary = annual_salary/12
  num_months = 0
  for x in range(36):
    current_savings += current_savings*(r/12) + monthly_salary*portion_saved
    num_months += 1;
    if(num_months % 6 == 0):
      annual_salary *= (1 + semi_annual_raise)
      monthly_salary = annual_salary/12
  if(current_savings > portion_down_payment + 100):
    high = portion_saved
  elif(current_savings < portion_down_payment - 100):
    low = portion_saved

  portion_saved = (low + high)/2

  #Debbugin (I don't know how to spell)
  #print("Loop completed, portion to try next: " + str(portion_saved))
  #print("current savings: " + str(current_savings))

  #For the fun
  if(portion_saved > 0.9999999999):
    print("\n You really shouldn't buy this house, let's be honest, you lack the salary to make it in time, in 36 months, you won't make it and if you can't make it in 36 months, then you really really shouldn't go for this house. \n")
    break #exit(0) If you don't want to show the later info

  
print("Best savings rate: " + str(round(portion_saved, 4)))

print("Steps in bisection search: " + str(cnt))

#I know this is incredebly messy, but it works. I am sorry I didn't take the time to clean it up. Have a great day :)

#Also, if you the out the -100s and the +100s then it gives the precise answer :)

#Finally, I should really change every variable to an input but yeah. I also personalize the message about not being able to pay as a joke and I even gave them values even though yeah.