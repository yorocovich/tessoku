d = int(input())  # Dの入力
n = int(input())  # Nの入力
b = [0] * d  # A相当のリスト

for i in range(n):
    l, r = map(int, input().split())
    l -= 1  # 0-indexed に変更
    r -= 1  # 0-indexed に変更
    b[l] += 1
    if r + 1 < d:
        b[r + 1] -= 1

for i in range(1, d):
    b[i] += b[i - 1]

for i in range(d):
    print(b[i])