#!/usr/bin/env python3

tpl = ()
print(f"{ tpl= }")

tpl = (40, 50, 40, "XYZ")
print(f"{ tpl= }")

tpl = ( 40 )
print(f"{ tpl= }, { type(tpl)= }")

tpl = (40, 50, 40, "XYZ")
print( f"{ tpl= } { type(tpl) = }" )
print( f"{ tpl[3]= }")
print( f"{ tpl*3= }")
print( f"{ tpl.count(40)= }" )
print( f"{ tpl.index('XYZ')=} ")

lst = [67, 34, "XYX"]
print(f"{ lst= } { type(lst)= }")

tpl1 = tuple(lst)
print(f"{ tpl1= } { type(tpl1)= }")
