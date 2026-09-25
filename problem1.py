n = int(input("Enter n:"))
intervals = [list(map(int, input("Enter interval:").split())) for _ in range(n)]

intervals.sort()

start,end = intervals[0]
for s, e in intervals[1:]:
    if s <= end:
        end = max(end, e)
    else:
        print(start, end)
        start, end = s, e

print("Result:", start, end)