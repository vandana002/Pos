mem=int(input('enter total memory available '))
blocksize=int(input('enter block size '))
processes=int(input('enter number of processes '))

req=[]
for i in range(processes):
    req.append(int(input('memory required by processes ')))

blocks=int(input("enter number of blocks available "))
int_frag=0
ext_frag=0
print("Process\tmem req\tmem alloc\tint_frag")
j=i=0
while(i<blocks):
    if(req[j]<=blocksize):
        int_frag+=(blocksize-req[j])
        print(i,"\t",req[j],"\tYes\t",blocksize-req[j])
        j+=1
        i+=1
    else:
        print(i,"\t",req[j],"\tNo\t----")
        j+=1

print("Total internal fragmentation is",int_frag)
print("total external fragmentation is",mem-(blocks*blocksize))
