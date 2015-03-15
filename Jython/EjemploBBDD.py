# -*- coding: utf-8 -*-

from com.ziclix.python.sql import zxJDBC


direccion = "jdbc:oracle:thin:@172.30.160.190:1521/enlaces6"
user = "daw20"
password = "tiger"
version = "oracle.jdbc.driver.OracleDriver" 

def muestra_datos(linea):
    # Mostrar nombre, puesto de trabajo, d�a, mes, a�o
    formato = "%-20s %-10s    %02d/ %2d/ %4d"
    dia = linea[4].day
    mes = linea[4].month
    yr = linea[4].year
    
    print formato % (linea[1].title(), linea[2].title(), dia, mes, yr)

conexion = zxJDBC.connect(direccion, user, password, version)

cursor = conexion.cursor()
 
cursor.execute("select * from emp")

cabecera = "%-20s %-10s    %-5s\n" % ('Apellidos', 'Puesto', 'Fecha')
print cabecera

for linea in cursor.fetchall():
    muestra_datos(linea)
