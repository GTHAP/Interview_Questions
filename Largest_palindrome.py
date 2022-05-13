# Finf the largest palindrome by three digit numbers
# Time complexity - O(N^2)
# Space complexity - O(1)

def largestPalindromeByThreeDigitNumbers():
	largestPalindrome = 0
	for i in range(100, 999):
		for j in range(101, 1000):		
			temp = i * j
			tempString = str(temp)
			if tempString == tempString[::-1]:
				largestPalindrome = temp
	return largestPalindrome
	
largestPalindromeByThreeDigitNumbers()
