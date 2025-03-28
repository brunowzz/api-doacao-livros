import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

def populate_db():
    with app.app_context():
        from app.database.db import get_db
        
        db = get_db()
        
        livros = [
            {
                "titulo": "Dom Quixote",
                "categoria": "Romance",
                "autor": "Miguel de Cervantes",
                "imagem_url": "https://example.com/dom-quixote.jpg"
            },
            {
                "titulo": "1984",
                "categoria": "Ficção Científica",
                "autor": "George Orwell",
                "imagem_url": "https://example.com/1984.jpg"
            },
            {
                "titulo": "O Pequeno Príncipe",
                "categoria": "Literatura Infantil",
                "autor": "Antoine de Saint-Exupéry",
                "imagem_url": "https://example.com/pequeno-principe.jpg"
            },
            {
                "titulo": "Cem Anos de Solidão",
                "categoria": "Realismo Mágico",
                "autor": "Gabriel García Márquez",
                "imagem_url": "https://example.com/cem-anos.jpg"
            }
        ]

        for livro in livros:
            db.execute(
                "INSERT INTO LIVROS (titulo, categoria, autor, imagem_url) VALUES (?, ?, ?, ?)",
                (livro["titulo"], livro["categoria"], livro["autor"], livro["imagem_url"])
            )
        
        db.commit()
        print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    populate_db()