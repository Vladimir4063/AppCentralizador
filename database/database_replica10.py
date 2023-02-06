import psycopg2

try:
    connection = psycopg2.connect(
        
    )
    print("Conexion exitosa!")

    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    result = cursor.fetchone()
    print(result)

    # cursor.execute("select * from resultado.resultado_stress_55205")
    # result_rows = cursor.fetchall()
    # for results in result_rows:
    #     print(results)

except Exception as ex:
    print("Uy:", ex)

finally:
    connection.close()
    print("Conexion finalizada!")