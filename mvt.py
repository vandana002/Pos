mem=int(input('enter total memory available'))
ch=i=1
alloc=0
pi=[]
while ch:
    pi.append(int(input('enter the memory for process')))
    alloc+=pi[i-1]
    if(alloc>mem):
        ch=0
        print('memory is full process',i,"cant be fit into memory")
        print('Total memory allocated is ',alloc-pi[i-1])
        print('External fragmentation is ',(mem-(alloc-pi[i-1])))
        for i in range(len(pi)-1):
            print(i+1,pi[i])
    i+=1
