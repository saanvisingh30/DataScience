import numpy as np  
arr = np.array([0, 30, 60, 90, 120, 150, 180])  
print("\nThe sin value of the angles",end = " ")  
print(np.sin(arr * np.pi/180))  
print("\nThe cosine value of the angles",end = " ")  
print(np.cos(arr * np.pi/180))  
print("\nThe tangent value of the angles",end = " ")  
print(np.tan(arr * np.pi/180)) 