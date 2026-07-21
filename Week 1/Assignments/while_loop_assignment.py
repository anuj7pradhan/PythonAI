
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



import random
num = random.randint(1,100)
guess_num = 0

while guess_num != num:
    guess_num = int(input("Guess a number between 1 and 100: "))
    if guess_num < num:
        print("Too low!")
    elif guess_num > num:
        print("Too high!")
    else:
        print("Correct!")


dp_payment = "5000"
while True:
    pending_amount = input("Pay just 5000 for AI Udaan course: ")
    if pending_amount == dp_payment:
        print("You are enrolled in AI Udaan successfully.")
        break
    else:
        print("Pay the fee to enroll the course AI Udaan")