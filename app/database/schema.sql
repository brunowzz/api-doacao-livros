DROP TABLE IF EXISTS LIVROS;

CREATE TABLE LIVROS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    autor TEXT NOT NULL,
    imagem_url TEXT NOT NULL
);