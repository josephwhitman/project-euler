# Project Euler Problem 2
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Import Python Math library to use factorial function
import math
# k is the largest divisor, n is k factorial (the largest number divisible by all natural numbers 1 thru k)
k = 20
n = math.factorial(k)
# loops over all x candidate numbers, looking for the smallest one that is divisible by all i
# (breaks after printing; might not be super efficient)
for x in xrange(1, n):
	if all(x%i == 0 for i in range(1,k+1))==True:
		print(x)
		break
	else:
		pass


