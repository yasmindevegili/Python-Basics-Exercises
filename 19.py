N = int(input())
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
resto2 = resto5%2
print (N,"\n%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00\n" %(notas100, notas50, notas20, notas10, notas5, notas2, resto2))

