"""
9. Write a script to replace last value of tuples in a list.
		Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
		Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""

l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l = list(filter(lambda x: x != (), l))
l[-1] = list(l[-1])

print(l)