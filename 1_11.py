"""
11. Write a script to remove duplicates from Dictionary.
"""

dic = {'1': '10', '2': '20', '3': '30', '4': '40', '5': '50', '6': '60', '7': '10', '8': '40'}
dic1 = dic.copy()
t = []
for key, value in dic.items():
        if value not in t:
            t.append(value)
        else:
            dic1.pop(key)
dic = dic1
print(dic)