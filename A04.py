n = int(input())
ans = []
while n > 1:
  ans.append(n % 2)
  n //= 2

#最後に追加
ans.append(n)

ans = ans[::-1]
ans = ''.join(map(str, ans))

ans = f'{int(ans):010d}'
print(ans)