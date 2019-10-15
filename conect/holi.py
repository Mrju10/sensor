
import time
import serial
import json
import csv


vector=[]
i=0

valor = serial.Serial('COM16', 9600)
while i<10:
	vector.append(valor.readline())
	# time.sleep(1)
	i += 1
	pass

print(vector)		
headers = ('extra','millon','millar','centenas','decenas','unidad','separador')

with open('tabla.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(vector)




