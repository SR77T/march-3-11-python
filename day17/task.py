# Take two numbers as input and add those numbers. Handle the possible exceptions.


# try:
#     num1 = int(input("enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 + num2
# except:
#     print("The input number is invalid")
# else:
#     print(f"The sum of two numbers is {result}")


# Take two numbers input and divide a number by another number. Handle the possible exceptions.
    
# try:
#     a = int(input("Enter a first number: "))
#     b = int(input("Enter a second number: "))
#     result = a / b
# except ValueError:
#     print("Invalid Input! Please enter a valid integer.")
# except ZeroDivisionError:
#     print("B can't be zero")
# else: 
#     print(f"The division  result is  {result}")


# Create a dictionary student with keys id, name, age, department. Take a input from the user, which 
# info (id, name, age or department) he wants to access and print the result. Handle the possible exceptions.

student = {"id": 1, "name": "Ram", "age": 30, "department": "CS"}
key = input("Enter the info you want to access ")
try:
    result = student[key]
except KeyError:
    print(f"The {key} is not present in the student")
else:
    print(f"The {key} of the student is {result}")


if key in student:
    print(f"The {key} of the student is {student[key]}")
else:
    print(f"The {key} is not present in the student")
    

result = student.get(key, "N/A")
print(f"The {key} of the student is {student[key]}")



# student = {"id" : 1,
#            "name" : "Jane",
#            "age" : 25,
#            "department" : "finance"
#            }
# try:
#     get_info = input("Which information do you want to access? Enter 'id', 'name', 'age' or 'department': ")
#     result =  student[get_info]
# except KeyError:
#     print(f"key error {get_info} is raised.")
# else: 
#     print(f"The {get_info} of the student is {result} ")