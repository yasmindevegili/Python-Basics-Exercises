A = float(input().replace(',', '.'))
B = float(input().replace(',', '.'))
C = float(input().replace(',', '.'))
pi = 3.14159

tri_retangulo = (A*C)/2
circulo = pi*(C**2)
trapezio = ((A+B)*C)/2
quadrado = B**2
retangulo = A*B

print ("TRIÂNGULO: {:.3f}".format(tri_retangulo))
print ("CIRCULO: {:.3f}".format(circulo))
print ("TRAPEZIO: {:.3f}".format(trapezio))
print ("QUADRADO: {:.3f}".format(quadrado))
print ("RETANGULO: {:.3f}".format(retangulo))
