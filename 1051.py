a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = 1,2,3,4,5
ab = []
for i, j in zip(a,b):
    ab.append(i != j)

print(ab)

print(sum(ab))

# return sum(i != j for i, j in zip(a, b))

