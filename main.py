
def fib(n,memo):
	if(n<=0):
		return 0
	elif(n==1):
		return 1
	elif(n in memo):
		return memo[n]

	memo[n] = fib(n-1,memo)+fib(n-2,memo)
	return memo[n]

memo = {}
for i in range(0,11):
	print(fib(i,memo))
