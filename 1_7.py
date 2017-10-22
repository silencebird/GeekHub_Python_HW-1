"""
7. Write a script to concatenate all elements in a list into a string and print it.
"""

k = int(input("input quantity of strings: "))
n=[]
for i in range(1, k+1):
    n.append(input("input string: "))
s = ''.join(n)
print (s)
