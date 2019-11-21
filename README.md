# Pizzaria-API-REST
API para Pizzaria utilizando Django Rest Framework

## Requisitos
 - Django==2.2.5
 - djangorestframework==3.10.3

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

