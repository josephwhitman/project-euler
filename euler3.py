# Project Euler Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
k = 600851475143
# create a function that determines if a number is prime
def isprime(x):
	"Check if integer x is prime, return True or False"
	if x == 2:
		return True
	elif x < 2 or not x & 1:
		return False
	for i in range(3, int(x**0.5)+1, 2):
		if x%i == 0:
			return False
	return True
# identify the largest prime factor
for x in range(3, int(k**0.5)+1, 2):
	if k%x == 0 and isprime(x) == True:
		lprime = x
	else:
		pass
print('The largest prime factor of k is', lprime)
