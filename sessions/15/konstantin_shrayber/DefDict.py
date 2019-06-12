import collections

def factorial(x: int):
    res = 1
    for i in range(1, x+1):
        res = res * i
    return res

defdict = collections.defaultdict(lambda:factorial)

for i in range(7):
    defdict[i] = defdict[i](i)

print(defdict)