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
>> Número aleatório 1234\
>> Número chutado 2314\
>> Resultado 0001\
>> O resultado é o numero chutado, porém com os acertos e os erros. 


Pip Freeze:

* bcrypt==3.1.7
* blinker==1.4
* certifi==2020.4.5.1
* cffi==1.14.0
* chardet==3.0.4
* click==7.1.1
* Flask==1.1.2
* Flask-Mail==0.9.1
* Flask-WTF==0.14.3
* idna==2.9
* itsdangerous==1.1.0
* Jinja2==2.11.2
* MarkupSafe==1.1.1
* pkg-resources==0.0.0
* pycparser==2.20
* pymongo==3.10.1
* requests==2.23.0
* six==1.14.0
* urllib3==1.25.9
* Werkzeug==1.0.1
* WTForms==2.2.1


##### MongoDB Script
>>
>>use mastermindDB
>>
>>db.users.drop()
>>
>>db.createCollection("users")
>>
>>db.users.createIndex({user:1},{unique: true})


