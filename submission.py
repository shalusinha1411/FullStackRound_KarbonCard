# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import numpy as np
R = int(3)
C = int(3)

print("Enter the values of a 3x3 matrix")
entries = list(map(float, input().split()))
  
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print("The input dataset")
print(matrix)

for r in range(R):
    for c in range(C):
        if(matrix[r][c]== 0):
            matrix[r][c] = np.nan
    
col_mean = np.nanmean(matrix, axis = 0)
# printing column mean
#print ("column mean", str(col_mean))
  
# find indices where nan value is present
inds = np.where(np.isnan(matrix))
  
# replace inds with avg of column
matrix[inds] = np.take(col_mean, inds[1])
  
# printing final array
#print ("final array", matrix)

col_mean = np.nanmean(matrix, axis = 0)
  
# printing column mean
#print ("columns mean", str(col_mean))

y = np.std(matrix, axis=0)
#print("std deviation", y)
for r in range(R):
    for c in range(C):
        matrix[r][c] = (matrix[r][c]-col_mean[c])/y[c]
        
        
print("The solution dataset is: ")
print(matrix)

# Sample Testcase
## R = 3, C = 3
## 1 2 0 0 1 1 5 6 5


