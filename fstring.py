#f string
import math
me = "datta"
a1  = 3
#a = "this is %s %s"%(me, a1)
#a = "this is {1} {0}"
#b = a.format(me, a1)
#print(b)
a = f"this is {me} {a1} {34*23}{math.sin(45)}"
print(a)