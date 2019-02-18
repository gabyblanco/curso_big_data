#float=para que me de decimal
pp = "p"
while (pp != "f"):
    pp = input("Introduce el precio por acción en dólares:")
    if pp != "f":
        precio=float(pp)
        def puede_ser_listado_en_NYSE(precio):
            return precio>=4

        if puede_ser_listado_en_NYSE(precio):
            print("Si puede aparecer en la bolsa de NY")
        else:
            print("No puede aparecer en la bolsa de NY")
    
    
    
    
