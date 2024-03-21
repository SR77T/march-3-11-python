a = [(5,4,1), (3,2,0), (1,7), (2,9),(0,10)]

def  sort_tuple(t):
    return  t[-1]
    
    
# b = sorted(a , key=sort_tuple)
# print(b)

a.sort(key=sort_tuple)
print(a)



# [(3, 2, 0), (5, 4, 1), (1, 7), (2, 9), (0, 10)]
# """
# Given a list a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)], sort the list based on the last item of each tuple inside the list.
# Output : [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]

# """

a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]


def sort_by_last_element(item):  # item => (5, 4)
    return item[-1]
    # return item[len(item)-1]  # item[3-1] = item[2], item[2-1] item[1]


a.sort(key=sort_by_last_element)
print(a)  # [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]



# If a function takes another function as an argument then such a function is called higher order function

a = [(5, 4), (3, 2), (1, 7), (2, 9), (0, 10)]
# [(0, 10), (1, 7), (2, 9), (3, 2), (5, 4)]


def sort_by_first_element(item):  # item => (5, 4)
    return item[0]


a.sort(key=sort_by_first_element)
print(a)  # [(0, 10), (1, 7), (2, 9), (3, 2), (5, 4)]

# here sort() is a higher order function


a = [3, 4, 1, 2]
a.sort()  # ascending
print(a)  #

a.sort(reverse=True)  # descending


result = sorted(a)  # builtin function
print(result)