#loopnumbers.py
for i in range (1, 100+1):
    #print i;
    if i % 4 == 0:
        print "Linked"
    elif i % 6 == 0:
        print "In"
    elif i % 4 == 0 and i % 6 == 0:
        print "LinkedIn"