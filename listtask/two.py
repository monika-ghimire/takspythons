# 2. Write a Python program to remove duplicate items from a list.

fruits = ['apple' , 'pie' , 'apple' , 'berry']

# fruits = list(set(fruits)) this will mess with order
# to maintain order we gona use loop 

uniqF =[]
for i in fruits:
    if i not in uniqF:
        uniqF.append(i)


print("List without duplicates:", uniqF)