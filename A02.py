n,x = map(int,input().split())
nums = list(map(int,input().split()))
isFound = False
for num in nums:
  if x == num:
    isFound = True
    break

print("Yes" if isFound else "No")
