Acredito que existem 2 formas princípais de implementar o desafio.

##### 1. Usando um algoritmo de ordenação pronto, como a função sorted do Python

PROS:
``` 
- otimizado para o problema
- sem necessidade de serviços ou pacotes extras para o projeto
- alto desempenho
- custo menor de recursos da máquina
- arquitetura simples
```
    
CONTRAS:

Se o problema fosse mais simples, como ordenar apenas por um campo, seria simples de resolver com a função sorted.
Mas se tratando de receber vários parâmetros de ordenação, que podem ser crescente e decrescente, o código iria ficar complexo.
```
- alta complexidade
- tempo de desenvolvimento elevado
````


##### 2. Usando um serviço de ordenação pronto, como um banco de dados

PROS:
```
- já existem dezenas de soluções prontas para uso, necessita apenas de parâmetros de entrada
- tempo de desenvolvimento extremamente menor, comparado ao item 1
- menor complexidade
```

CONTRAS:
```
- menor desempenho
- arquitetura um pouco mais complexa
- custo maior de recursos da máquina
- necessidade de pacotes externos e um serviço de banco de dados
```


Decidi seguir usando o esquema do item 2.

Além do banco de dados, resolvi o framework Django + Django Rest. Eu poderia ir de Flask, mas teria
que desenvolver mais códigos. 

Django já vem com muitos módulos embutidos em tem um ORM poderoso, que atende
perfeitamente os requisitos do desafio. Usando Django, o banco de dados fica 
da escolha do usuário, no meu caso, escolhi sqlite3 devido a simplicidade
de configuração.
