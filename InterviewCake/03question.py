# Given a list_of_ints, find the highest_product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

# Will return an empty list if provided with an empty list, or a list with only one element
def highest_product(list_of_ints):
	if len(list_of_ints) < 3:
		return None
	list_of_ints = sorted(list_of_ints, reverse=True)
	return list_of_ints[0] * list_of_ints[1] * list_of_ints[2] 
	
def test_cases():
	result1 = highest_product([])
	if result1 is not None:
		print "Empty list should return 0."
	result2 = highest_product([5])
	if result2 is not None:
		print "List should contain at least 3 elements"
	result3 = highest_product([5,2])
	if result3 is not None:
		print "List should contain at least 3 elements"
	result4 = highest_product([5,2,4])
	if result4 != 40:
		print "Highest product should have been 40, given [5,2,4]"
	result5 = highest_product([6,5,10,5])
	if result5 != 300:
		print "Highest product should have been 300, given [6,5,10,5]"
test_cases()