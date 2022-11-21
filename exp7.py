import numpy as np
row,col=list(map(int,input('Enterrowandcol').split()))
A=np.array(list(map(int,input('EntermatrixA').split())))
A.shape=(int(row),int(col))
print(A)

if(row==col):
    print(np.linalg.eig(A))
    print(np.linalg.eigvals(A))
else:
    print("Eigenvaluesarecalculatedonlyforsquarematrices")
