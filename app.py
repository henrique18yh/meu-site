from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando catálogo de camisetas
produtos = [
    {
        'id': 1,
        'nome': 'Camiseta Tradicional Branca',
        'descricao': 'Camiseta 100% algodão, confortável e durável.',
        'preco': 59.90,
        'cor': 'Branca',
        'marca': 'Brucele',
        'tamanho': ['P', 'M', 'G', 'GG'],
        'imagem': 'static\camisetabrucelee.webp'
    },
    {
        'id': 2,
        'nome': 'Camiseta Slim Fit Preta',
        'descricao': 'Modelo slim fit, tecido Dry Fit para melhor respirabilidade.',
        'preco': 79.90,
        'cor': 'Preta',
        'marca': 'Nike',
        'tamanho': ['P', 'M', 'G'],
        'imagem': 'static\camisetanike.webp'
    },
    {
        'id': 3,
        'nome': 'Camiseta Oversized Azul',
        'descricao': 'Estilo oversized, super confortável e moderna.',
        'preco': 69.90,
        'cor': 'Azul',
        'marca': 'Puma',
        'tamanho': ['M', 'G', 'GG'],
        'imagem': "static\camiseta.webp"
    },
]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/produto/<int:id>')
def produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return "Produto não encontrado", 404
    return render_template('produto.html', produto=produto)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    mensagem_enviada = False
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        mensagem = request.form.get('mensagem', '').strip()
        if nome and email and mensagem:
            # Aqui poderia salvar ou enviar a mensagem por email
            return redirect(url_for('contato', mensagem_enviada='1'))
    mensagem_enviada = request.args.get('mensagem_enviada') == '1'
    return render_template('contato.html', mensagem_enviada=mensagem_enviada)
app.run(debug=True,)    


