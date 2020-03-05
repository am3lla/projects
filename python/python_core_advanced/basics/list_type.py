#!/usr/bin/env python3

l = []
print( f"{ l= }" )

l = [10, 20, "Bharath", -10, 30.5]
print( f"{ l= }" )
print( f"{ l[3]= }" )
print( f"{ l[3:5]= }" )
print( f"{ l*4= }" )
print( f"{ len(l)= }" )

l.append(40)
l.remove("Bharath")
print( f"{ l= }" )
del(l[1])
print( f"{ l= }" )

m = l.copy()
m.clear()
print( f"{ len(m)= }" )

print( f"{max(l)= }" )
print( f"{min(l)= }" )

l.insert(3, 99)
print( f"{ l= }" )

l.sort()
print( f"{ l= }" )

l.sort(reverse = True)
print( f"{ l= }" )
