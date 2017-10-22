"""
8. Write a script to replace last value of tuples in a list.
		Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
		Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
x = 100
j = 0
for i in l:
    i = list(i)
    i[-1] = x
    l[j]= tuple(i)
    print (i)
    j+=1
print(l)
