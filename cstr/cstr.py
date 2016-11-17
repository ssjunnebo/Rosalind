data = []
with open('rosalind_cstr.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

base = data[0]
for i in range(len(base)):
    cnt_0 = 0
    cnt_1 = 0
    row = ''
    for seq in data:
        if base[i] == seq[i]:
            row += '1'
            cnt_1 += 1
        else:
            row += '0'
            cnt_0 += 1
    if cnt_1>1 and cnt_0>1:
        print(row)
