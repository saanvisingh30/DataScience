import numpy as np
a=np.array([[12,34,45],[56,33,78],[76,34,23]])
#print(a)
for x in a:
    for  c in x:
        print(c,end="\t")
    print()