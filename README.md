# PersonalCheff
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="exemplo.webp" alt="exemplo imagem">
> Uma aplicação web de receitas chamada PersonalCheff desenvolvida durante o curso de Python no Senac Americana. A aplicação listará receitas e clicando em cada nome de receita você pode ver a receita completa.

### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
- [X] Criar e ativar o ambiente virtual
```
python -m venv .\venv\
venv\Scripts\activate
# se der erro no powershell utilize o comando abaixo para resolver a permissão
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- [X] Instalar o Django
```
python -m pip install django==3.2
```
- [X] Criar o projeto PersonalCheff
```
django-admin.py startproject PersonalCheffProject PersonalCheffProj
```
- [X] Subir o servidor e testar o projeto
```
entrar na pasta do projeto
cd PersonalCheffProj

executar o projeto no servidor
python manage.py runserver
```
- [X] Alterar o idioma do projeto para `pt-br`
    - Abrir o arquivo `settings.py` e na linha 106 trocar `en-us` para `pt-br`
- [X] Alterar o timezone do projeto para `America/Sao_Paulo`
- [X] Criar o app receitas
```
* preciso estar dentro da pasta do projeto (PersonalcheffProj)
python manage.py startapp receitas
```
- [X] Registrar o app receitas
```
no arquivo settings.py adicionar o app receitas na lista de apps 
INSTALLED_APPS[
    ...
    'receitas',
]
```
- [X] Configurar a rota inicial(index)
    - Dentro da pasta receita(app) criar o arquivo `urls.py`
    - no arquivo `urls.py` 
        ```python
            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.index, name='index')
            ]
        ```
- [X] Criar a view para a rota inicial
    - Dentro da pasta receitas(app) abrir o arquivo `views.py` 
    ```python
        from django.shortcuts import render
        from django.http import HttpResponse

        def index(request):
            return HttpResponse("<h1>Seja bem vindo</h1>")
    ```
- [X] Registrar a rota inicial
    - Dentro da pasta PersonalCheffProj(app) abrir o arquivo `urls.py`
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('receitas.urls')),
    ]
    ```
- [X] Criar o arquivo index.html
    - Dentro da pasta receitas(app), crie a pasta `templates`
    - Dentro da pasta `templates`crie seus arquivos HTML começando pelo `index.html`
    - No arquivo `views.py` que está dentro da pasta do app faça a seguinte alteração de código: 
    ```python
    from django.shortcuts import render

    def index(request):
        return render(request,'index.html')
    ```
- [X] Integrar arquivos estáticos (CSS, JS, IMG)
    - Dentro da pasta do projeto (PersonalCheffProj), criar a pasta `static`
    - Dentro da pasta `static`, colocar as imagens, os arquivos css e os arquivos js que for utilizar
    - No arquivo `settings.py`: 
        - realize a importação da biblioteca `os` através do comando `import os` 
        - na linha ~58 adicione o caminho dos templates da seguinte forma:
        ```python
        'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],
        ```
        - no final do arquivo, após a linha `STATIC_URL` insira o seguinte código:
        ```python
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'PersonalCheffProj/static')
        ]
        ```
        - `STATIC_URL`: é a configuração da rota através do qual os arquivos estáticos seram servidos
        - `STATIC_ROOT`: configuração da pasta de saída(destino) dos arquivos estáticos
        - `STATICFILES_DIRS`: cofiguração da(s) pasta de origem dos arquivos estáticos.
        - após realizar essas configurações execute, no terminal, o comando `python manage.py collectstatic`
        - na primeira linha do arquivo `index.html` insira `{% load static %}`. Esse comando deve ser usado em todos os arquivos em que você for utilizar arquivos estáticos.
        - insira uma imagem utilizando o comando `<img src="{% static 'logo.png' %}">`. Sempre que for utilizar um arquivo estático você deve utilizar `{% static 'nome-do-arquivo' %}`
- [X] Utilizando links
    - para criar um link para a página index, independente de onde você esteja utilize o comando `url`:
        ```python
        <a href="{% url 'index' %}">Página inicial</a>
        ```
- [X] Criando o base.html
    - na pasta `templates`crie o arquivo `base.html`. Esse arquivo contém todo o código de estrutura comum à todas as páginas. Nesse arquivo deve ficar tudo que tiver antes do `body` e tudo que tiver depois do `/body`.
    - nesse arquivo deve conter o `{% load static %}`
    - nesse arquivo, no local aonde será carregado o conteúdo das outras páginas, deve existir os delimitadores `{% block content %}` e `{% endblock %}`
    - o código do `base.html` será algo parecido com:
        ```python
        {% load static %}
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PersonalCheff</title>
            <link rel="stylesheet" href="{% static 'estilos.css' %}">
            <link rel="shortcut icon" href="{% static 'logo.png' %}" type="image/x-icon">
        </head>
        <body>
        {% block content %}
        
        {% endblock %}
        </body>
        </html>
        ```
- [X] Separando em partials
    - criar uma pasta chamada `partials` dentro da pasta `templates`
    - dentro da pasta `partials`crie os arquivos que serão as **partes globais** utilizadas no seu projeto como `header.html`, `footer.html`, `menu.html`, `side-bar.html`, `banner.html`, etc. No nosso exemplo criamos as partials `header.html` e `footer.html`
    - insira em cada um dos arquivos partials seus códigos correspondentes. Exemplo:  no arquivo `header.html` eu insiro todo o conteúdo que eu quero que seja apresentado no cabeçalho da minha aplicação. Não se esqueça do comando `{% load static %}`.
    - para incluir as partials nos arquivos de destino utilize o comando `include` da seguinte maneira: `{% include 'partials/header.html' %}`
- [ ] Renderizando dados dinamicamente
- [ ] Criando um dicionario com as receitas
- [ ] Criando o banco de dados(MySQL/MariaDB)
- [ ] Instalando o conector do bando de dados MySQL
- [ ] Criando o modelo da receita
- [ ] Criando a migration (mapeamento)
- [ ] Realizando a migration
- [ ] Registrando um modelo no admin
- [ ] Criando um usuário para o ambiente administrativo

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>