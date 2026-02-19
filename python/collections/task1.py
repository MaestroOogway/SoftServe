divisiblebytwo = []
divisiblebythree = []
notdivisiblebytwoandthree = []

for i in range(1,11):
    if (i%2==0):
        divisiblebytwo.append(i)
    if (i%3==0):
        divisiblebythree.append(i)
    elif(i%2!=0 and i%3!=0):
        notdivisiblebytwoandthree.append(i)

print(
    f"Numbers divisible by two: {divisiblebytwo}\n"
    f"Numbers divisible by three: {divisiblebythree}\n"
    f"Not divisible by two or three: {notdivisiblebytwoandthree}"
)