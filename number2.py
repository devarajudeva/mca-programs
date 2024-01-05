num=int(input('enter a number:-'))
i=1
temp=false
while i<num:
   if num%i==0 and i!=1 and i!=num:
        temp=true
        i+=1
if not temp:
     print("it is a prime")
 else:
      print("it is not prime")
      
            