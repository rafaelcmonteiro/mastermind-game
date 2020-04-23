# API Flask - Mastermind

### Sobre a aplicação.
Esta aplicação web é uma versão simplificada do jogo Mastermind.

##### As regras do jogo são:
* O jogo gera um numero randomico de 4 digitos diferetes(no jogo original são 4 cores.)
* O usuário deve chutar o numero que foi gerado pela maquina. 
* Após o chute, o jogo retornará um numero composto por zeros e uns.
* Zero significa que o digito existe no número random, porém esta na posição errada.
* Um significa que o digito esta correto e na posição correta.

##### Exemplo:
    Número aleatório 1234\
    Número chutado 2314\
    Resultado 0001\
    O resultado é o numero chutado, porém com os acertos e os erros. 

### Configurando o Environment

##### Build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64


##### Use Mastermind installer
* Necessário instalar o pip na maquina.
* No projeto, procure por mastermind-installer.sh
* Copie o código e coloque em um arquivo .sh
* Feito isso de as devidas permissões usando o comando chmod -x nomedoarquivo.sh

##### MongoDB Script
    
    db version v4.2.5
    MongoDB shell version v4.2.5
    
    Abra o MongoDB shell através do comando "mongo" e insira os comandos a seguir: 
    
    use mastermindDB
    
    db.users.drop()
    
    db.createCollection("users")
    
    db.users.createIndex({user:1},{unique: true})

##### Flask-Mail

    Entre na pasta game.
    Altere o gmail e senha de acordo com os seus.
    
    Exemplo:
        exemplo@gmail.com
        senha
        
    Não pule linha.
