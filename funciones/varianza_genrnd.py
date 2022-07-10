import math
def varianza_genrnd(arg):
  sum=0
  med=0

  for i in arg:
    med+=i
  
  media= med/len(arg)
  
  for i in arg:
    sum+= (i-media)*(i-media)

  var_cuad=sum/len(arg)
  return math.sqrt(var_cuad)


