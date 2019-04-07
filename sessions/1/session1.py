# comment

print("We can print")
5 / 2
5 // 2
5 % 2
1.1 + 2
2**16


variable = "string value"
variable = 0
variable = None
variable = True
variable = True if 6 > 3 else False

"string in double \t (tab) quotes \n new line"
'string in single quotes \n \t the same'
f'formatted string can contains variables {variable} or expressions {5+2}' # since 3.6
'formatted string can contains variables {variable} or expressions '.format(variable=variable) # sinse 3.0
c = "somestring"[4]
c = "somestring"[2:4]
c = "somestring"[::2]
c = "somestring"[::-1]
len(c)
c = "ab" + "edc"[::-1]

variable = True or False
variable = not variable
variable = None
variable is None

# we can compare
"0" == 0 # False
bool("") # False

variable = not True and not False
if variable:
    print("YES")
else:
    print("No")

for i in range(1,3):
    print(f"for {i}")

import random

while True:
    value = random.randint(0, 4)
    print(f"variable is {value}")
    if not value:
        break

while False:
    pass
else:
    print("While loop stop")

print("After while")

# good place to continue https://learnxinyminutes.com/docs/python3/