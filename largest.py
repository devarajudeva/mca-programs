a=[1,9,11,21,65,78,143]
out=a[0]
out2=a[0]
for var in a:
    if out<var:
        out=var
for var in a:
    if out2<var and var!=out:
        out2=var
print(out2)