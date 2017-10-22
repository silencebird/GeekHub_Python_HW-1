"""
4. Write a script to concatenate N strings.
"""

n = int(input("input quantity of strings: "))
s = ""
for i in range(1,n+1):
    s += str(input("Input string: "))
print (s)