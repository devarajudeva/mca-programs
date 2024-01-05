def sample(a,b):
   for i in range(a,b+1):
       yield i*2
       yield i*5
out =sample (5,15)
print(list(out))
