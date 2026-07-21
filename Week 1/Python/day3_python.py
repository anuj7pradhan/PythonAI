name1 = "Balkrishna"
name2 = "sumnima"
name3 = "sulen"
# It will be hectic if we store lisk this way so we introduce some python collections Datatypes /  Non-primitive datatype
"""
collections Datatypes /  Non-primitive datatype

1. List
2. Sets
3. Tuples
4. Dictionary
"""

print("****** List ******")
# If we have same kind of datatype then we can collect in the list of items
# List
country_list = ["Nepal","Japan","Australia","Germany","Denmark"] # List datatype
print(type(country_list))
print("This is country_list",country_list)
print(country_list[0],"is in 1st index")
print(country_list[-3])
country_list.append("India") # Add India to the list
print(country_list)
print(country_list.pop()) # Removes last item of the list
print(country_list)
country_list.insert(0,"Swizerland") # Adds to list 0 index
print(country_list)
country_list.remove("Australia")
print(country_list)
country_list[1] = "Singapore"
print(country_list)
print(len(country_list))

print("****** Tuples ******")

# Tupels - it is static / fixed
country_tuple = ("Norway","Nepal","Norway","Japan","Australia") # Tuple datatype
print(type(country_tuple))
print("This is country_tuple",country_tuple)
print(country_tuple[0])
# country_tuple[3] = "China" # 'tuple' object does not support item assignment
print(country_tuple)
print("There are ",country_tuple.count("Norway"),"Norway in the given tuple.")

print("****** Set ******")
 
country_set = {"Nepal","Japan","Australia","Nepal"} # Sets datatype
print(type(country_set))
print("This is country_set",country_set)
# print(country_set{0},"is in 1st index")
print(country_set)

print("****** Dictionary ******")
"""
Dictionary is very important
--> All the data are connected in this format
    --> Client side application--> made in "javascript, React, Dart etc.."
    --> Server side            --> made in "python, java, php etc..."
        --> both understands json format, or XML 
            --> and these formats are in dictionary form
"""

person_information = {
    "name" : "Anuj",
    "age" : 26,
    "Course" : "AI",
    "College": "IIMS",
    "IsNepali": True
}

print(person_information)
print(person_information["name"])
person_information["Color"] = "Blue"
print(person_information)
person_information["Color"] = "Black"
print(person_information)
person_information.pop("College")
print(person_information)

