def fcfs(arr,head):
    previous=head
    num=0
    print("Seek sequence is")
    for i in range(len(arr)):

        if(arr[i]>previous):
            num+=arr[i]-previous
        else:
            num+=previous-arr[i]
        print(arr[i])
        previous=arr[i]
        
    return num
        
   
def scan(arr,head,dir):
    previous=head
    left=[]
    right=[]
    for i in range(len(arr)):
        if arr[i]>head:
            right.append(arr[i])
        elif arr[i]<head:
            left.append(arr[i])
    left.sort()
    right.sort()
    num=2
    sum=0
    while(num!=0):
        
        if dir=="left":
            for i in range(len(left)-1,-1,-1):
                print(left[i])
                
            dir="right"
            if num==2:
                sum+=previous-0
                previous=0
            else:
                sum+=previous-left[i]
            num-=1
            

        elif dir=="right":
            for i in range(len(right)):
                print(right[i])
                
            dir="left"
            if(num==2):
                sum+=199-previous
                previous=199
            else:
                sum+=right[i]-previous
            num-=1

    return sum

def cscan(arr,head,dir):
    previous=head
    left=[]
    right=[]
    for i in range(len(arr)):
        if arr[i]>head:
            right.append(arr[i])
        elif arr[i]<head:
            left.append(arr[i])
    left.sort()
    right.sort()
    num=2
    sum=0
    while(num!=0):
        
        if dir=="left":
            for i in range(len(left)-1,-1,-1):
                print(left[i])
                
            dir="right"
            if num==2:
                sum+=previous-0
                previous=199
                sum+=199
            else:
                sum+=left[len(left)-1]-previous
            num-=1
            

        elif dir=="right":
            for i in range(len(right)):
                print(right[i])
                
            dir="left"
            if(num==2):
                sum+=199-previous
                sum+=199
                previous=0
            else:
                sum+=previous-right[len(right)-1]
            num-=1

    return sum


arr=list(map(int,input().split()))
head=int(input("enter read/write head "))
choice=int(input("enter your choice :"))
if choice==1:
    print("total number of track movements is ",fcfs(arr,head))

elif choice==2:
    dir=input("direction")
    print("total number of track movements is ",scan(arr,head,dir))

elif choice==3:
    dir=input("direction ")
    print("total number of track movements is ",cscan(arr,head,dir))
