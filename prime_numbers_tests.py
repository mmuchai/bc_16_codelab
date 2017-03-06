import unittest
from prime_numbers import solution

class TestSolution (unittest.TestCase):
	def test_list_of_prime_numbers(self):
		self.assertTrue (solution(10), [1, 2, 3, 5, 7])
	def test_cannot_take_negative(self):
		self.assertFalse(solution (-5), ValueError(("Should be non_negative")))
	def test_must_be_integer(self):
		self.assertFalse(solution ("cats"), ValueError("Can only take positive integer"))
	def test_list_prime_numbers_from_zero_to_n_inclusive(self):
		self.assertTrue (solution (11), [1,2,3,5,7,11])
	def test_not_one (self):
		self.assertTrue(solution(0 or 1), ValueError("Not prime number"))

if __name__ == '__main__':
	unittest.main()
