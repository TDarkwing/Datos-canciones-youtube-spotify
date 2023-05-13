import psycopg2

try:
    connection=psycopg2.connect(
    host='Localhost',
    user='postgres',
    password='123',
    database='Music'
    )
    print("Conexion exitosa")
    cursor=connection.cursor()

    #Imprime Artista

    cursor.execute("select * from Artista")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)

    #Imprime pagina_spotify

    cursor.execute("select * from pagina_spotify")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)

    #Imprime canal_youtube

    cursor.execute("select * from canal_youtube")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)

    #Imprime album

    cursor.execute("select * from album")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)

    #Imprime cancion

    cursor.execute("select * from cancion")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print("\n")
    print("*"*300+"\n"+"*"*300)

    #Imprime estar_en_album

    cursor.execute("select * from estar_en_album")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)

    #Imprime publicar_cancion

    cursor.execute("select * from publicar_cancion")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)

    #Imprime datos_youtube

    cursor.execute("select * from datos_youtube")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print("\n")
    print("*"*300+"\n"+"*"*300)

    #Imprime datos_spotify

    cursor.execute("select * from datos_spotify")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("*"*300+"\n"+"*"*300)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")

