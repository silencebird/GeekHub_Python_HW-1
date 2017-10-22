"""
1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
		Sample data : 1, 5, 7, 23
		Output :
		List : [‘1', ' 5', ' 7', ' 23']
		Tuple : (‘1', ' 5', ' 7', ' 23')
"""

s = str(input("type numbers: "))
list_type = []
tuple_type = ()
list_type = s.split(",")
tuple_type  = tuple(list_type)
print (tuple_type)
print (list_type)