import numpy as np

dt=np.dtype([('id',np.dtype(np.int8)),('name',np.dtype('S20')),('sal',np.dtype('i2'))])
ar=np.array([(101,'A',2000),(102,'B',3000),(103,'C',4000),(104,'D',7000),(105,'R',2000)],dtype=dt)
#print(ar)
#print(ar["id"])
#print(ar["name"])
#print(ar["sal"])
for row in ar:
    print(row["id"],"\t",row["name"],"\t",row["sal"])