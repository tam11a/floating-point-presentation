x = '1011001010'
y = 0
for i, j in enumerate(x):
    y += int(j) * (2**((i + 1) * -1))
print(y)