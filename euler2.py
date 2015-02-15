# Project Euler Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Create a function that returns all the Fibonacci numbers up to n as a list
def fib(n):
	"Return a list containing the Fibonacci series up to n"
	result=[]
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result
# use the above function to generate a list of all Fibonacci numbers under 4 million
k = 4000000
fn=fib(k)
# sum only the even numbers in the list
ftotal = sum(x for x in fn if x%2==0)
print('The sum of all even Fibonacci numbers below', k, 'is', ftotal)