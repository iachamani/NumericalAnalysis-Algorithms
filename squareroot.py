def squareroot(a,precision):
    y = a
    while(True):
      root = 1/2*(y+a/y)
      if abs(root-y) <= precision:
        break
      y = root
    return root
   
x = float((input("Type a number : ")))
#precision
l = 0.000000001
result = squareroot(x,l)
print(result)


