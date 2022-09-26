N = int(input())
anos = N/365
meses = (N%365)/30
dias = (N%365)%30
print ("%i ano(s)"%(anos))
print ("%i mes(es)"%(meses))
print ("%i dia(s)"%(dias))
