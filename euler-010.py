#The sum of the primes below 10 is 2+3+5+7=17
#Find the sum of all the primes below two million

pmax = 2000000

#checks if integer is prime
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

#store all the primes below pmax as a list
primelist = filter(isprime, range(1,pmax))

#sum all the primes in the list
psum = 0
for i in primelist:
	psum += int(i)

print('The sum of all the primes below two million is', psum)

#Answer: 142913828922
