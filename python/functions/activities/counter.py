def counter(text):
    newtext = ""
    for i in range(len(text) - 1, -1, -1):
        newtext = newtext + text[i]
    return newtext

userin = (input("Write something: "))
print(counter(userin))