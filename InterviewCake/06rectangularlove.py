# Interview Cake #6 
# https://www.interviewcake.com/question/python/rectangular-love
# Returns True if a tuple is valid or false if NOT valid

def is_int(num):
    if type(num) is int:
        return True
    return False

def is_valid_tuple(tpl):
    return False if type(tpl) is not tuple or len(tpl) != 4 or is_int(tpl[0]) != True or is_int(tpl[1]) != True else True

def between_inclusive(tpl, item):
    return ((item >= tpl[0]) and (item <= tpl[1]))

def is_between(range, pos):
    return between_inclusive(range, pos);

def find_x_overlap(Axywh, Bxywh):
    print "find_x_overlap"
    cords = (Axywh, Bxywh)
    for cord in cords:
        if is_valid_tuple(cord) != True: return False
    print "Rectange 1: x=" + str(Axywh[0]) + ", y=" + str(Axywh[1]) + ", w=" + str(Axywh[2]) + ", h=" + str(Axywh[3])
    print "Rectange 2: x=" + str(Bxywh[0]) + ", y=" + str(Bxywh[1]) + ", w=" + str(Bxywh[2]) + ", h=" + str(Bxywh[3])
#     if Axywh[0] > Bxywh[0]:
#         print "Coordinate A(x) " + str(Axywh[0]) + " is greater than " + "coordinate B(x) " + str(Bxywh[0])
#     if Axywh[0] < Bxywh[0]:
#         print "Coordinate A(x) " + str(Axywh[0]) + " is less than " + "coordinate B(x) " + str(Bxywh[0])
    range = (Axywh[0], Axywh[2])
    pos = Bxywh[0]
    if is_between((range), pos):
        print str(pos) + " is between " + str(range[0]) + " and " + str(range[1])
    else:
        print str(pos) + " is NOT between " + str(range[0]) + " and " + str(range[1])
        
def find_y_overlap(Axywh, Bxywh):
    print "find_y_overlap"
    cords = (Axywh, Bxywh)
    for cord in cords:
        if is_valid_tuple(cord) != True: return False
    print "Rectange 1: x=" + str(Axywh[0]) + ", y=" + str(Axywh[1]) + ", w=" + str(Axywh[2]) + ", h=" + str(Axywh[3])
    print "Rectange 2: x=" + str(Bxywh[0]) + ", y=" + str(Bxywh[1]) + ", w=" + str(Bxywh[2]) + ", h=" + str(Bxywh[3])
#     range = (Axywh[1], Axywh[3])
#     pos = Bxywh[1]
#     if is_between((range), pos):
#         print str(pos) + " is between " + str(range[0]) + " and " + str(range[1])
#     else:
#         print str(pos) + " is NOT between " + str(range[0]) + " and " + str(range[1])

def locate_intersection(cords):
    # Test for valid tuple
#     i = 1
    for cord in cords:
        if is_valid_tuple(cord) != True: return False
    if len(cords) != 2:
        print "Valid set of cordinates is ((x, y), (x, y)) as contained in two tuples."
    else:
        find_x_overlap((cords[0][0], cords[0][1]), (cords[1][0], cords[1][1]))
#         print "COORDINATES:"
#         print str(cords[0][0]) + " " + str(cords[0][1])
#         print str(cords[1][0]) + " " + str(cords[1][1])
#     print i
#     i = i + 1

def run_tests():
    
    def test_cases_tuples():
        if is_valid_tuple([]) != False:
            print "Tuple Test 1: Should return False when a non tuple is passed."
        if is_valid_tuple(()) != False:
            print "Tuple Test 2: Should return False when a non tuple is passed."
        if is_valid_tuple((1)) != False:
            print "Tuple Test 3: Should return False when a non tuple is passed."
        if is_valid_tuple((1, 2, 3, 4)) != True:
            print "Tuple Test 4: Should return True when a tuple of more than four elements is passed."
        if is_valid_tuple((1, 3)) != False:
            print "Tuple Test 5: Should be a valid tuple of four elements."
        if is_valid_tuple(("a", 3)) != False:
            print "Tuple Test 6: Should be a valid tuple of integer elements."
    
    def test_find_x_overlap():
        # Coordinates are ((x, y, w, h), (w, y, w, h))
        rect1_xywh = (1, 5, 10, 5)
        rect2_xywh = (8, 7, 5, 10)
        result = find_x_overlap(rect1_xywh, rect2_xywh)
#         if result != ((11, 10)):
#             print "Test 1: Should return (11, 9) if given " + str(rect1_xywh) + ", " + str(rect2_xywh) + " but got " + str(result)
        rect1_xywh = (1, 5, 10, 4)
        rect2_xywh = (8, 1, 10, 5)
        result = find_x_overlap(rect1_xywh, rect2_xywh)
#         if result != ((11, 10)):
#             print "Test 2: Should return (11, 9) if given " + str(rect1_xywh) + ", " + str(rect2_xywh) + " but got " + str(result)

    def test_find_y_overlap():
        # Coordinates are ((x, y, w, h), (w, y, w, h))
        rect1_xywh = (1, 5, 10, 15)
        rect2_xywh = (8, 7, 5, 10)
        result = find_y_overlap(rect1_xywh, rect2_xywh)
        
        rect1_xywh = (1, 5, 10, -25)
        rect2_xywh = (12, 7, 5, 10)
        result = find_y_overlap(rect1_xywh, rect2_xywh)
    
#     def test_locate_intersection():
#         test1_xy1 = (8, 7)
#         test1_xy2 = (11, 10)
#         result = locate_intersection((test1_xy1, test1_xy2))
#         if result != ((8, 10), (11, 7)):
#             print "Test 1: Should return ((8, 10), (11, 7)) if given (" + str(test1_xy1) + ", " + str(test1_xy2) + ") but got " + str(result)
#         test2_xy1 = (11, 9)
#         test2_xy2 = (8, 1)
#         result = locate_intersection((test2_xy1, test2_xy2))
#         if result != ((8, 5), (11, 6)):
#             print "Test 2: Should return ((8, 6), (11, 5)) if given (" + str(test2_xy1) + ", " + str(test2_xy2) + ") but got " + str(result)

    # Call Test Case Functions   
    test_cases_tuples()
    test_find_x_overlap()
    test_find_y_overlap()
#     test_locate_intersection()

# Main Program
def main():
    # Call Tests
    run_tests()
    # Continue 
    # "Nothing to do yet."
   
main()