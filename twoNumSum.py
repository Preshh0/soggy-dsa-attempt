def twoNum(array,sum):
    for i in array:
        j = sum - i
        if j in array:
            return (i, j)

one = [1,23,4]
sum = 5
twoNum(one,sum)

