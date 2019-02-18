def berkus_eval(idea,prototipo,equipo,estrategia,ventas):
#el modelo de berkus agrega 0.5 de valor al argumento sobre los 20 millones, 
#es por eso que agregamos 0.5/20 millones si cada argumento es true
    plus=0.5
    valor=0
    if idea:
 #el += mantiene el valor del valor y le suma el plus
        valor += plus
    if prototipo:
        valor += plus
    if equipo:
        valor += plus
    if estrategia:
        valor += plus
    if ventas:
        valor += plus
    return valor 
    
#debemos agregar true or false porque puede que alguna opcion no cumpla  
    
print("El valor agregado a la empresa es de:", berkus_eval(True,True,True,False,False))

#lo que el resultado muestra es: de los 20 millones que esta valorada 
#calculamos que habra medio milon mas 
