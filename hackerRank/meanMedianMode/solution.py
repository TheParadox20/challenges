#n=int(input()) #number of elements
#x=input() #elemnts
n=5
x="9 5 7 1 3"
arr=x.split(' ')
for i in range(0,len(arr)):
    arr.append(int(arr[0]))
    arr.pop(0)
def mean(n):
    sum=0
    for i in arr:
        sum=sum+int(i)
    return sum/n
def median(n):
    arr.sort()
    if n%2!=0:
        middle=int((n/2))
        return arr[int(middle)]
    else:
        middle=int(n/2)
        return (arr[middle]+arr[middle-1])/2
def mode(n):
    arr.sort()
    arr.append('-1')
    #create a element count pair array
    elementCount=[]
    count=1
    for i in range(0,len(arr)-1):
        current=arr[i]
        next=arr[i+1]
        if current!=next:
            elementCount.append(arr[i])
            elementCount.append(count)
        if current==next:
            count+=1
            continue
        count=1
    arr.pop()
    maxIndex=1
    checkValue='-1'
    for i in range(3,len(elementCount),2):
        if elementCount[i-2]<elementCount[i] and elementCount[i]!=checkValue:
            #print("found: ",elementCount[i-1],'with: ',elementCount[i])
            checkValue=elementCount[i]
            maxIndex=i
    #print(elementCount)
    return elementCount[maxIndex-1]
print(round(mean(n),1))
print(round(median(n),1))
print(mode(n))