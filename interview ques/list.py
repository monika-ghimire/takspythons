# 2. Write a Python function that takes two lists of integers as input
# and returns a new list containing only the numbers that are present in both lists, 
# but with each number appearing only once in the final list.


def find_common(l1, l2):
    new_list = list(set(l1) & set(l2))
    return new_list

l1 =[2, 4, 1]
l2 =[0, 2, 5]

res = find_common(l1,l2)

print('here is resutle' , res)

