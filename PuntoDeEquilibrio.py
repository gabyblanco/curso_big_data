def calculaPuntoEquilibrio(coste_total_fijo, precio_unitario, coste_unitario_variable):
    return round(coste_total_fijo / (precio_unitario - coste_unitario_variable))
coste_total=10000
precio=250
coste_unitario=124
PuntoEquilibrio= calculaPuntoEquilibrio(coste_total, precio, coste_unitario)

print('Tienes que vender un total de ' + str(PuntoEquilibrio) + ' unidades')

