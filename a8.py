import numpy as np

dt=np.dtype([('id',np.dtype(np.int8)),('name',np.dtype('S20')),('sal',np.dtype('i2'))])
ar=np.array([(101,'A',2000),(102,'B',3000),(103,'C',4000),(104,'D',7000),(105,'R',2000)],dtype=dt)
for row in ar:
    for col in row:
        print(col,end="\t")
    print()