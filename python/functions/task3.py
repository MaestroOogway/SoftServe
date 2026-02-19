def numberofc(mystring):
    result = {}
    characters = "".join(dict.fromkeys(mystring))

    for i in characters:
        times = mystring.count(i)
        result[i] = times
    
    return result


print(numberofc("fabian"))