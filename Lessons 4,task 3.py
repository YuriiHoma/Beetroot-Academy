from random import randint

number_1 = randint(5, 6)
number_2 = randint(3, 9)
together = number_1 * number_2
answear = input(f'How much is {number_1} * {number_2}? ')
if not answear:
    False
ans = int(answear)
print('Good job' if ans == together else 'wrong')