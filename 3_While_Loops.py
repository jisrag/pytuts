# While example 1
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))



#While Example 2
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)


#While Example 3

def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n+=1

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3

#While example 4 - Take care with the zeros

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while (n % 2 == 0) and n!=0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
print (is_power_of_two(0))



#While Example 5

def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  cont=0
  x=1
  while x<n:
    if n%x == 0:
      cont+=x
    x+=1
  return cont

print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16