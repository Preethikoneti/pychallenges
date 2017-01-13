# Interview Cake Question 5
# https://www.interviewcake.com/question/python/coin
# I had help:
#   https://www.youtube.com/watch?v=EScqJEEKC10

def is_int(num):
    if type(num) is int:
        return True
    return False

def is_lst(lst):
    if type(lst) is not list:
        return False
    return True

def is_lst_of_nums(lst):
    if is_lst(lst) != True:
        return False
    else:
        for elem in lst: 
            if is_int(elem) != True:
                return False
    return True

def is_valid_input(num, lst):
    return False if is_int(num) != True or is_lst_of_nums(lst) != True else True
    
def change(amount, coins_available, coins_so_far):
    False if is_valid_input(amount, coins_available) != True else True
    if sum(coins_so_far) == amount: #if sum so far equals target, then yield list
        yield coins_so_far
    elif sum(coins_so_far) > amount: #if sum is greater than target, we've gone too far so pass
        pass
    elif coins_available == []: #if there are no more coins to use, then pass
        pass
    else:
        # Recursively loop through coins available against the first coins available
        for coin in change(amount, coins_available[:], coins_so_far+[coins_available[0]]): 
            yield coin
        # Recursively loop through coins available minus the first coin
        for coin in change(amount, coins_available[1:], coins_so_far):
            yield coin

def test_datatypes():
    test_1 = 5
    if is_int(test_1) != True:
        print "Test 1: Element should be an integer but got " + str(test_1) + "."
    test_2 = [1,2,3]
    if is_lst(test_2) != True:
        print "Test 2: Should return True if provided a valid list data type."
    test_3 = [1,2,3]
    if is_lst_of_nums(test_3) != True:
        print "Test 3: Should return True if provided a valid list data type containing integers."
    if is_valid_input(4, [1,2,3]) != True:
        print "Test 4: Should return True if provided a valid integer of money and a list of denominations."
        
def test_change():
    test1_amount = 15
    test1_denoms = [1, 5, 10, 25]
    if len([s for s in change(test1_amount, test1_denoms, [])]) != 6:
        print "Solution should return 6 for amount " + str(test1_amount) + " with denominations of " + str(test1_denoms)
    test2_amount = 20
    test2_denoms = [1, 5, 10, 25]
    if len([s for s in change(test2_amount, test2_denoms, [])]) != 9:
        print "Solution should return 6 for amount " + str(test1_amount) + " with denominations of " + str(test1_denoms)
    
# Run tests
def run_tests():
    test_datatypes()
    test_change()
    
# Main Program
def main():
    # Call Tests
    run_tests()
    # Continue 
    amount = 4
    denoms = [1, 2, 3]
    solution = ([s for s in change(amount, denoms, [])])
    for s in solution:
        print s
    print "Total number of solutions: " + str(len([s for s in change(amount, denoms, [])]))
   
main()