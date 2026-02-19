def probability(lst, num):
    newlist = []
    for i in lst:
        if i >= num:
            newlist.append(i)

    prob = 100 * (len(newlist)) / len(lst)
    return prob

milist = [0,5,3,10,1]
n = 7

print(probability(milist,n))