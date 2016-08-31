import re
def describe(s):
    sets = re.findall("(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)", s)
    return "".join([str(len(x)) + x[0] for x in sets])
s = '1'
for i in range(30):
    s = describe(s)
print(len(s))