a = "q w e r t y u i o p"
aa = a.split()
b = "a s d f g h j k l"
bb = b.split()
c = "z x c v b n m"
cc = c.split()
d = input()
d = d.lower()
x,y,z = "","",""
for i in d :
    if i in aa :
        x = x + i
for i in d :
    if i in bb :
        y = y + i
for i in d :
    if i in cc :
        z = z + i
if x == d or y == d or z == d:
    print("Yes")
else:
    print("No")
