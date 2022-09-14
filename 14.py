a = int(input())
b = int(input())
c = int(input())
MaiorAB = (a+b+abs(a-b))/2
MaiorAB = (c+MaiorAB+abs(c-MaiorAB))/2
print (MaiorAB, "eh o maior")
