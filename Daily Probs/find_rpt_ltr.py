"""This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null."""
def dups(s):
	for i in s :
		res = i if s.count(i)> 1 else 0
		if res:
			return res
	return None

# o/p
print(dups('abcdbef'))