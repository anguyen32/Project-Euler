'''

Problem 2 
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def sol1():
	fib = [1,2]
	cur = 0
	i = 0;
	j = 1
	sum = 2
	while cur <= 4000000:
		if cur%2 == 0:
			sum += cur
		cur = fib[i] + fib [j]
		fib.append(cur)
		i+=1
		j+=1
		
	# print(fib)
	return sum

if __name__ == '__main__':
	print(sol1())