l = [1,2,3,4,5,6]
def liste():
    if len(l) <2:
        return
    l[0], l[-1] = l[-1], l[0]
    print(l)
liste()
