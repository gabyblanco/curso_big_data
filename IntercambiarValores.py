def intercambiar(a,b):
    return b, a
    aux = b
    b=a
    a=aux
    
x=5
y=2
x,y= intercambiar(x,y)
print (x, y)
