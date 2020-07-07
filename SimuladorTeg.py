import random
import datetime
import sys
import mysql.connector
from mysql.connector import Error
from time import time

fichas_ataque = 0
fichas_defensa = 0
simulaciones = 10000
vict_ataque = 0
vict_defensa = 0


def jugar(fatq, fdef):

    cant_d_ataque = 0
    cant_d_defensa = 0
    lanzamiento = ()
    comparar = 3

    while fatq > 1 and fdef > 0: # Juega hasta que se acaben fichas
        if fatq > 3: cant_d_ataque = 3
        elif fatq == 3: cant_d_ataque = 2
        else: cant_d_ataque = 1

        if fdef >= 3: cant_d_defensa = 3
        elif fdef == 2: cant_d_defensa = 2
        else: cant_d_defensa = 1

        lanzamiento = (tirar_dados(cant_d_ataque, cant_d_defensa))  # llama tirar dados
        if cant_d_ataque <= cant_d_defensa:
            comparar = cant_d_ataque
        else: comparar = cant_d_defensa

        for comp in range(0, comparar):
            if int(lanzamiento[0][comp]) > int(lanzamiento[1][comp]):
                fdef -= 1
            else: fatq -= 1

    if fdef == 0: return "gana ataque"
    else: return "gana defensa "


def tirar_dados(cant_d_ataque, cant_d_defensa):
        
    
    dados_ataque = [0, 0, 0]
    dados_defensa = [0, 0, 0]
    for x in range(0, 3):
        if (x + 1) <= cant_d_ataque:
            dados_ataque[x] = random.randint(1, 6)
        if (x + 1) <= cant_d_defensa:
            dados_defensa[x] = random.randint(1, 6)
    dados_ataque.sort(reverse=True)
    dados_defensa.sort(reverse=True)
    return (dados_ataque, dados_defensa)


# EJECUCION ######
if len(sys.argv) > 1:
    simulaciones = int(sys.argv[1])

proceso_porct = 0
fichas_ataque = int(input('Ingrese fichas del atacante: '))
fichas_defensa = int(input('ingrese fichas del defensor: '))
t = time() # start time for the for loop
for simulacion in range(simulaciones):  ## Ciclo for de simulacciones : por defect 10mil
    if jugar(fichas_ataque, fichas_defensa) == "gana ataque": # llama funcion jugar, envia cant fichas, devuelve ganador
        vict_ataque += 1
    else:
        vict_defensa += 1
    if simulacion/simulaciones*100 >= proceso_porct + 10: # porcentaje de calculo simulaciones
        proceso_porct += 10
        print('Simulando: %' + str(proceso_porct))
print('Simulando: %100. Tiempo consumido en el cálculo : {:.4f} s'.format(time() - t))
porct_vict = str(round(vict_ataque/simulaciones*100, 2))
porct_derrot = str(round(vict_defensa/simulaciones*100, 2))
print('Simulaciones totales: ' + str(simulaciones))
print('Victoria ataque: %' + porct_vict)
print('Victoria defensa: %' + porct_derrot)

# conector SQL para guardar datos en mi server MySql
try:
    conexion = mysql.connector.connect(host='179.62.88.24',
                                         database='SimuladorTeg',
                                         user='adminer',
                                         password='Ledhouse130d')
    if conexion.is_connected():
        db_Info = conexion.get_server_info()
        print('')
        print("Conectado a illo MySql Version ", db_Info)
        cursor = conexion.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Esta conectado a la Base de datos: ", record)
        mySql_insert_query = """INSERT INTO registro (fecha, simulaciones, fichas_ataque, fichas_defensa, porct_victoria_ataque, porct_victoria_defensa) 
                           VALUES (%s, %s, %s, %s, %s, %s) """
        recordTuple = (datetime.datetime.today(), simulaciones, fichas_ataque, \
            fichas_defensa, porct_vict, porct_derrot)
        cursor.execute(mySql_insert_query, recordTuple)
        conexion.commit()
        print("registro almacenado exitosamente")

except Error as e:
    print("Error conectado a illo MySQL", e)
finally:

    if (conexion.is_connected()):
        cursor.close()
        conexion.close()
        print("la conexion MySql fue desactivada")
