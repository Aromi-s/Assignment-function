def recur_factorial(n):
	if n==1:
		return n
	else:
		return n*recur_factorial(n-1)
num=7
if num<0:
	print("factorial doesn't exit for negative numbers")
elif num==0:
	print("the factorial of zero is one")
else:
	print("the factorial of",num,"is",recur_factorial(num))				