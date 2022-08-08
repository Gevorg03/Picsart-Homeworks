# def intersect(lst1, lst2):
#     intersect_lst = []
#     for el_lst1 in lst1:
#         for el_lst2 in lst2:
#             if el_lst1 == el_lst2:
#                 intersect_lst.append(el_lst2)
#     return intersect_lst
# print(intersect([1, 2, 3], [2, 3, 4]))

def degree(lst:list):
    max_count = lst.count(lst[0])
    element = lst[0]
    index2 = None
    # kamanc grum enq
    for el in lst:
        if max_count < lst.count(el):
            max_count = lst.count(el)
            element = el

    index1 = lst.index(element)
    reversed_lst = reversed(lst)
    for i in range():
        if reversed_lst[i] == element:
            index2 = i

#    for i in range(index1, index2+1):
#        print(lst[i])
print(degree([1,2,2,3,1,4,2, 3]))

