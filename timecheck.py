# 5. Write a program to take time as input from user. Print "Morning" if the time is between 7 to 12.
# Print "Afternoon" if the time is between 12 to 3. Print "Evening" if the time is between 3 to 6. Else print "night"
userTime = int(input("Enter time (in 24-hour format): "))

if 7 <= userTime < 12:
    print("Morning")
elif 12 <= userTime < 15:
    print("Afternoon")
elif 15 <= userTime < 18:
    print("Evening")
else:
    print("Night")

