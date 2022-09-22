X = float(input())
if(0>X) or (X>100):
    print("Fora de intervalo")
elif(X>=0) and (X<=25):
    print("Intervalo [0,25]")
elif(X>25) and (X<=50):
    print("Intervalo (25,50]")
elif (X>50) and (X<=75):
    print("Intervalo (50,75]")
elif(X>75) and (X<=100):
    print("Intervalo (75,100]")
