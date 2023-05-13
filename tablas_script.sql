
CREATE TABLE Artista (
	ID integer NOT NULL,
	Nombre varchar(70),
	PRIMARY KEY (ID)
);

CREATE TABLE Canal_youtube(
	Artista_id integer,
	Channel varchar(90),
	FOREIGN KEY(Artista_id) REFERENCES Artista
);


CREATE TABLE Pagina_spotify (
	Artista_id integer,
	Url_spotify varchar(200),
	FOREIGN KEY(Artista_id) REFERENCES Artista
);

CREATE TABLE Album (
	ID integer,
	Artista_id integer,
	Album varchar(220),
	Album_type varchar(20),
    PRIMARY KEY (ID),
	FOREIGN KEY(Artista_id) REFERENCES Artista
);

CREATE TABLE Cancion (
	ID integer,
	Track varchar(220),
	Danceability numeric(14,11),
	Energy numeric(8,4),
	Key numeric(8,4),
	Loudness numeric(9,4),
	Speechiness numeric(7,2),
	Acousticness numeric(14,10),
	Instrumentalness numeric(14,10),
	Liveness numeric(7,3),
	Valence numeric(7,3),
	Tempo numeric(10,3),
	Duration_ms numeric(10,2),
	PRIMARY KEY (ID)
);

CREATE TABLE Publicar_cancion (
	artista_id integer,
	cancion_id integer,
	FOREIGN KEY(Cancion_id) REFERENCES Cancion,
	FOREIGN KEY(artista_id) REFERENCES Artista 
);

CREATE TABLE Estar_en_album (
	Cancion_id integer,
	Album_id integer,
	FOREIGN KEY(Cancion_id) REFERENCES Cancion,
	FOREIGN KEY(Album_id) REFERENCES Album
);

CREATE TABLE Datos_spotify (
	Cancion_id integer,
	Url varchar(200),
	Stream numeric(14),
	FOREIGN KEY(Cancion_id) REFERENCES Cancion
);

CREATE TABLE Datos_youtube (
	Cancion_id integer,
	Title varchar(220),
	Url_youtube varchar(200),
	Views numeric(12,2),
	Likes numeric(12,2),
	Comments numeric(12,2),
	Lincesed varchar(12),
	Official_video varchar(12),
	Description varchar(30000),
	FOREIGN KEY(Cancion_id) REFERENCES Cancion
);