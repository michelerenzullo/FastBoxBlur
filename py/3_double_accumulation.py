import numpy as np
import collections

# ksize = 7 r = 3
# input array 200 19 55 44 59 2 4 110 22 4
# padded twice 4 2 59 | 44 55 19 | 200 19 55 44 59 2 4 110 22 4 | 22 110 4 | 2 59 44

# expected / correct outputs
# 1st pass 109 164 183 | 383 398 451 | 436 451 398 383 293 296 245 223 274 276 | 274 223 245 | 241 219 109
# 2nd pass 839 1237 1688 | 2124 2466 2700 | 2900 2810 2708 2502 2289 2112 1990 1881 1811 1760 | 1756 1752 1587 | 1311 1037 814

# output is
# 1st pass 109 164 183 | 383 398 451 | 436 451 398 383 293 296 245 223 274 276 | 274 223 245 | 241 219 109
# 2nd pass 839 1237 1688 | 2124 2466 2700 | 2900 2810 2708 2502 2289 2112 1990 1881 1811 1760 | 1756 1752 1587 | 1311 1037 814

input_data = np.array([200, 19, 55, 44, 59, 2, 4, 110, 22, 4])

ksize = 57  # kernel is odd

radius = int(ksize/2)
print("kernel size:", ksize, "radius:", radius)

x1 = np.array(input_data)
d = collections.deque(maxlen=ksize+1)

print(x1)

sum1 = 0
sum2 = 0

output1_debug = np.zeros(x1.size + radius*4, dtype=int)
output2_debug = np.zeros(x1.size + radius*4, dtype=int)
output1 = np.zeros(x1.size, dtype=int)
output2 = np.zeros(x1.size, dtype=int)
d.extend(np.zeros(ksize + 1, dtype=int))

lut = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1])
for i in range(radius):
    sum1 = sum1 + x1[lut[(ksize-i-1) % lut.size]]

for i in range(radius, ksize):
    sum1 = sum1 + x1[lut[(ksize-i-1) % lut.size]]
    output1_debug[i - radius] = sum1
    d.append(sum1)
    sum2 = sum2 - d[0] + d[ksize]
    if (i >= radius*2):
        output2_debug[i - radius*2] = sum2


for i in range(1, x1.size + radius * 2):
    sum1 = sum1 + x1[lut[i % lut.size]] - x1[lut[(ksize-i) % lut.size]]
    d.append(sum1)
    sum2 = sum2 - d[0] + d[ksize]
    output1_debug[i + radius] = sum1
    output2_debug[i] = sum2
    if (i - radius >= 0):
        if (i - radius < x1.size):
            output1[i - radius] = sum1
        if (i - radius*2 >= 0):
            output2[i - radius*2] = sum2

for i in range(x1.size + radius * 2, x1.size + radius*3):
    sum1 = sum1 - x1[lut[(ksize-i) % lut.size]]
    d.append(sum1)
    sum2 = sum2 - d[0] + d[ksize]
    output1_debug[i + radius] = sum1
    output2_debug[i] = sum2

j = 1
for i in range(x1.size + radius*3, x1.size + radius*4):
    sum2 = sum2 - d[j]
    output2_debug[i] = sum2
    j += 1

print(output1, "\n", output2)
print(" ")
print(output1_debug, "\n", output2_debug)
