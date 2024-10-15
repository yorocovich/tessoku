n, q = map(int,input().split())
guests = list(map(int,input().split()))
sum_guests = 0
cumulative_guests = []
for guest in guests:
  sum_guests += guest
  cumulative_guests.append(sum_guests)

for _ in range(q):
  l,r = map(int,input().split())
  ans = cumulative_guests[r-1]-(cumulative_guests[l-2] if l-2 >= 0 else 0)
  print(ans)