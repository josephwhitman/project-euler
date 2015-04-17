# Project Euler Problem 9
# A Pythagorean triplet is a set of 3 natural numbers a< b < c for which a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc
from fractions import gcd
for m in range(1,int(500**0.5)):
	for n in range(1,int(500**0.5)):
		if m > n and m%2 != n%2 and gcd(m,n)==1:
			a = m^2 - n^2
			b = 2*m*n
			c = m^2 + n^2
			if a + b + c = 1000:
				trip = a*b*c
				break
print(trip)