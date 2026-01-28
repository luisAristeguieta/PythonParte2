from transporte import resolverProblema
#cantidades de productos existentes en origenes
origenes1=[200,300,200,400] 
#cantidades de productos que se requieren en destinos
destinos1=[100,300,200,300,200] 

origenes2=[500,300,200,400,300] #1700
destinos2=[400,500,600,200] #1700

print("****PROBLEMA 1*****")
print(f"   ORIGENES: {origenes1}")
print(f"   DESTINOS: {destinos1}")
solucion1=resolverProblema(origenes1,destinos1)
print(f"SOLUCION: {solucion1}")
print("****PROBLEMA 2*****")
print(f"   ORIGENES: {origenes2}")
print(f"   DESTINOS: {destinos2}")
solucion2=resolverProblema(origenes2,destinos2)
print(f"SOLUCION: {solucion2}")

