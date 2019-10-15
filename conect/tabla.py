import csv

tabla = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [7,8,9],
         [7,8,9],
         [7,8,9]

         ]
headers = ('Imagen', 'temperatura', 'Nivel')

with open('tabla.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(tabla)