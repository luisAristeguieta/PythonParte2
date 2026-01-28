from transporte import validarListas
#cantidades de productos existentes en origenes
origenes1=[200,300,200,400] 
#cantidades de productos que se requieren en destinos
destinos1=[100,300,200,300,200] 
#cantidades de productos que se requieren en destinos
destinos2=[100,300,200,300,300] 


resultado1=validarListas(origenes1,destinos1)
print(f" RESULTADO 1: {resultado1}")

resultado2=validarListas(origenes1,destinos2)
print(f"  RESULTADO 2: {resultado2}")