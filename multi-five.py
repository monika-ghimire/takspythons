# 6. Write a program to check if an input number is a multiple of 5 or not.

num=int(input('enter number you want check'))

if num % 5 == 0:
    times = num // 5
    print(num, "is a multiple of 5.")
    print("It is divisible by 5", times, "times.")
else:
    print(num, "is not multiple of 5")
    