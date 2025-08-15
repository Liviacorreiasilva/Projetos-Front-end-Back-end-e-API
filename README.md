Buscador de CEP com Python e Flask

>Um projeto web simples para buscar informações de endereços no Brasil a partir de um CEP, utilizando a API pública ViaCEP. Este projeto foi desenvolvido com Python, Flask, HTML e CSS, e é ideal para quem quer aprender a consumir APIs externas e criar aplicações web.

Funcionalidades:

>Consulta de CEP em tempo real via API ViaCEP.

>Retorno de informações detalhadas do endereço: logradouro, bairro, cidade e estado.

>Interface amigável construída com HTML e CSS.

>Validação simples e tratamento de erros para CEPs inválidos ou não encontrados.

Tecnologias utilizadas

>Python (nível intermediário)

>Flask (microframework web, nível intermediário)

>Requests (consumo de APIs, nível intermediário)

>HTML / CSS (front-end, nível intermediário)

>Jinja2 (templates dinâmicos no Flask)

O que é uma API?

>API significa Interface de Programação de Aplicações. É um conjunto de regras que permite que dois sistemas diferentes se comuniquem entre si.

Como acessar uma API?

>Uma API é acessada por meio de requisições HTTP, que contêm:

>URL: endereço da API

>Headers: informações sobre a requisição

>Body: dados enviados ou recebidos

>HTTP é o protocolo usado para transferir dados entre o cliente (navegador ou aplicação) e o servidor. Uma requisição HTTP é a mensagem que solicita dados ou serviços de um servidor.

Estrutura do projeto

>buscador-cep/
│
├─ templates/
│   └─ index.html       # Template HTML principal
│
├─ static/
│   └─ style.css        # Estilos CSS
│
├─ app.py               # Código principal em Python
├─ requirements.txt     # Dependências do projeto
└─ README.md            # Este arquivo

Como executar o projeto

Clone o repositório:

>git clone <URL_DO_SEU_REPOSITORIO>


Entre na pasta do projeto:

>cd buscador-cep


Crie e ative um ambiente virtual (recomendado):

>python -m venv .venv
>source .venv/bin/activate   # Linux/Mac
>.venv\Scripts\activate      # Windows


Instale as dependências:

>pip install -r requirements.txt


Execute a aplicação:

>python app.py


Acesse no navegador:

>http://127.0.0.1:5000/

Exemplo de uso

>Digite um CEP no campo de pesquisa (ex: 01001-000).

>Clique em Buscar.

>O sistema retornará as informações do endereço correspondentes ao CEP informado.

Aprendizado com o projeto

>Este projeto foi o meu primeiro passo no consumo de APIs com Python e Flask. Durante o desenvolvimento, aprendi:

>Como consumir APIs externas usando requests.

>Como criar rotas e templates dinâmicos com Flask.

>Como estruturar uma aplicação web simples com HTML e CSS.

>Como tratar erros de entrada do usuário de forma amigável.

Autor
Lívia Correia
>Bacharelado em Sistemas de Informação | Suporte em TI | Python | Flask | JavaScript | HTML/CSS
GitHub: https://github.com/Liviacorreiasilva/Projetos-Front-end-Back-end-e-API
