#For Example 1
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
#        print(square(n))
    return sum

print(sum_squares(10)) # Should be 285

#For Example 2  Factorial
def factorial(n):
    result = 1
    for i in range(1, n):
        result+=result*i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

#For Example 3 Nested For Loops
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team )

#For Example 4 - Validating the list in a for cicle

def is_valid(user):
    if len(user)>3:
        return True
    return False


def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat", "pap"])

#For Example 5
def factorialnew(n):
    result = 1
    for x in range(1,n):
        result += result*x
    return result

for n in range(10):
    print(n, factorialnew(n))


#For Example 6
def cube(num):
  result = num**3
  return result
  

for n in range(1,11):
  print(n, cube(n))

#For Example 7
for n in range(100):
  if n%7==0:
    print(n)