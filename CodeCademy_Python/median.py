def median(list):
    print "Unsorted list: " + str(list)
    list = sorted(list)
    print "Sorted list: " + str(sorted(list))
    print "Modulo: " + str(len(list) % 2)
    print "Length of list: " + str(len(list))        
#     for index, item in enumerate(list, start=0):   # default is zero
#         print(index, item)

    if len(list) > 1:
        enumerate(list, start=0)
        pos1 = len(list) / 2-1
        pos2 = len(list) / 2
        print (list[pos1])
        print (list[pos2])
        if len(list) % 2 == 0:
#             enumerate(list, start=0)
            print "Index and Value (Left, Right): " + str(pos1) + " & " + str(list[pos1]) + ", " + str(pos2) + " & " + str(list[pos2])
            return (list[pos1] + list[pos2]) / 2.0
        else:
            return list[pos2]
    else: 
        return 1
    
print median([6, 8, 12, 2, 23])