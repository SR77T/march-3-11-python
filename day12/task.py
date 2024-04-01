students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]

# filter those students whose age is greater than 25 using filter() function
# 1. Normal Solution
# 2. using filter() function

import functools
def sum(x,y):
    if type(x) == dict:
        return x["age"] + y["age"]
    else:
        return x + y["age"]
    
result = functools.reduce(sum, students)
print(result)
    



def upper_case(each):
     each["name"] = each["name"].upper()
     return each
result = map(upper_case, students)
print(list(result))


result = []
for each in students:
    if  each["age"] > 25:
        result.append(each)
print(result)


result = []
def age_greater(each):
    if each["age"] > 25:
        return True
    else:
        return  False
result = filter(age_greater, students)
print(list(result))

