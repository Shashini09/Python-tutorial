A=[]

for v in range (5):
    A.append(int(input('enter the number')))

print(A)

def partition (A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<= x:
            i=i+1
            A[i],A[j] =A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

quicksort(A,0,len(A)-1)
print("sorted'")
for k in range (len(A)):
    print(A[k])

mean=sum(A)/len(A)
print('mean',mean)


n=len(A)

if n%2==0:
    meadian=(A[n//2-1]+A[n//2])/2
else:
    meadian=(A[n//2])

print('meadian',meadian)
