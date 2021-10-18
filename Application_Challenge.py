"""
Compute the sum of all numbers between 1 and 1000 which are divisible by 3 and 5
"""

my_sum = 0
"""
# using a little number theory, all numbers divisible by 3 and 5 must also be divisible by 15
# the lowest common factor 
for i in range(1, 1001):
    if i % 15 == 0:
        my_sum = my_sum + i

print(my_sum)

"""
# or can be accomplished with nested loops

for i in range(1, 1001):
    if i % 3 == 0:
        if i % 5 == 0:
            my_sum = my_sum + i

print(my_sum)

# solution: 33165