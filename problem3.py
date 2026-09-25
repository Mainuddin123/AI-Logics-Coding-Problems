n = int(input("Enter n:"))
a = list(map(int, input("Enter elements:").split()))

m = int(input("Enter m value:"))
b = list(map(int, input("Enter elements:").split()))

left = 0
right = 0
carry = 0
ans = []

while left < n or right < m or carry:
    x = a[left] if left < n else 0
    y = b[right] if right < m else 0

    total = x + y + carry
    ans.append(total % 10)
    carry = total // 10

    left+=1
    right+=1

print("Output:", *ans)