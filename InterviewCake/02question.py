# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# 
# For example, given:
# 
#   [1, 7, 3, 4]
# 
# your function would return:
# 
#   [84, 12, 28, 21]
# 
# by calculating:
# 
#   [7*3*4, 1*3*4, 1*7*4, 1*7*3]
# 
# Do not use division in your solution.

# Will return an empty list if provided with an empty list, or a list with only one element
def get_products_of_all_ints_except_at_index(list_of_ints):
	if len(list_of_ints) <= 1:
		return [] 
	product = 1
	list = []
	# This is a solution but not the one they wanted.
# 	for index, num in enumerate(list_of_ints, start=0):
# 		product = product * num
# 	for index, num in enumerate(list_of_ints, start=0):
# 		list.append(product/num)
	for index, num in enumerate(list_of_ints, start=0):
		for index2, num2 in enumerate(list_of_ints, start=0):
			if index != index2:
				product = product * num2
		list.append(product)
		product = 1
	return list
	
def test_cases():
	result1 = get_products_of_all_ints_except_at_index([])
	if result1 != []:
		print "Expect a list to be empty when empty list is passed to function."
	result2 = get_products_of_all_ints_except_at_index([5])
	if result2 != []:
		print "Expect a list to have at least two elements."
	result3 = get_products_of_all_ints_except_at_index([1,7])
	if result3 != [7,1]:
		print "Expect result to be [7,1]"
	result4 = get_products_of_all_ints_except_at_index([1,6,9,5])
	if result4 != [270,45,30,54]:
		print "Expect result to be [270,45,30,54]"
		
test_cases()