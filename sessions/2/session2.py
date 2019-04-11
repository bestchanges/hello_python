# tuples
t = ()
print(t)
print(type(t))

t = (1, 'a')
v1, v2 = t
print(v1, v2)

t = 2, 'b'
v1, v2 = t
print(v1, v2)
t = 2, 'b', 'c'
# v1, v2 = t
# print(v1, v2)


# dicts

# sets
s = set()
s1 = {0,1,2,3,2,4}
print(s1)
s2 = {1,2,4,6}
print(s1 - s2)
#print(s1 + s2)
print(s1 & s2)
# print(s1 / s2)
print(s1 | s2)
print(s1 ^ s2)

# id, hash
s1 = "string"
s2 = "string"
print(id(s1))
print(id(s2))

#  https://learnxinyminutes.com/docs/python3/