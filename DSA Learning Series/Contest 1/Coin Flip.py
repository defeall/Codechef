T = int(input())
for i in range(T):
    G = int(input())
    for j in range(G):
        I, N, Q = input().split()
        if(int(N)%2==0):
            print(int(N)//2)
        else:
            if(I == '1' and Q=='1'):
                print(int(N)//2)
            elif(I == '1' and Q=='2'):
                print((int(N)//2)+1)
            elif(I == '2' and Q=='1'):
                print((int(N)//2)+1)
            elif(I == '2' and Q=='2'):
                print((int(N)//2))
