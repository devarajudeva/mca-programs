password=input ('enter a password')
validate={
    'upper':false,
    'lower':false,
    'num':false,
    'char':false}
if len(password)>=8:
 for char in password:
if 'A'<=char <='Z':
 validate['upper']=true
elif 'a' <=chr<='Z':
validate['lower']=true
elif '0'<=char <='9':
    validate['num']=true
elif char!='':
        validate['char']=true
        elif char =='':
            validate['space']=true
            if(
                validate ['upper'] and
                validate['lower'] and
                validate['char'] and
                validate['num' ]and
                print ('password is valid')
            )
elif:
    print ('password is invalid')