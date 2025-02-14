﻿# Desafio_sefaz_maceioin

Dev. Fullstack Jr
Secretaria Municipal de Fazenda de Maceió

# Nome do Projeto

Maceio IN

## Desafio

Gilberto precisa de um site simples chamado "Maceió IN". Este site deve ter uma apresentação agradável e minimalista, com controle de usuário através de login. A página inicial (Landing Page) apresentará uma breve descrição da Secretaria de Fazenda de Maceió e suas atividades.
Além disso, a página deverá conter uma lista contendo o cadastro de pessoas da secretaria com informações básicas como: nome, setor e e-mail. Será possível adicionar, alterar e excluir esses dados, que serão exibidos em uma tabela abaixo. Os setores disponíveis são: Contabilidade, Financeiro, Atendimento, Orçamento e TI.
As paletas de cores devem seguir o exemplo em maceio.al.gov.br assim como marca e ambientação.
Deve-se evitar o uso de IA para funcionalidades importantes do sistema, lembre-se que o objetivo é testar o seu conhecimento em programação e design, boa sorte!


## Tecnologias Usadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- **[Python 12](https://www.python.org/)**: Linguagem de programação usada no backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Framework web em Python que facilita o desenvolvimento rápido e seguro de aplicações web.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML/HTML5)**: Estrutura da interface do usuário.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Estilização da interface do usuário.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: Framework CSS para design responsivo e componentes de UI
- **[SQLite](https://www.sqlite.org/)**: Banco de dados utilizado para testes.
- **[Git](https://git-scm.com/)**:  Controle de versão para gerenciamento do código-fonte.


## Para rodar o projeto



1. Clone o Repositorio:
    ```bash
    git clone https://github.com/kemuelkesley/sefaz-maceioin.git
    ```

2. Navegue até o diretorio do Projeto:
    ```bash
    cd sefaz-maceioin
    ```

3. Crie um Ambiente Virtual:
    ```bash   
    python -m venv venv

    Ativar ambiente virtual
    
    # On Linux use `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
    ```

4. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

 # Observação o projeto já está com o banco e já tem um usuario e senha criados, caso queira criar seu próprio usuario e senha siga os passo logo abaixo.

   ```bash
    Usuario: admin
    Senha: bandal
   ```    

6. Aplicar as migrações do banco de dados -  nesse projeto o banco já está aqui:
    ```bash

    Caso precise Criar as tabelas ou fazer migrações do banco use esse comando
    1 - python manage.py migrate  
    ```

7. Criar acesso para Area administrativa:
    ```bash
    1 - Execute o comando: python manage.py createsuperuser  
    2 - Crie um nome de usuário - o usuario que você criar aqui será o seu usuario para logar no sistema 
    3 - Opcionalmente, informe um e-mail  
    4 - Defina uma senha  - A senha criada será a que você vai usar para logar no sistema
    5 - Confirme a senha no final  
    6 - Para acessar a área administrativa, vá até: http://127.0.0.1:8000/admin/  
    7 - Insira o nome de usuário e a senha criados.  
    ```

8. Fazer o projeto rodar:
    ```bash
    python manage.py runserver

    Endereço:

    http://127.0.0.1:8000/
    ```

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões, encontrar problemas ou quiser enviar um pull request, sinta-se à vontade para colaborar.

## License

This project is licensed under [kemSoftware].
