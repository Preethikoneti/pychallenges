# Question at https://www.interviewcake.com/question/python/merging-ranges

# Returns True if a tuple is valid or false if NOT valid
def is_valid_tuple(tpl):
    return False if type(tpl) is not tuple or len(tpl) != 2 or tpl[0] >= tpl[1] else True

def is_valid_tuple_array(lst):
    if type(lst) is not list:
        return False
    if len(lst) == 0:
        return True
    for tpl in lst:
        if is_valid_tuple(tpl) is False:
            return False
    return True

def between_inclusive(tpl, item):
    return ((item >= tpl[0]) and (item <= tpl[1]))

def is_overlaping(left, right):
    return between_inclusive(left, right[0]);

def merge_tuples(left, right):
    return (left[0], max(left[1], right[1]))

def condensed_ranges(meetings):
    if is_valid_tuple_array(meetings) == False:
        return []
    if len(meetings) == 1:
        return meetings
    meetings_sorted = sorted(meetings, key=lambda tup: tup[0])
    cur = 1
    new_meetings = [meetings_sorted[0]]
    while (cur < len(meetings_sorted)):
        nm_last = len(new_meetings)-1
        if (is_overlaping(new_meetings[nm_last],meetings_sorted[cur])):
            new_meetings[nm_last] = merge_tuples(new_meetings[nm_last],meetings_sorted[cur]) 
        else:
            new_meetings.append(meetings_sorted[cur])
        cur = cur + 1
    return new_meetings

def test_cases_condensed():
    if condensed_ranges([2, 1]) != []:
        print "Condensed range should be empty when invalid data is provided."
    if condensed_ranges([(0, 1)]) != [(0, 1)]:
        print "Should return a condensed range of [(0,1)]"
    result1 = condensed_ranges([(3, 5),(1, 2)])
    if result1 != [(1, 2),(3, 5)]:
        print "Should return a sorted and condensed range of [(1, 2),(3, 5)] but got " + str(result1)
    result2 = condensed_ranges([(1, 2),(2, 4)])
    if result2 != [(1, 4)]:
        print "Should return a sorted and condensed range of [(1, 4)] but got " + str(result2)
    result3 = condensed_ranges([(1, 2),(2, 4),(5, 6)])
    if result3 != [(1, 4),(5, 6)]:
        print "Should return a sorted and condensed range of [(1, 4),(5, 6)] but got " + str(result3)
    result4 = condensed_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    if result4 != [(0, 1), (3, 8), (9, 12)]:
        print "Should return a sorted and condensed range of [(0, 1), (3, 8), (9, 12)] but got " + str(result4)
    result5 = condensed_ranges([(6, 9), (0, 1), (1, 3), (3, 7)])
    if result5 != [(0, 9)]:
        print "Should return a sorted and condensed range of [(0, 9)] but got " + str(result5)

def test_cases_check_for_overlaps():
    if is_overlaping((1, 4), (2, 8)) != True:
        print "Tuples should be overlaping."
    if is_overlaping((1, 4), (9, 11)) != False:
        print "Tuples should not be overlaping."
    if is_overlaping((1, 4), (2, 3)) != True:
        print "Tuples should be overlaping."
    if is_overlaping((1, 4), (4, 6)) != True:
        print "Tuples should be overlaping."
    if is_overlaping((1, 4), (1, 4)) != True:
        print "Tuples should be overlaping."

def test_cases_merge_tuples():
    if merge_tuples((1,2),(2,4)) != (1,4):
        print "A: Tuples should merge"
    if merge_tuples((1,3),(1,5)) != (1,5):
        print "B: Tuples should merge"
    if merge_tuples((2,8),(2,8)) != (2,8):
        print "B: Tuples should merge"
    if merge_tuples((1,9),(3,5)) != (1,9):
        print "B: Tuples should merge"

def test_cases():
    test1 = condense_ranges([])
    if test1 != []:
        print "Empty list should contain no entries."
    test2 = condense_ranges([()])
    if test2 != "All tuples must have two numberic elements.":
        print "All tuples must have two numberic elements." 

def test_cases_tuples():
    if is_valid_tuple([]) != False:
        print "A: Should return False when a non tuple is passed."
    if is_valid_tuple(()) != False:
        print "B: Should return False when a non tuple is passed."
    if is_valid_tuple((1)) != False:
        print "C: Should return False when a non tuple is passed."
    if is_valid_tuple((3,2)) != False:
        print "D: Should return False when a non tuple is passed."
    if is_valid_tuple((1,2,3)) != False:
        print "E: Should return False when a non tuple is passed."
    if is_valid_tuple((1,3)) != True:
        print "Should be a valid tuple."

def test_cases_tuples_list():
    if is_valid_tuple_array([]) != True:
        print "A: Should return True if provided an empty list []."
    if is_valid_tuple_array([(1, 2)]) != True:
        print "B: Should return True if provided a list of valid tuples."
    if is_valid_tuple_array([(2, 1)]) != False:
        print "C: Should return False if provided a list that contains an invalid tuple."
    if is_valid_tuple_array([(1, 2),(2, 1)]) != False:
        print "D:fffffff Should return False if provided a list that contains an invalid tuple."
    if is_valid_tuple_array([(1, 2),(3, 4),(3, 6)]) != True:
        print "E: Should return True if provided a list of valid tuples."
    if is_valid_tuple_array(1) != False:
        print "F: Should return False if a list is not provided."
        
test_cases_merge_tuples()
test_cases_check_for_overlaps()
test_cases_tuples()
test_cases_tuples_list()
test_cases_condensed()
print condensed_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])