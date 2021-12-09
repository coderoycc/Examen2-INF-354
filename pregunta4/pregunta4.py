import random

datos = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
pesos = [random.uniform(0,1),random.uniform(0,1), random.uniform(0,1)]
#ajuste aprendizaje
aprendiendo = True
salidaEntera = 0
iteracion = 0
tasaAprende = 0.3 

while(aprendiendo):
    iteracion = iteracion+1
    aprendiendo = False
    
    for cont in range(0,4):
        #Formula S  = f(E1*P1 + E2*P2 +1*P3) el 1 es por RETROALIMIENTACION 
        salidareal = (datos[cont][0]*pesos[0] + datos[cont][1]*pesos[1] + 1*pesos[2])
        if(salidareal>0):
            salidaEntera=1
        else:
            salidaEntera=0
        #erroo
        error_real=datos[cont][2]-salidareal
        error = datos[cont][2]-salidaEntera
        print("ERROR",error_real)
        if(error!=0):
            pesos[0]+=tasaAprende*error*datos[cont][0]
            pesos[1]+=tasaAprende*error*datos[cont][1]
            pesos[2]+=tasaAprende*error*1
            aprendiendo=True
            
    if not aprendiendo:
        break

for cont in range(0,4):
    real = datos[cont][0]*pesos[0]+datos[cont][1]*pesos[1]+pesos[2]
    resultado=0
    if real>0:
        resultado=1
    print("Entrada: ",datos[cont][0], " y ",datos[cont][1]," = ", datos[cont][2], "Res: ",resultado)