#Desarrolle un programa en Python que resuelva ecuaciones de segundo grado. Estas ecuaciones
#tienen la siguiente forma:
#ax2 + bx +c = 0 con a ≠ 0

a= 2
b= -7
c= 3
raiz= (b**2)-(4*a*c)
x1=float(-b+(raiz**0.5))/(2*a)
x2=float(-b-(raiz**0.5))/(2*a)

print('Solucion:', "x1:", x1)
print('Solucion:', "x2:", x2)

a=1
b=-5
c=6
raiz= (b**2)-(4*a*c)
x1=float(-b+(raiz**0.5))/(2*a)
x2=float(-b-(raiz**0.5))/(2*a)

print('Solucion:', "x1:", x1)
print('Solucion:', "x2:", x2)

a=2
b=4
c=-6
raiz= (b**2)-(4*a*c)
x1=float(-b+(raiz**0.5))/(2*a)
x2=float(-b-(raiz**0.5))/(2*a)

print('Solucion:', "x1:", x1)
print('Solucion:', "x2:", x2)
