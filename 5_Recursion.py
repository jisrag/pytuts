#Recursion General Example

# def recursive_function(parameters):
#    if base_case_condition(parameters):
#        return base_case_value
#    recursive_function(modified_parameters)


#Example 1 Sum of previus numbers
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(900)) # Should be 15

#Example 2 Factorial

def factorial(n):
    print("Factorial called with " + str(n))
    if n<2:
        print("Returning 1")
        return 1
    result=n*factorial(n-1)
    print("Returning " + str(result) + " for  factorial of " + str(n))
    return result

factorial(4)

