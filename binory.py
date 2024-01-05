string =input('enter a string:-')
i=0
out=''
while i<len(string):
    if niot('A'<=string[i] <'z' or '0'<=string[i]<='9'):
        out =out+'-'
    else:
        out=out+string[i]
        i=1
 print(out)