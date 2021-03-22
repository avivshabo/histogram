

import console
from prettytable import PrettyTable

#elements = console.get_int_array()
#elements = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maxElem = max(elements)
minElem = min(elements)
bucketsNum = console.get_int()
#bucketsNum = 3
rangeSize = maxElem - minElem + 1  #12
bucketSize =  rangeSize//bucketsNum #integer division   4

print(f"Max element:{maxElem}\nMin element:{minElem}\nrange size:{rangeSize}\nbucket size:{bucketSize}\n\n")
buckets = [0] * bucketsNum
bucketElements =  [""] * bucketsNum

histogramTable = PrettyTable(['Bucket', 'Count', 'Elements'])
for index in range(bucketsNum):
    bucketMin = minElem + bucketSize*index
    bucketMax = bucketMin + bucketSize - 1
    for element in elements:
        if bucketMin <= element <= bucketMax:
            buckets[index] += 1
            bucketElements[index] += f"{element},"
            
    histogramTable.add_row([index, buckets[index], bucketElements[index]])
print("Histogram Table:")
print(histogramTable)
