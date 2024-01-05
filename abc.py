rows=int(input('no of rows:-'))
cols=int(input('no of cols:-'))
for i in range(rows):
    for j in range(cols):
        if i == 0 or i==rows-1:
           print('+',end=' ')
        else:
            if j==0 or j == cols-1 or j==i or rows-i-1 ==j:
                print('+',end =' ')
            else:
                print(' ',end=' ')

    print()