# Pizzaria-API-REST
API para Pizzaria utilizando Django Rest Framework

## Requisitos
 - Django==2.2.5
 - djangorestframework==3.10.3


## Modelagem

```Javascript
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

Employee {
	"name": "",
	"cpf": "",
	"salary": 0.0,
	"manager": manager()
}

Manager {
	"name": "",
	"cpf": "",
	"salary": 0.0,
	"email": ""
}

Pizza {
	"name": "",
	"description": "",
	"price": 0.0
}

Demand {
	"date": 00-00-0000,
	"client": Client(),
	"employee": Employee(),
	"pizza": Pizza(),
	"progress": Progress()
}

Progress {
	"name": ""
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

