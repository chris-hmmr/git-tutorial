def find_smallest(a,b,c):
  x = int(a)
  y = int(b)
  z = int(c)
  smallest = 0
  if x < y and x < z:
    smallest = x
  elif  y < z:
    smallest = y
  else :
    smallest = z

  return smallest

print("The smallest number is :", find_smallest (2,4,8))

print ("Hallo my name is Ray")