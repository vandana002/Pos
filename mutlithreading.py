n=int(input("enter the no.of processes:"))
p=list(map(str,input("enter the processes:").split()))
bt=list(map(int,input("enter the burst time:").split()))
pri=list(map(int,input("enter the priority:").split()))
qno=list(map(int,input("enter queue no:").split()))
hold=[]
ct=[0]*n
tat=[0]*n
wt=[0]*n
val=0
gt=[]
for i in range(n):
    x=pri.index(min(pri))
    if(qno[x]!=min(qno)):
        hold.append(x)
    else:
        gt.append(p[x])
        ct[x]=bt[x]+val
        tat[x]=ct[x]
        wt[x]=tat[x]-bt[x]
        val+=bt[x]

    pri[x]=99999
for i in hold:
    gt.append(p[i])
    ct[i]=bt[i]+val
    tat[i]=ct[i]
    wt[i]=tat[i]-bt[i]
    val+=bt[i]



print("completion time ",ct)
print("turn around time ",tat)
print("waiting time ",wt)

print("gant chart ",gt)
print("avg tat ",round(sum(tat)/n,3))
print("avg bt ",(round(sum(bt)/n,3))) #optional
print("avg wt ",round(sum(wt)/n,3))
