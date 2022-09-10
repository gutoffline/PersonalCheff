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
- [ ] Integrar arquivos estáticos (CSS, JS)
- [ ] Utilizando links
- [ ] Criando o base.html
- [ ] Separando em partials
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