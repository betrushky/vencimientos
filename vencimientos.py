from datetime import datetime, timedelta

def hoy():
    fecha_actual = datetime.now()
    fe_str = datetime.strftime(fecha_actual,"%d-%m-%Y")
    fecha_actual= datetime.strptime(fe_str,"%d-%m-%Y")
    return fecha_actual

def calcular_fecha(hoy, prod, lot, fech):
    
    fecha_prod = datetime.strptime(fech,"%d-%m-%Y")
    vigente = (fecha_prod - hoy) / timedelta(days=1) # timedelta convierte la fecha en flotante para dias.
    if int(vigente)<= 30 and int(vigente)>0:
        print(f"El producto {prod} con lote: {lot} Está a {int(vigente)} dias de vencimiento")
    elif int(vigente)<= 0:
        print(f"El producto {prod} con lote: {lot} Está vencido y hay que retirarlo INMEDIATAMENTE")

calcular_fecha(hoy(),"Ordegan","CG316","16-12-2024")
