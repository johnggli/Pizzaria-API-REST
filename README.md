# Pizzaria-API-REST
API para Pizzaria utilizando Django Rest Framework

## Requisitos
 - Django==2.2.5
 - djangorestframework==3.10.3


## Modelagem

```json
Address {
	street: "",
    suite: "",
    city: "",
    zipcod: ""
}

Client {
	name: "",
	email: "",
	phone: "",
	phone_two: "",
	address: Address()
}

Employee {
	name: "",
	cpf: "",
	salary: 0.0,
	commission: 0.0,
	manager: false
}

Pizza {
	name: "",
	description: "",
	price: 0.0,
	time: 0
}

Demand {
	date: 00-00-0000,
	client: Client(),
	employee: Employee(),
	pizza: [Pizza()] # list
}

```