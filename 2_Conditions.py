#If Condition example one

def number_group(number):
  if number>0:
    return "Positive"
  elif number==0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#If condition example 2

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

#If condition example 3
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize%block_size
    # Depending on whether there's a remainder or not, return the right number.
    if partial_block > 0:
        return (block_size*full_blocks)+block_size
    return block_size*full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192