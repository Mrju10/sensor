import pymysql
import csv
 
with open('tabla.csv.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
     for row in reader:
          print(row)

try:

	conexion = pymysql.connect(host='localhost',port=3306,user='root',password='',db='laravel')
	cursor= conexion.cursor() 

  

	cursor.execute("INSERT INTO books (Centenas,Decenas,Millar,Separador) VALUES(%s, %s, %s,%s)", ('60', '50','50','10'))
	conexion.commit()
	conexion.close()

		 
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

		# # Guardar cambios.
		#    with conexion.cursor() as cursor:
		#         sql = "INSERT INTO `persona` (`Centenas`, `Decenas`, `Millar`, `Separador`) VALUES(%s, %s, %s,, %s)"
		#         cursor.execute(sql, ("49", "50", "50","10"))
		    
