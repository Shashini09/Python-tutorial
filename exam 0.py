def multiply(M,n):
    if n==1:
        return M
    else:
        return (M + multiply(M,n-1))

while True:
        n=int(input('enter number n'))

        if n == -1:
            print("finished")
            break
        
        M=int(input("Enter number M:"))
        print(multiply(M,n))
              
        
        
