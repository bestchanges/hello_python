# comment

print("Hello world")

# if (length("string") > 0) {
#     int a = 0;
#     print("something");
# }
if "string":
    a = 0
    print("something")

print("====================================")

print(5 / 2)
print(5 // 2)
print(5 % 2)
print(1.1 + 2)
print(2**16)

print("====================================")

variable = "string value"
variable += " add string"
variable = 0
variable += 1
variable = None
variable = True
variable = True if 6 > 3 else False
print(type(variable))

print("====================================")

"string in double \t (tab) quotes \n new line"
'string in single quotes \n \t the same'

print("concatenate " + 'strings')
print("but only strings! " + str(True) + ' ' + str(18))

print(f'since 3.6 f-strings expand variables {variable} or expressions {5+2}')
print('since 3.0 format function of string {variable}'.format(variable=variable))
print('or by positions {} {}'.format("position1", 12+8))
print('old-school formattings %s %04d %.2f' % ("string", 18, 3.1415))

print("subrange"[4])
print("subrange"[2:4])
print("subrange"[::2])
print("reverse"[::-1])
print("ab" + "edc"[::-1])
print(len("string"))

print("====================================")

print(True or False)
variable = None
print(not False)
print(variable is None)
print(variable is False)
print(not True and not False)

print(bool(0))
print(bool(""))
print(bool([]))

print("====================================")

# we can compare different types
print("0" == 0) # False
print(0 == False) # True
print(0 is False) # False

print("====================================")

tuple = ("some", 1, False, 18)
print(tuple)

print("====================================")

variable = "18"
if variable == 18:
    print("yes int 18")
elif variable == False:
    print("yes False")
else:
    print("Other case")

for i in (1, 2, 3, 4):
    print(f"for over tuple {i}")

for i in range(0,3):
    print(f"for in range {i}")

i = 0
while i < 2:
    print(f"In while i={i}")
    i += 1

import random
while True:
    value = random.randint(0, 4)
    print(f"variable is {value}")
    if not value:
        break

while False:
    pass
else:
    print("While loop finished")

# No DO-WHILE
# No SWITCH-CASE

print("====================================")


# now let's go to projects/guess_game
# good place to continue https://learnxinyminutes.com/docs/python3/