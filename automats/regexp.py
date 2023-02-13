from re import split

f= open('exploit.txt','r')
mensaje = f.read()


w = [[x for x in line.split() if len(x)>0] for line in mensaje.split('\n')]
#print(w)


#print(w[0:30])
#IE
print(w[26:27])
#CURP 
print(w[37:38])
#NUMERO DE ACTA 
print(w[53:54])
#Entidad de Registro 
print(w[57:58])
#FECHA DE REGISTRO
print(w[64:65])

#DATOS
#NOMBRE
print(w[101:104])
#E=CIVL
print(w[111:112])
#FECHA DE NACIMIENTO
print(w[112:113])

#LUGAR DE NACIMIENTO
print(w[122:123] + w[123:124])
#NACIONALIDAD
print(w[121:122])

print("*************DATOS DE DEFUNCION****************")
#FECHA DE DEFUNCION
print(w[157:158])
#HORA DE DEFUNCION
print(w[158:159])
#lUGAR DE DEFUNCION
print(w[159:160])
#DESTINO CADAVER
print(w[161:162])
#CAUSA DE LA DEFUNCION
print(w[170:181])
#link verifica
print(w[420:422])





