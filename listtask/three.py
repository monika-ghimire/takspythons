# 3. Write a Python program to find the list of words that are longer than 5 from a given list of strings:
student_list = ['Nashib', 'Dibash', 'Sushmita','Aayushma','Rajan']

found=[]

for i in student_list:
    if len(i) > 5:
      found.append(i)
print('after check here is list of name who have more the 5 words in name ')
print(found)
