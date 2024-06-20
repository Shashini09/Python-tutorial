def pow(x,n):
    if n==0:
        return 1
    else:
        return x* pow(x,(n-1))
while True:
    x=int(input('enter number'))
    if x==-1:
        print('finished')
        break
    else:
        n=int(input("enter the number n:"))
        print("output:",pow(x,n))
        
        
