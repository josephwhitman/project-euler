# Project Euler Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# modified prime checker function from problem 3
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
# filter numbers list into list of primes then print.
n = 1000000
# n is arbitrary, just needs to be higher than the 10 001st prime number.
primelist= filter(isprime, range(1, n))
print(primelist.pop(10000))
