"""
13. Write a script to get the maximum and minimum value in a dictionary.
"""


from functools import reduce
dic = {'1': '10', '2': '20', '3': '30', '4': '40', '5': '50', '6': '60', '7': '10', '8': '40'}

max_value = reduce(lambda x, y: max(x,y), dic.values())
min_value = reduce(lambda x, y: min(x,y), dic.values())
print (max_value)
print (min_value)