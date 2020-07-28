N = int(input())
list1 = []
for i in range(N):
    list1.append(int(input()))
list1.sort()
for i in range(N):
    list1[i] = list1[i]*(N-i)
print(max(list1))
