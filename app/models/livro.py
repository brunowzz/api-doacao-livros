from ..database.db import get_db

class Livro:
    def __init__(self, id=None, titulo=None, categoria=None, autor=None, imagem_url=None):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.imagem_url = imagem_url
    
    @staticmethod
    def from_row(row):
        return Livro(
            id=row['id'],
            titulo=row['titulo'],
            categoria=row['categoria'],
            autor=row['autor'],
            imagem_url=row['imagem_url']
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'categoria': self.categoria,
            'autor': self.autor,
            'imagem_url': self.imagem_url
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        livros = db.execute('SELECT * FROM LIVROS').fetchall()
        return [Livro.from_row(livro) for livro in livros]
    
    @staticmethod
    def create(titulo, categoria, autor, imagem_url):
        db = get_db()
        cursor = db.execute(
            'INSERT INTO LIVROS (titulo, categoria, autor, imagem_url) VALUES (?, ?, ?, ?)',
            (titulo, categoria, autor, imagem_url)
        )
        db.commit()
        
        return Livro(
            id=cursor.lastrowid,
            titulo=titulo,
            categoria=categoria,
            autor=autor,
            imagem_url=imagem_url
        )