def var(x):
   print(x,id(x))
   x.append(4)
   print(x,id(x))

x = [1,2,3]   
var(x)
print(x,id(x))