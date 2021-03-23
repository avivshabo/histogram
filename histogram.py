

import console
from prettytable import PrettyTable

#elements = console.get_int_array()
elements = [1, 1, 3, 5, 7, 9, 22, 11, 4, 37, 5]

maxElem = max(elements)
minElem = min(elements)
#bucketsNum = console.get_int()
bucketsNum = 3
rangeSize = maxElem - minElem + 1  #12
bucketSize =  rangeSize//bucketsNum #integer division   4


print(f"+-----------------------------+")
print(f"Total elements: {len(elements)}\nMax element:{maxElem}\nMin element:{minElem}\nRange size:{rangeSize}\nBucket size:{bucketSize}")
print(f"+-----------------------------+")
print(f"\n\n")
buckets = [0] * bucketsNum
bucketElements =  [""] * bucketsNum

histogramTable = PrettyTable(['Bucket', 'Bucket Range', 'Count', 'Elements'])
for index in range(bucketsNum):
    bucketMin = minElem + bucketSize*index
    bucketMax = bucketMin + bucketSize
    for element in elements:
        if bucketMin <= element <= bucketMax:
            buckets[index] += 1
            bucketElements[index] = ",".join(filter(None,[bucketElements[index],str(element)]))
    histogramTable.add_row([index, f"{bucketMin}..{bucketMax}", buckets[index], bucketElements[index]])

print("Histogram Table:")
print(histogramTable)
