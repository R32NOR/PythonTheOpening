# Script for check code possibilities of bike alarm
"""
I bought a bike alarm, where I can set 4-digit code. Each position can be set as A, B or C.
I want to check all possibilities of code set.
"""

digit_posibility = ['A', 'B', 'C']
code_length = 4
number_of_possibilities = pow(len(digit_posibility),code_length)
combinations = []

print('Total number of possibilities:', number_of_possibilities, '\nOptions are:')

for p1 in digit_posibility:
    for p2 in digit_posibility:
        for p3 in digit_posibility:
            for p4 in digit_posibility:
                combination = p1+p2+p3+p4
                combinations.append(combination)

n = 1
for i in combinations:
    print(f'{str(n).rjust(2)}.', i)
    n+=1





