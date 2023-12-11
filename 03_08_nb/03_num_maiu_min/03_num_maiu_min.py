def up_low(s):
    nlow=nupp=0
    for car in s :
        if car.islower() : 
            nlow += 1 
        elif car.isupper() : 
            nupp += 1

    print (f"No. of Upper case characters :  { nupp }" )
    print (f"No. of lower case characters :  { nlow }" )
       

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

