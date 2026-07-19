
# 1. What is while loop?
    # --> While loop is a loop which can be executed a set of instructions as long as a condition is True


# 2. Explain it's syntax with an example.
# This is a targeted variable
i = 1
# Giving the condition
while i < 10:
    # Indentation the Printing variable
    print(i)
    # Modifier that prevents the infinite loops
    i+=1

# 3. What is the difference between a for loop and a while loop?
    # --> for loops are used when we know how many times we need to execute the condition / block of code. 
    # --> while loops are used when we don't know how many times we need to execute the condition / block of code untill the condition becomes False.

# 4. Give three real-life examples where a while loop can be used.

license = "yes"
rider =""

while rider != license:
    rider = input("Do you have license???")
    if rider != license:
        print("Rs.1000 fine")
print("Drive safely")
