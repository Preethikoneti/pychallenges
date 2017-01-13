def remove_duplicates(list):
    newlist = []
    for e in list:
        if e not in newlist:
            newlist.append(e)
    return newlist

print remove_duplicates([1,1,2,2,3,4,5,5])