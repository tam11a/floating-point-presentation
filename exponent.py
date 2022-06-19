# calculate Exponent
x = '10011'
y = 0
for i, j in enumerate(reversed(x)):
    y += int(j) * (2**i)
print(y)