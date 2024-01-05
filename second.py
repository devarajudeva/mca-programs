a=[1,2,6,3,1,5,88,6,35,90]
out=a[0]
out2=a[0]
for i in a:
    if out<i  :
        out2=out
        out=i
    elif out2<i:
        out2=i
print(out,out2)