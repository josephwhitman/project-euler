# Project Euler Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# basically, need to find 3x + 5y where 3x and 5y are natural numbers under 1000
# (60)

print('This program answers Project Euler Problem 1: Find the sum of all the multiples of 3 or 5 below 1000')
summ = 0
for x in range(1, 1000):
	if x%3==0 or x%5==0:
		summ = summ + x


print('The sum is',summ)
