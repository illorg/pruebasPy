import random
import datetime
import sys
import mysql.connector
import numpy as np
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
    lanzamiento = np.array([[0, 0, 0], [0, 0, 0]], dtype='int8')
    comparar = 3

    while fatq > 1 and fdef > 0:  # Juega hasta que se acaben fichas
        if fatq > 3:  # defino cant dados de ataque
            cant_d_ataque = 3
        elif fatq == 3:
            cant_d_ataque = 2
        else:
            cant_d_ataque = 1

        if fdef >= 3:  # defino cant dados defen
            cant_d_defensa = 3
        else:
            cant_d_defensa = fdef

        lanzamiento = (tirar_dados(cant_d_ataque, cant_d_defensa))  # llama funcion tirar dados
        if cant_d_ataque <= cant_d_defensa:  # elige cuantos dados se comparan
            comparar = cant_d_ataque
        else:
            comparar = cant_d_defensa

        for comp in range(0, comparar):
            if int(lanzamiento[0][comp]) > int(lanzamiento[1][comp]):
                fdef -= 1
            else:
                fatq -= 1

    if fdef == 0:
        return True
    else:
        return False


def tirar_dados(cant_d_ataque, cant_d_defensa):

    dados_ataque = np.array([0, 0, 0], dtype='int8')
    dados_defensa = np.array([0, 0, 0], dtype='int8')
    for x in range(0, 3):
        if (x + 1) <= cant_d_ataque:
            dados_ataque[x] = random.randint(1, 6)
        if (x + 1) <= cant_d_defensa:
            dados_defensa[x] = random.randint(1, 6)
    dados_ataque = -np.sort(-dados_ataque)
    dados_defensa = -np.sort(-dados_defensa)
    return (dados_ataque, dados_defensa)


def run():
        
    # EJECUCION ######
    global fichas_ataque
    global fichas_defensa
    global simulaciones
    global vict_ataque
    global vict_defensa    
    if len(sys.argv) > 1:
        simulaciones = int(sys.argv[1])
        fichas_ataque = int(sys.argv[2])
        fichas_defensa = int(sys.argv[3])
    else:
        fichas_ataque = int(input('Ingrese fichas del atacante: '))
        fichas_defensa = int(input('ingrese fichas del defensor: '))

    proceso_porct = 0
    t = time()  # inicializo Timer
    for simulacion in range(simulaciones):  # Ciclo for de simulacciones : por defect 10K
        if jugar(fichas_ataque, fichas_defensa) is True:  # llama funcion jugar, envia cant fichas, devuelve ganador
            vict_ataque += 1
        else:
            vict_defensa += 1
        if simulacion/simulaciones*100 >= proceso_porct + 10:  # porcentaje de calculo simulaciones
            proceso_porct += 10
            print('Simulando: %' + str(proceso_porct))
    print('Simulando: %100. Tiempo consumido en el cálculo : {:.4f} s'.format(time() - t))
    porct_vict = str(round(vict_ataque/simulaciones*100, 2))
    porct_derrot = str(round(vict_defensa/simulaciones*100, 2))
    print(f'Simulaciones totales:  {simulaciones}')
    print(f'Victoria ataque: %{porct_vict}')
    print(f'Victoria defensa: %{porct_derrot}')

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
            mySql_insert_query = """INSERT INTO registro (fecha, simulaciones, fichas_ataque, fichas_defensa,
            porct_victoria_ataque, porct_victoria_defensa)
                            VALUES (%s, %s, %s, %s, %s, %s)"""
            recordTuple = (datetime.datetime.today(), simulaciones, fichas_ataque,
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
            print("la conexion MySql finalizo correctamente")


if __name__=='__main__':
    run()
    