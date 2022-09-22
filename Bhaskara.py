import math
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = (B**2)-4*A*C
if(A==0) or (delta<0):
    print ("Impossivel calcular")
    
else:
    root1 = (-B+math.sqrt(delta))/(2*A)
    root2 = (-B-math.sqrt(delta))/(2*A)
    print ("R1 = {:.5f}".format(root1))
    print ("R2 = {:.5f}".format(root2))
    
