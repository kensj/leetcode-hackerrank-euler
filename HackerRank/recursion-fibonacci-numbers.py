def fibonacci(n):
    return n if n==0 or n==1 else fibonacci(n-1) + fibonacci(n-2)
	