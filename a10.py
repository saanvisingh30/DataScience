import numpy as np

dt=np.dtype([('id',np.dtype(np.int8)),('name',np.dtype('S20')),('sal',np.dtype('i2'))])
ar=np.array([(101,'A',2000),(102,'B',3000),(103,'C',4000),(104,'D',7000),(105,'R',2000)],dtype=dt)

for row in ar:
   da=int(row["sal"]*40/100)
   hra=int(row["sal"]*8/100)
   pf=int(row["sal"]*4/100)
   gs=row["sal"]+da+hra-pf 
   it=int(gs*4/100)
   ns=gs-it
   print(row["id"],"\t",row["name"],"\t",row["sal"],"\t",da,"\t",hra,"\t",pf,"\t",gs,"\t",it,"\t",ns)