import numpy as np
ar=[[12,34,45],[56,33,78],[76,34,23]]
a=np.array(ar)
#print(a)
for x in a:
    for  c in x:
        print(c,end="\t")
    print()
