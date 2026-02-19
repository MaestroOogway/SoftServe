def counter(listh):
    newlist= []
    for i in range(len(listh) - 1, -1, -1):
        newlist.append(listh[i])
    return newlist

listmy = [324,78,4,0,23,98]
print(counter(listmy))