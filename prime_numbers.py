def solution(n):
	"""A function that generates prime numbers from o to n, given a parameter n"""
	for num in range (0, int(n+1)):
		if isinstance (num, int):
			return True
		elif num < 0:
			raise ValueError ("Should be non_negative")
		elif num == 0 or num == 1:
			raise ValueError ("Not prime number")
		else:
			raise ValueError("Can only take positive integer")
			if num%1==0 and num%num==0:
				result = []
				result.append(num)
				print (result)
				return True
			else:
				return False