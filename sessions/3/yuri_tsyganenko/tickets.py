
def goodNumbers():
  sums = {}
  for s in range(0, 28):
    sums[s] = []

  for i1 in range(10):
    for i2 in range(10):
      for i3 in range(10):
        sums[i1 + i2 + i3].append((i1, i2, i3))

  for s in range(0, 28):
    for left in sums[s]:
      for right in sums[s]:
        yield "{}{}{}{}{}{}".format(left[0], left[1], left[2], right[0], right[1], right[2])


cnt = 0
for i in goodNumbers():
  cnt+=1

print(cnt)

