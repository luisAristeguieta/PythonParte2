from transporte import resolverProblema
#cantidades de productos existentes en origenes
origenes1=[200,300,200] 
#cantidades de productos que se requieren en destinos
destinos1=[100,200,400] 

print("****PROBLEMA 1*****")
print(f"   ORIGENES: {origenes1}")
print(f"   DESTINOS: {destinos1}")
solucion1=resolverProblema(origenes1,destinos1)
