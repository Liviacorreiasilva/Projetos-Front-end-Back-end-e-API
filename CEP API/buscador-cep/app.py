from flask import Flask, render_template, request  # Importa Flask, render_template e request
import requests  # Importa requests para fazer requisições HTTP

# Cria o objeto da aplicação Flask
app = Flask(__name__)

# Define a rota para a página inicial "/"
@app.route('/')
def home():
    # Retorna o arquivo HTML chamado index.html da pasta templates
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/buscar', methods=['POST'])
def buscar():
    cep = request.form['cep']  # Obtém o CEP enviado pelo formulário

    # URL da API para buscar informações do CEP
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # Faz a requisição para a API
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if resposta.status_code == 200:
        dados = resposta.json()  # Converte a resposta JSON em dicionário

        # Verifica se a resposta tem erro (CEP inválido)
        if 'erro' in dados:
            resultado = None  # Se o CEP não existir, resultado é None
        else:
            resultado = dados  # Se existir, guarda os dados do CEP
    else:
        resultado = None  # Se a requisição falhar, define resultado como None

    # Renderiza o template index.html com os dados do CEP (se houver)
    return render_template('index.html', resultado=resultado)

# Faz o servidor rodar só se esse arquivo for executado diretamente
if __name__ == '__main__':
    # Executa a aplicação Flask com modo de desenvolvimento ativado
    app.run(debug=True)

# O código acima cria uma aplicação Flask simples que renderiza um template HTML quando a rota raiz é acessada.
# O Flask é um microframework para Python que facilita a criação de aplicações web.
# O método render_template é usado para renderizar arquivos HTML que estão na pasta templates.
# Ele inicializa seu servidor, escuta requisições e manda as respostas certas para páginas HTML.
# O arquivo HTML index.html deve estar na pasta templates para que o Flask possa encontrá-lo.
# O modo debug=True permite que você veja erros diretamente no navegador
# e recarrega automaticamente a aplicação quando há mudanças no código.
