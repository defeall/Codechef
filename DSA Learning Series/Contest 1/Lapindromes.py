T= int(input())
for i in range(T):
    a = list(input())
    x=1
    if(len(a)%2==0):
        b,c=a[:len(a)//2],a[len(a)//2:]
        d=list(set(b))
        for i in d:
            if b.count(i) == c.count(i):
                continue
            else:
                x=0
    else:
        b,c=a[:len(a)//2],a[(len(a)//2)+1:]
        d=list(set(b))
        for i in d:
            if b.count(i) == c.count(i):
                continue
            else:
                x=0
    if(x==0):
        print('NO')
    else:
        print('YES')
