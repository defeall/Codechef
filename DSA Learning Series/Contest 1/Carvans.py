T = int(input())
for i in range(T):
    N = int(input())
    max_speed = input().split(" ")
    a = 1
    if(N == 1):
        print(1)
        continue
    if(N == 0):
        print(0)
        continue
    for j in range(1,len(max_speed)):
        if(max_speed[j]<=max_speed[j-1]):
            a = a+1
        else:
            max_speed[j] = max_speed[j-1]
    print(a)
