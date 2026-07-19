# Display the message: "Welcome to DPLMS Student Registration System."

print("\n***** Displaying a message *****\n")

print("Welcome to DPLMS Student Registration System.")

# 2. Create a list containing these courses: Python with AI/ML, JavaScript, Flutter, and MERN Stack.

print("\n***** Creating a list *****\n")

courses_list = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]
print(courses_list)
print(f"\nThe given course_list is {type(courses_list)} dataType.\n")

print("\n***** Creating a list using set *****\n")

courses_set = {"Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"}
print(courses_set)
print(f"The given course_list is {type(courses_set)} dataType.\n")

# 3. Use a for loop to display all available courses.
print("\n***** For loop in list *****\n")

for course in courses_list:
    print(course)

print("\n***** For loop in set *****\n")
for course in courses_set:
    print(course)

# 4. Ask the user to enter Student Name, Email. Age, and Selected Course.

print("\n***** Ask the user to enter Student Name, Email. Age, and Selected Course. *****\n")
print(input("Enter your name: "))
print(input("Enter your Email: "))
print(int(input("Enter your age: ")))
print(input("Enter your Selected Course: "))


# 5. Store the entered information inside a Python Dictionary.

# Firstly Creating an empty dictionary 
person_info ={}

person_info["name"] = input("Enter your name: ")
person_info["email"] = input("Enter your email: ")
person_info["age"] = int(input("Enter your age: "))
person_info["course"] = input("Enter your course: ")

print(person_info)

# 6. Use an if...else statement to check whether the selected course exists in the course list

# Checking the value in the dictionary
if "AIUDAAN" in person_info.values():
    print("Registration successful")
else:
    print("Course Not Available")

# 7. If the course exists, display 'Registration Successful; Otherwise display "Course Not Available"
# 8. Print the student's. registration details in a clean, formatted output