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
arr=list(map(int,input().split()))
head=int(input("enter read/write head "))
print("total number of track movements is ",fcfs(arr,head))

