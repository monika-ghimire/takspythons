# 4. Write a Python function that takes two lists and returns True if they have at least one common member.


non_veg = ['meet' , 'egg' , 'fish' , 'panner']
veg =['panner' , 'tofu', ]

found_match =[]

for i in non_veg:
    for j in veg:
        if i == j:
            found_match.append(i)
            found_match.append(j)

print('same food is:' ,found_match)