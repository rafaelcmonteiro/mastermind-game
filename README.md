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
