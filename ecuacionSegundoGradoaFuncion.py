a= 2
b= -7
c= 3


def segundogrado(a,b,c):
    raiz= (b**2)-(4*a*c)
    x1= float(-b+(raiz**0.5))/(2*a)
    x2= float(-b-(raiz**0.5))/(2*a)
    #funcion round(valor que queremos redondear, decimales que queremos)
    return round(x1,2),round(x2,2)

x1, x2 = segundogrado(a,b,c)
print ("X=",x1, "X=",x2)

#otra manera de imprimir
print(segundogrado(a,b,c))
