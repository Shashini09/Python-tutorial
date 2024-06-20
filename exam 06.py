def sumcube(n):
    if n==1 :
        return 1
    else:
        return  sumcube(n-1)+n*n*n

while True:
    n=int(input('enter number'))
    if n==-1:
        print("finished")
        break
    else:
        print("Output",sumcube(n))
