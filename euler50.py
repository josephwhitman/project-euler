# Project Euler Problem 7
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# Seen this before. Trotting out the old isprime
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
# filter numbers list into list of primes
n = 1000
k = 1000
primelist= filter(isprime, xrange(1, n))
# now primelist contains all primes below n
# now we need to create a sum of primes, check if prime, and reduce by the lowest prime then check again
sumprimes = sum(primelist)
sumprimesrev = sum(primelist)
for i in range(0, len(primelist)):
	if sumprimes < k and isprime(sumprimes)==True:
		print(sumprimes)
		pass
	else:
		sumprimes = sumprimes - primelist[i]
		pass
# now in reverse, taking off the highest prime each time
for i in range(len(primelist)-1, -1, -1):
	if sumprimesrev < k and isprime(sumprimesrev)==True:
		print(sumprimesrev)
		pass
	else:
		sumprimesrev = sumprimesrev - primelist[i]
		pass


# compare with the two methods
# problem: 97 and 41 both fit, but 41 is made by summing MORE CONSECUTIVE PRIMES
# next step: find a better method that chooses the right number
