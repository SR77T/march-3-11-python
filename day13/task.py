# create a decorator function which converts a string input to uppercase


def  to_upper(func):
    def inner_func(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner_func
        

@to_upper
def message(msg):
    return msg

result = message("Hello World")
print(result)  # Output: HELLO WORLD


# create a decorator function "login_required" which asks for a password. If the password matches 
# "1234" then allow permission to access the main function else display the message "Not allowed !"

def login_required(func):
    def inner_func(*args, **kwargs):
        password = input('Enter your password : ')
        if password == '1234':
            return func(*args, **kwargs)
        else:
            return "Not Allowed!"
    return inner_func


@login_required
def addition(a, b):
    return a + b

result = addition(3, 4)
print(result)


# create a decorator function which calculates the execution time of a fucntion
import time
def execution_time(func):
    def inner_func(*args, **kwargs):
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("execution time is", end_time-start_time)
        return result
    return inner_func
        
@execution_time
def my_fxn():
    for i in range (100000000):
        pass
my_fxn()

