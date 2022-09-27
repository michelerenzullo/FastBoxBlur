import numpy as np
import collections

#ksize = 7 r = 3
#input array 200 19 55 44 59 2 4 110 22 4 
#padded twice 4 2 59 | 44 55 19 | 200 19 55 44 59 2 4 110 22 4 | 22 110 4 | 2 59 44

# expected / correct outputs
# 1st pass 109 164 183 | 383 398 451 | 436 451 398 383 293 296 245 223 274 276 | 274 223 245 | 241 219 109
# 2nd pass 839 1237 1688 | 2124 2466 2700 | 2900 2810 2708 2502 2289 2112 1990 1881 1811 1760 | 1756 1752 1587 | 1311 1037 814

# output is 
# 1st pass 109 164 183 | 383 398 451 | 436 451 398 383 293 296 245 223 274 276 | 274 223 245 | 241 219 109
# 2nd pass 839 1237 1688 | 2124 2466 2700 | 2900 2810 2708 2502 2289 2112 1990 1881 1811 1760 | 1756 1752 1587 | 1311 1037 814

input_data=np.array([200,19,55,44,59,2,4,110,22,4])

b = 13 #kernel is odd

r = int(b/2)
print("kernel size:",b,"radius:",r)

x1 = np.array(input_data)
d = collections.deque(maxlen=b+1)

print(x1)

sum1=0
sum2=0

output1 = np.zeros(x1.size, dtype=int)
output2 = np.zeros(x1.size, dtype=int)
d.extend(np.zeros(b + 1, dtype=int))

print(b,x1.size)
for i in range(r):
    e = (((x1.size-1)- (b-i) % (x1.size)),(b-1-i))[(b-i) < (x1.size)]
    #print(e,b-i-1)
    sum1= sum1 + x1[e]

for i in range(r, b):
    e = (((x1.size-1)- (b-i) % (x1.size)),(b-1-i))[(b-i) < (x1.size)]
    #print(e,b-i-1)
    sum1= sum1 + x1[e]
    d.append(sum1)
    sum2 = sum2 - d[0] + d[b]

for i in range(1, x1.size ):
    e = (((x1.size-1)- abs(b-i) % (x1.size-1)),abs(b-i))[abs(b-i) < (x1.size)]
    sum1 = sum1 - x1[e] + x1[i]
    d.append(sum1)
    sum2 = sum2 - d[0] + d[b]
    if(i >= r):
        output1[i - r] = sum1
        if(i >= r*2):
            output2[i - r*2] = sum2
    
for i in range(x1.size , x1.size + r*2):
    e = (((x1.size-1)- abs(b-i) % (x1.size-1)),abs(b-i))[abs(b-i) < (x1.size)]
    #print(e,abs(b-i))
    sum1 = sum1 + x1[(x1.size-1-i) % (x1.size-1)] - x1[e]
    d.append(sum1)
    sum2 = sum2 - d[0] + d[b]
    if(i < x1.size + r):
        if(i - r >=0):
            print(i-r)
            output1[i - r] = sum1
    if (i - r*2 >=0):
        #print(i-r*2,sum2)
        output2[i - r*2] = sum2


print(output1,"\n",output2)
