# API Flask - Mastermind

### Sobre a aplicação.
Esta aplicação web é uma versão simplificada do jogo Mastermind. Esta aplicação conta com banco de dados para criação de perfis, a interação com o banco é bem simples já que ela só guarda dados do usuário como: nome completo, usuário, senha e histórico de melhor jogo.

##### As regras do jogo são:
* O jogo gera um numero randomico de 4 digitos diferetes(no jogo original são 4 cores.)
* O usuário deve chutar o numero que foi gerado pela maquina. 
* Após o chute, o jogo retornará um numero composto por zeros e uns.
* Zero significa que o digito existe no número random, porém esta na posição errada.
* Um significa que o digito esta correto e na posição correta.

##### Exemplo:
    Número aleatório 1234
    Número chutado 2314
    Resultado 0001
    O resultado é o numero chutado, porém com os acertos e os erros. 

### Configurando o Environment

##### Build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64


##### Use Mastermind installer
* Necessário instalar o pip na maquina.
* No projeto que esta no github, procure por mastermind-installer.sh
* Copie o código e coloque em um arquivo .sh
* Feito isso de as devidas permissões usando o comando chmod -x nomedoarquivo.sh
* Após a instalação é necessário alterar a porta onde será rodada a aplicação. 
* A aplicação esta configurada para rodar na porta 5001.
* A aplicatação será instalada na home do usuário.
* A partir desse ponto já é possível rodar o "app.py", lembre-se de dar um "source /venv/bin/activate" antes de rodar a aplicação.

##### MongoDB Script
    
    db version v4.2.5
    MongoDB shell version v4.2.5
    
    Não é necessário fazer o passo seguinte, criando o banco e a collection. O pymongo la na aplicação ficará responsável por criar o banco e a primeira collection assim que for preenchido o primeiro cadastro. 
    
    Abra o MongoDB shell através do comando "mongo" e insira os comandos a seguir: 
    
    use mastermindDB
    
    db.users.drop()
    
    db.createCollection("users")
    
    db.users.createIndex({user:1},{unique: true})
    
    Dentro da pasta DAO, tem o código de interação com o banco de dados, será necessário mudar a porta de entrada do banco
    para a porta que o seu mongoDB usa. Na aplicação esta configurada para mongodb://localhost:27017/

##### Flask-Mail

    Entre na pasta game.
    Altere o gmail e senha de acordo com os seus.
    
    Exemplo:
        exemplo@gmail.com
        senha
        
    Não pule linha.
