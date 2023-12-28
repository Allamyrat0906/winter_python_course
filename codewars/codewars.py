

def proc_arr(arr):
    sum = ""
    smaller = sorted(arr)
    higher = smaller(reverse=True)
    for i in smaller:
        sum = sum+i

    print(sum)
    print(higher)


proc_arr(['1', '2', '2', '3', '2', '3'])
