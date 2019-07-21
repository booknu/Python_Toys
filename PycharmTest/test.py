a,b,c=map(int,input().split())
d=[[0]*(c+1) for i in range(b+1)]
d[1][1]=1
for i in range(a-1):
    t,d=d,[[0]*(c+1) for t in range(b+1)]
    for j in range(b+1):
        for k in range(c+1):
            d[j][k]+=t[j][k]*i
            if j<b:
                d[j+1][k]+=t[j][k]
            if k<c:
                d[j][k+1]+=t[j][k]
            d[j][k]%=1000000007
print(d[b][c])