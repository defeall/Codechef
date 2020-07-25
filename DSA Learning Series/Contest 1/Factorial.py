t = int(input())
for i in range(t):
    a = int(input())
    count = 0
    i = 5
    while(a/i>=1):
        count = count + a//i
        i = i*5
    print(count)
