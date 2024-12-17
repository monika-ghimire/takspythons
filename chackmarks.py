# 2. Write a program to return the grade of a person according to the marks they received.  
# Example:
# input: Enter your marks: 90
# Output : Distinction


marks = int(input('enter your marks to check'))

if marks==30:
    print('you are just pass')
elif marks>30 and marks<=50:
    print('good marks pass with great number')
elif marks>50  and marks<=80:
    print('excellent you got A ')
elif marks>80:
    print('hurry your hard working seeing in result you got A+ ')
else:
    print('you got fail , plz work hard ')



