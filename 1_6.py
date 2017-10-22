"""
6. Write a script to check whether a specified value is contained in a group of values.
		Test Data :
		3 -> [1, 5, 8, 3] : True
		-1 -> (1, 5, 8, 3) : False
"""

n = input()
l = [1, 5, 8, 3]
t = (-1, 5, 8, 3)
l = str(l[:])
t = str(t[:])
print(n in l)
print(n in t)