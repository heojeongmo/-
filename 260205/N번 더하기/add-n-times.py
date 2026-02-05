inp = input()
arr = inp.split()
a = int(arr[0])
n = int(arr[1])

# 출력
for _ in range(n):
    a += n
    print(a)