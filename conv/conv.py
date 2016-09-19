from collections import Counter

data = []
with open('rosalind_conv.txt','r') as f:
    for line in f:
        data.append(line.strip())
S1 = [float(x) for x in data[0].split()]
S2 = [float(x) for x in data[1].split()]

#calculate Minkowski difference of S1 and S2
min_diff = []
for i in S1:
    for j in S2:
        diff = round(i - j, 5)
        min_diff.append(diff)

#find most common value and its frequency
x = Counter(min_diff).most_common(1)

print(x[0][1])
print(x[0][0])
