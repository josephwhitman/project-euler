# Project Euler Problem 6
n = 100
# First let's find the square of the sum of n natural numbers
squaresum = sum(range(1,n+1))**2
# Now to find the sum of squares
sumsquares = 0
for i in range(1,n+1):
	sumsquares = sumsquares+i**2
# find and print the difference
diff = squaresum - sumsquares
print(diff)