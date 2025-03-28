from flask import Blueprint, request, jsonify
from ..models.livro import Livro

livros_bp = Blueprint('livros', __name__)

@livros_bp.route('/')
def index():
    return jsonify({
        "mensagem": "Bem-vindo ao sistema de doação de livros! Compartilhe conhecimento, doe um livro!",
        "rotas_disponíveis": {
            "GET /": "Página inicial",
            "GET /livros": "Listar todos os livros cadastrados",
            "POST /doar": "Cadastrar um novo livro"
        }
    })

@livros_bp.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.get_all()
    return jsonify([livro.to_dict() for livro in livros])

@livros_bp.route('/doar', methods=['POST'])
def doar_livro():
    dados = request.get_json()
    
    campos_obrigatorios = ['titulo', 'categoria', 'autor', 'imagem_url']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"O campo '{campo}' é obrigatório"}), 400
    
    livro = Livro.create(
        titulo=dados['titulo'],
        categoria=dados['categoria'],
        autor=dados['autor'],
        imagem_url=dados['imagem_url']
    )
    
    return jsonify({
        "mensagem": "Livro cadastrado com sucesso",
        "livro": livro.to_dict()
    }), 201