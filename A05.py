n, k = map(int,input().split())
patterns = 0
for i in range(1,n+1):
  for j in range(1,n+1):
    if 0 < k - (i + j) <= n:
      patterns += 1
      
print(patterns)