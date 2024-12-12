import numpy as np  
x, y = np.ogrid[:3, :4]  
a=np.where(x > y, x, 10 + y)  
a  
