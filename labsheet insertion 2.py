A=[]

for v in range(10):
    A.append(int(input('enter the number:')))

print(A)

def insertionsort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1

        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
    A[i+1]=key

insertionsort(A)
print('sorted Array')
for k in range(len(A)):
    print(A[k])

minimum=A[0]
maximum=A[-1]


print ('minimum value',minimum)
print('maximum value',maximum)


average = sum(A) / len(A)
print('average',average)
