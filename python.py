def vowelindex(a):
    l=[]
    i=0
    while i<len(a):
        if a[i] in 'aeiouAEIOU':
            l=l+[i]
        i+=1
    return l
b=vowelindex('aeiouAEIOU')
print(b)
