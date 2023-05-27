import plotly.express as px
from dash import Dash,html,dcc
import pandas as pd
import plotly.graph_objects as go
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
    #consulta 1
    #La consulta trata de comparar vistas y stream de 15 artistas
    cursor.execute("""
        select h.nombre as artista, sum (g.stream) as Stream_Spotify, sum(g.views) as Vistas_Youtube
        from (((Datos_Youtube as a inner join Cancion as b on a.Cancion_id = b.ID) as c inner join Datos_Spotify as d on c.ID = d.Cancion_id) as e inner join Publicar_Cancion as f on e.ID = f.Cancion_id) as g inner join Artista as h on g.Artista_id = h.ID
        where h.nombre = 'Gorillaz' or h.nombre = 'Snow Patrol' or h.nombre = '50 Cent' or h.nombre = 'Metallica' or h.nombre = 'Coldplay' or h.nombre = 'Grupo Laberinto' or h.nombre = 'Ennio Morricone' or h.nombre = 'Seu Jorge' or h.nombre = 'Leonard Cohen' or h.nombre = 'Good Charlotte' or h.nombre = 'Nirvana' or h.nombre = 'Maroon 5' or h.nombre = 'Romeo Santos' or h.nombre = 'Yandel' or h.nombre = 'Foo Fighters'
        group by h.nombre;
    """)
    app = Dash(__name__)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows,columns=['nombre','spotify','youtube'])
    #Tabla para youtube
    fig0 = px.bar(df, x = 'nombre', y = 'youtube', color_discrete_sequence= ["#c4302b"])
    #Tabla para spotify
    fig1= px.bar(df, x = 'nombre', y = 'spotify', color_discrete_sequence= ["#1ED761"])

    #Se fucionan las dos graficas para que se muestrean agrupadas
    diseño = go.Layout(title = 'Vistas youtube vs spotify')
    fig = go.Figure(data = fig0.data + fig1.data, layout=diseño)

    #Consulta 2
    #La consulta trata de comparar vistas y likes en youtube de 15 artistas
    cursor.execute("""
        select f.nombre as artista, sum(e.views) as Vistas, sum(e.likes) as Likes
        from ((Datos_Youtube as a inner join Cancion as b on a.Cancion_id = b.ID) as c inner join Publicar_Cancion as d on c.ID = d.Cancion_id) as e inner join Artista as f on e.Artista_id = f.ID
        where f.nombre = 'Gorillaz' or f.nombre = 'Snow Patrol' or f.nombre = '50 Cent' or f.nombre = 'Metallica' or f.nombre = 'Coldplay' or f.nombre = 'Grupo Laberinto' or f.nombre = 'Ennio Morricone' or f.nombre = 'Seu Jorge' or f.nombre = 'Leonard Cohen' or f.nombre = 'Good Charlotte' or f.nombre = 'Nirvana' or f.nombre = 'Maroon 5' or f.nombre = 'Romeo Santos' or f.nombre = 'Yandel' or f.nombre = 'Foo Fighters'
        group by f.nombre
    """)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows,columns=['nombre','spotify','youtube'])
    #Tabla para Likes
    fig0 = px.line(df, x = 'nombre', y = 'youtube', color_discrete_sequence= ["#0d0887"])
    #Tabla para vistas
    fig1= px.line(df, x = 'nombre', y = 'spotify', color_discrete_sequence= ["#fb9f3a"])

    #Se fucionan las dos graficas para que se muestrean agrupadas
    diseño = go.Layout(title = 'Vistas y likes youtube')
    fig2 = go.Figure(data = fig0.data + fig1.data, layout=diseño)

    #Consulta 3
    #La consulta trata de comparar vistas y likes de canciones en album y singles de 15 canciones
    cursor.execute("""
        select e.track, f.album, f.album_type, sum(e.views) as vistas, sum(e.likes) as likes
        from ((Datos_Youtube as a inner join Cancion as b on a.Cancion_id = b.ID) as c inner join Estar_en_album as d on c.ID = d.Cancion_id) as e inner join album as f on e.Album_id = f.ID
        where e.ID = 0 or e.ID = 1 or e.ID = 2 or e.ID = 3 or e.ID = 4 or e.ID = 5 or e.ID = 6 or e.ID = 7 or e.ID = 8 or e.ID = 9 or e.ID = 10 or e.ID = 11 or e.ID = 12 or e.ID = 13 or e.ID = 14
        group by e.track, f.album, f.album_type;
    """)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows,columns=['nombre','album','tipo','vistas', 'likes'])
    #Tabla para el tipo de likes
    fig3 = px.bar(df, x = 'nombre', y = 'likes', color = "tipo", barmode="group", title = 'Likes sencillo vs album')
    #Tabla para vistas
    fig4= px.bar(df, x = 'nombre', y = 'vistas', color = "tipo", barmode="group", title = 'Vistas sencillo vs album')

    #Consulta 4
    #La consulta trata de comparar vistas y stream de canciones en album y singles de 15 canciones
    cursor.execute("""
        select h.Album, g.track, h.album_type, sum(g.views) as vistas, sum(g.stream) as Stream
        from (((Datos_Youtube as a inner join Cancion as b on a.Cancion_id = b.ID) as c inner join Datos_Spotify as d on c.ID = d.Cancion_id) as e inner join Estar_en_Album as f on e.ID = f.Cancion_id) as g inner join Album as h on g.Album_id = h.id
        where h.ID = 0 or h.ID = 1 or h.ID = 2 or h.ID = 3 or h.ID = 4 or h.ID = 5 or h.ID = 6 or h.ID = 7 or h.ID = 8 or h.ID = 9 or h.ID = 10 or h.ID = 11 or h.ID = 12 or h.ID = 13 or h.ID = 14
        group by (h.Album, g.track, h.album_type);
    """)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows,columns=['nombre','album','tipo','vistas', 'likes'])
    #Tabla para el tipo de likes
    fig5 = px.bar(df, x = 'nombre', y = 'likes', color = "tipo", barmode="group", title = 'Likes sencillo vs album', color_discrete_sequence=['#2FBE83','#9C44C5'])
    #Tabla para vistas
    fig6= px.bar(df, x = 'nombre', y = 'vistas', color = "tipo", barmode="group", title = 'Vistas sencillo vs album', color_discrete_sequence=['#BFEC45','#EB8E4A'])



    app.layout = html.Div(style={'textAlign' : 'center','background-image':'url("https://img.freepik.com/foto-gratis/pergamino-pergamino-vintage-papel-blanco-blanco_53876-41732.jpg")',
                                 "padding": "2rem 1rem",
                                 'margin':'0'},
    children=[
    html.H1(children='Analisis de datos de musica en youtube y spotify'),
    #Grafico primera consulta
    dcc.Graph(
    id='example-gragh',
    figure = fig
    ),
    html.P("""Tenemos una barra roja que representa el número de vistas acumulado de un
        artista en YouTube, y una barra verde que representa el número de vistas acumuladas en Spotify.
        Podemos darnos cuenta de dos cosas y es, primero, la predilección por el pop ya que los artistas
        Coldplay y Maroon 5 tienen los picos más altos de vistas. A su vez podemos notar como las barras en
        Spotify son más altas, por lo cual podemos concluir que se acumulan más vistas en la plataforma de
        Spotify."""),
    #Grafico segunda consulta
    dcc.Graph(
    id='example-gragh',
    figure = fig2
    ),
    html.P("""Por su parte, tenemos la tabla de relación entre vistas y likes acumulados de un
    artista en YouTube, de forma lineal no damos cuenta de que algunos artistas tienen más aceptación
    por parte de su público, por ejemplo, el artista Coldplay a pesar de tener más vistas acumuladas que
    el artista Romeo Santos se ve como Coldplay no tiene tanta aceptación en comparación a Romeo
    Santos, concluyendo que tener un gran número de vistas no es sinónimo de aceptación.
    """),
    #Grafico tercera consulta
    dcc.Graph(
    id='example-gragh',
    figure = fig3
    ),
    dcc.Graph(
    id='example-gragh',
    figure = fig4
    ),
    html.P("""Podemos ver dos tablas, una que nos mide el número de vistas acumuladas en
    YouTube de una canción en particular y otra que nos mide el numero acumulado de likes de la
    misma en YouTube. A su vez podemos hacer dos diferenciaciones entre canciones publicadas en
    album y canciones publicadas como sencillo. Ahora bien, tanto en vistas como en likes parece haber
    un mayor acumulado en canciones publicadas en álbum, esto podría indicarnos que este tipo de
    canciones son más convenientes para publicar. No obstante, posteriormente veremos la tasa de
    aceptación del público en las canciones para corroborar que esta idea sea verídica."""),
    #Grafico cuarta consulta
    dcc.Graph(
    id='example-gragh',
    figure = fig5
    ),
    dcc.Graph(
    id='example-gragh',
    figure = fig6
    ),
    html.P("""Podemos ver dos tablas, en una se muestra el número acumulado de vistas en
    YouTube de una canción en particular, mientras que en otro su número acumulado de vistas en
    Spotify se hace la diferencia también entre canciones del tipo sencillo y canciones publicadas en
    álbum, en la gráfica se puede ver un mayor acumulado en canciones de tipo album y cabe resaltar
    que las vistas acumuladas en YouTube y Spotify suele variar bastante entre canciones, cosa que no
    pasaba cuando analizábamos a los artistas.
    """),
    #Contenedor que tiene las opiniones
    html.Div(style={'textAlign' : 'left','padding':'1em'},children=[
        html.H1(style={'textAlign' : 'center'},children=['Discucion']),
        html.H2('Opinio de Juan Diego'),
        html.P("""Para la primera consulta: Teniendo en cuenta que en Spotify se suele consumir música de forma
        más esporádica, podemos suponer que los oyentes recurrentes de Spotify no van a ser muy fieles a
        un artista en particular. Por lo tanto, suponemos que las vistas acumuladas van a ser mayores en
        YouTube que en Spotify."""),
        html.P("""Para la segunda consulta: Podemos suponer que la aceptación de una artista varia con respecto al
        género musical que se dedica a crear. Por ejemplo, suponemos que artistas que realizan canciones
        del género pop (Maroon 5, Coldplay) tendrían más likes en proporción con las vistas que canciones
        de genero metal (Metallica, Foo fighters). Por lo tanto, creemos que la proporción entre likes y vistas
        será mayor o menor dependiendo del género al que se dedique el artista.
        """),
        html.P("""Para la tercera consulta: Dado a que en YouTube a parte de la canción se vende también un video
        musical y que las canciones publicadas como sencillo suelen tener más probabilidad de ser
        publicadas con videoclip, se esperaría que las canciones de tipo sencillo tengan mayor aceptación
        (proporción vistas-likes) que las canciones publicadas en álbum."""),
        html.P("""Para la cuarta consulta: Como se dijo anteriormente, en Spotify se suele consumir música de forma
        más esporádica, esto implica que el oyente promedio de Spotify podría consumir más canciones
        lanzadas en forma de sencillo porque estas no necesitan de contexto o apoyarse de otras canciones
        para garantizar la transmisión de su mensaje. Como tal esta hipótesis defiende que en total las vistas
        de canciones lanzadas en álbum son mayores en YouTube, mientras que las vistas de las lanzadas
        como sencillo son mayores en Spotify."""),
        #Opinion de Juan Jose
        html.H2('Opinio de Juan Jose'),
        html.P("""Para la primera consulta: Como se puede ver los diagramas de barras, hay una preferencia a spototify.
              Posiblemente se deba a que spotify esta mas especializado en la musica y tiene una calidad mayor de audio.
               Por el contrario, el contenido principal de youtube son videos de diferentes tematicas, y no tanto en la musica """),
        html.P("""Para la segunda consulta: Como se ve en la grafica, la diferencia entre vistas y likes es abismal.
                Esto indica que los likes no representan realmete la opinion de la totolidad de la poblicion, en este caso"""),
        html.P("""Para la tercera consulta: Aqui hay una preferencia por los albumnes, tanto en likes como en vistas.
        Esto se podria deber a que muchas canciones famosas pueden estar dentro de un mismo abum, ademas de tener posibles colaboraciones
        con otros artistas"""),
        html.P("""Para la cuarta consulta: Para este caso se repite el mismo escenario de la consulta anterior, apesar de cambiar de plataforma
        . Cabe resaltar que se ve una caida de vistas y likes comparada con la anterior""")
    ])
    ]
    )



    if __name__ == '__main__':
        app.run_server(debug = True)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")