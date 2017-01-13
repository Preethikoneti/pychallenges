def reverse(t):
    t_list = list(t)
    r_list = []
#     print "List of text: " + str(t_list)
    t_Index = len(t_list)-1
#     print "Length of list: ", str(t_Index)
    for e in t_list:
#         print t_list[t_Index]
        r_list.append(t_list[t_Index])
        t_Index -= 1
    r_list = ''.join(r_list)
    return r_list
    
text = "hello"
print reverse(text)