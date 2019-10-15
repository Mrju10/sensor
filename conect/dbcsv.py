import csv

reader = csv.reader(open('tabla.csv', 'rb'))
for row in (reader):
    row.split('...indica el delimitador...')
    Centenas,Decenas,Millar,Separador = row[0],row[1],row[2],row[3] 
# Aquí me sale duda si quieres contar la cantidad de 
# datos que tienes por columna o por 'celda' dentro del dato
# Para cantidad de datos por celda:
   # print len(Centenas), len(Decenas), len(Millar), len(Separador )
# Para la cantidad de datos por columna
#print len(reader[...numero de columna...])