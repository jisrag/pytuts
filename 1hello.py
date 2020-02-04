#Variables
print("Hola mundo Cruel!!") 
color = "Red"
thing = "Hell"
print(color + " is the color of the " + thing)
print(((((1+2)*3)/4))**5)

#Explicit convertion
bill = 47.28
tip = bill * .15
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))

#Functions
def print_seconds(hours, minutes, seconds):
    print((hours*3600)+(minutes*60)+seconds)

print_seconds(1,2,3)

#Return values / We can return more than a value
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a+amount_b
print(result)

#Reusing Code with functions
def print_monthly_expense(month, hours):
  _mon_cost=hours*0.65
  print("In " + month + " we spent " + str(_mon_cost))
  
june_hours = 243
print_monthly_expense("June", june_hours)

july_hours = 325
print_monthly_expense("July", july_hours)

august_hours = 298
print_monthly_expense("August", august_hours)

#With functions yet
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)