data=[[[1,2],[3,4]],[[5,6],[7,8]]]
def ttt(m):
    v=m[0][0]
    for row in m:
        for element in row:
            if v<element: v=element
    return v
print(ttt(data[0]))
