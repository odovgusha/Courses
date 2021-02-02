import numpy as np

C = np.matrix('5 5; -1 7')
print(C)
print(np.linalg.inv(C))
print(C.T)

####want C=UEV.T
#CC.T=VE.T
#C@C.T = VE.TEV.T
#CV = UE

CCT =  C.T @ C
print(CCT)
print(np.linalg.det(CCT))
