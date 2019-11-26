# Pizzaria-API-REST
API para Pizzaria utilizando Django Rest Framework

Pizzaria-API-REST tem por objetivo facilitar o cadastro de clientes e facilitar os controle dos pedido de pizzas realizados por parte dos clientes. Projeto desenvolvido como projeto de avaliação da disciplina de programação para a internet 2, ministrada por Ely da Silva Miranda.

## Alunos

<div style="display: flex; flex-direction: row; justify-content: space-evenly; flex-wrap: wrap;">

<div style="display: flex; flex-direction: column; align-items: center;">
<img width="200" style="border-radius: 50%;" src="https://avatars0.githubusercontent.com/u/43749971?s=460&v=4"/>
<h3><a href="https://github.com/JohnEmerson1406">John Emerson</a></h3>
</div>

<div style="display: flex; flex-direction: column; align-items: center;">
<img width="200" style="border-radius: 50%;" src="https://avatars3.githubusercontent.com/u/36716898?s=460&v=4"/>
<h3><a href="https://github.com/pedrohenriquedevbr">Pedro Henrique</a></h3>
</div>

</div>


## Requisitos
 - Django==2.2.5
 - djangorestframework==3.10.3
 - django-rest-swagger==2.2.0
 - django-crispy-forms==1.8.1
 - django-filter==2.2.0
 - djangorestframework-simplejwt==4.3.0


## Acompanhe a apresentação do desenvolvimento com o sistema em funcionamento no seu computador.

Antes de iniciar a instalação certifique-se que possui o python>=3.5 instalado no seu computador.

### Instalação
 - Faça o clone ou download do projeto no seu computador.
 - instale os requerimentos para rodar a aplicação com o comando: 		pip install requirements.txt
 - realize as migrações com o conando: python manage.py migrate
 - e finalmente coloque para rodas: python manage.py runserver


## Modelagem do projeto

```json
Address {
	"street": "",
    "suite": "",
    "city": "",
    "zipcode": ""
}

Client {
	"name": "",
	"email": "",
	"phone": "",
	"address": Address()
}

Manager {
	"name": "",
	"cpf": "",
	"salary": 0.0,
	"email": ""
}

Employee {
	"name": "",
	"cpf": "",
	"salary": 0.0,
	"manager": manager()
}

Progress {
	"name": ""
}

Pizza {
	"name": "",
	"description": "",
	"price": 0.0
}

Demand {
	"created": 00-00-0000,
	"client": Client(),
	"employee": Employee(),
	"pizza": Pizza(),
	"progress": Progress()
}

```


## Funcionalidades

1. Funcionário gerencia clientes
2. Gerente gerencia funcionários e clientes
3. Funcionário e gerente pode criar pedidos
4. Funcionário e gerente altera o andamento do pedido
5. Somente o gerente pode criar sabores de pizzas, porém todos podem ter acesso as pizzas cadastradas
6. geração de relatórios
	1. Funcionário pode verificar o ultimo pedido de um cliente
	2. Funcionário pode verificar todos os pedidos atendidos por ele
	3. Gerente pode ver qual é o cliente que faz mais pedidos
	4. Gerente pode verificar qual vendedor mais vende


## Conventional commits
- **chore**: 	add Oyster build script    	// Pequenas alterações que não são novas funcionalidades.
- **docs**: 	explain hat wobble          // Semelhante a uma wiki; documentações etc.
- **feat**: 	add beta sequence           // Criação de Nova funcionalidade;
- **fix**: 		remove error message        // Correção de bugs
- **refactor**: share logic 4d3d3d3     	// Refatoração de um código
- **style**: 	convert tabs to spaces     	// Alteração em estilos, formatação de código etc.
- **test**: 	ensure that increment       // Criação de testes da sua aplicação

> A mensagem do seu commit deve possuir até 7 palavras;
> A descrição deve estar em inglês, em prol de objetividade;
> O tempo verbal da mensagem deve estar no presente;
> A mensagem tem que ser objetiva e rígida;