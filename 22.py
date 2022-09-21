N = float(input())
notas100 = N/100
resto100 = N%100
notas50 = resto100/50
resto50 = resto100%50
notas20 = resto50/20
resto20 = resto50%20
notas10 = resto20/10
resto10 = resto20%10
notas5 = resto10/5
resto5 = resto10%5
notas2 = resto5/2

moeda1 = resto5%2

print ("NOTAS:")
print ("%i nota(s) de R$ 100,00"%(notas100))
print ("%i nota(s) de R$ 50,00"%(notas50))
print ("%i nota(s) de R$ 20,00"%(notas20))
print ("%i nota(s) de R$ 10,00"%(notas10))
print ("%i nota(s) de R$ 5,00"%(notas5))
print ("%i nota(s) de R$ 2,00"%(notas2))
print ("MOEDAS:")
print ("%i moeda(s) de R$ 1,00"%(moeda1))
print (seqvalor[])
