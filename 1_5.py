"""
5. Write a script to convert decimal to hexadecimal
		Sample decimal number: 30, 4
		Expected output: 1e, 04
"""

n = str(input("input decimal numbers: "))
dec_list = n.split(",")
dec_list = list(map(int, dec_list))
dec_list = list(map(hex, dec_list))
for i in  dec_list:
    print(i.split('x')[-1], end=" ")