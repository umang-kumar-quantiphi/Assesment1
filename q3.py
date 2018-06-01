print("Enter the list as space separated numbers")
n=[int(x) for x in raw_input().split(" ")]
n.sort()
print("enter the number to be searched")
s=int(input())
high=len(n)-1
low=0
flag=0
while high>=low and flag==0:
    
    mid = (high+low)/2
    if n[mid]>s:
        high=mid-1
        
    elif n[mid]<s:
        low=mid+1
        
    else:
        print "The number is found at index", mid
        flag=1
        
    
if flag==0:print("The number is not found")
        


