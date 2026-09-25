from collections import deque

n = int(input("Enter n:"))
arr = list(map(int, input("Enter elements:").split()))
k = int(input())

mn = deque()
mx = deque()

left = 0
best_len = 0
best_start = 1

for right in range(n):
    while mn and arr[mn[-1]] >= arr[right]:
        mn.pop()
    mn.append(right)

    while mx and arr[mx[-1]] <= arr[right]:
        mx.pop()
    mx.append(right)

    while arr[mx[0]] - arr[mn[0]] > k:
        if mn[0] == left:
            mn.popleft()
        if mx[0] == left:
            mx.popleft()
        left += 1

    length = right - left + 1

    if length > best_len:
        best_len = length
        best_start = left + 1

print("Output:",best_len, best_start)