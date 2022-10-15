
def nearest_square(num):
    if num < 0:
        return 0
    start = 1
    while start**2 <= num:
        start+=1
    return start **2
