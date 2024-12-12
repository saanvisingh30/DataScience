import numpy as np

dt=np.dtype([('id',np.dtype(np.int8)),('name',np.dtype('S20')),('phy',np.dtype('i2')),('chm',np.dtype('i2')),('math',np.dtype('i2'))])
ar=np.array([(101,'A',60,70,80),(102,'B',30,40,50),(103,'C',40,60,70)],dtype=dt)

for row in ar:
    total=row["phy"]+row["chm"]+row["math"]
    per=int(total/3)
    print(row["id"],"\t",row["name"],"\t",row["phy"],"\t",row["chm"],"\t",row["math"],"\t",total,"\t",per)