def purify(list):
    nlist = []
    for e in list:
        if e % 2 == 0:
            nlist.append(e)
    return nlist
    
print purify([1,2,3,4,5,6,7,8,9])