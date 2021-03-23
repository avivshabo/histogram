# histogram
A python script to print the histogram table of a given integer array


Sample:

    python histogram.py
    +-----------------------------+
    Total elements: 11
    Max element:37
    Min element:1
    Range size:37
    Bucket size:12
    +-----------------------------+



    Histogram Table:
    +--------+--------------+-------+--------------------+
    | Bucket | Bucket Range | Count |      Elements      |
    +--------+--------------+-------+--------------------+
    |   0    |    1..13     |   9   | 1,1,3,5,7,9,11,4,5 |
    |   1    |    13..25    |   1   |         22         |
    |   2    |    25..37    |   1   |         37         |
    +--------+--------------+-------+--------------------+
