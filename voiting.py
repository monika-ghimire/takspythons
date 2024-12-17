# 3. Write a program to take age as input from user and check whether the user is illegible for voting or not.
print('to check illegible for voting or not')
age=int(input('please put your age '))
minage = 18
if age>=18:
    print('yes at ',age, 'age you can vote')
else:
    print('no at this',age, 'you are to young')
    print('wait next',minage - age,'year')

