my_list1 = [1, 2, 3, 4, 5, 6]

my_list2 = list(range(1, 102, 10))
# range function takes numbers from arg1 to arg2-1
# arg3 changes the increment (optional)
print(my_list1)
print(my_list2)

print(type(my_list1))

# operations on lists
print(my_list1[2])
# returns the 2nd element in the list
print(my_list1[-1])
# using a negative number returns the element from reverse order

# let's create a slice from 2nd element to the 4th element
print(my_list1[1:4])

# length of a list
print(len(my_list1))

# maximum and minimum of a list
print(max(my_list1))
print(min(my_list1))

# add an element to a list
my_list1.append(-4)
print(my_list1)

# reverse a list
my_list1.reverse()
print(my_list1)

# create a list and add them together
my_list2 = [20, 30, 40, 50, 60]

print(my_list1 + my_list2)
print(my_list2 + my_list1)