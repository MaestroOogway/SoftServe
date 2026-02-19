def largest(a,b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: The largest number
    """
    largestn = 0
    if (a > b):
        largestn = a
    elif (b > a):
        largestn = b
    else:
        largestn = a = b

    return (f"the largest num is: {largestn}")

print(largest(50,100))