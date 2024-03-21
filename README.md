# Documentação da API

## Introdução
Esta API requer Django e Django Rest Framework para execução do backend, e Vue.js para o frontend. A URL base da API é localhost, e os endpoints podem ser acessados adicionando "/api/v1/" à URL base.

#### TECNOLOGIAS USADAS:
- Bootstap:
- Git:
- Django:
- Dajngo Rest Framework:

#### ENDPOINTS CRIADOS 
- CUSTOMERS
  - api/v1/ customers/  (listar todos os clientes)
  - api/v1/ customers/create/ [name='customer-create']
  - api/v1/ customers/<int:pk>/ [name='customer-detail']
- PRODUCTS:
  - api/v1/ products/ [name='product-list']
  - api/v1/ products/create/ [name='product-create']
  - api/v1/ products/<int:pk>/ [name='product-details']
- PRODUCTS GROUP:
  - api/v1/ productgroups/ [name='customer-list']
  - api/v1/ productgroups/create/ [name='customer-create']
  - api/v1/ productgroups/<int:pk>/ [name='customer-detail']
- SELLER
  - api/v1/ sellers/ [name='seller-list']
  - api/v1/ sellers/create/ [name='seller-create']
  - api/v1/ sellers/<int:pk>/ [name='seller-list']
- SALES
  - api/v1/ sales/create/ [name='sales-create']
  - api/v1/ sales/<int:pk>/ [name='sales-details']
  - api/v1/ sales/?<str:seller>/<str:first_name>/<str:last_name> [name='sales-filtered-seller']
  - api/v1/ sales/?<str:customer>/<str:first_name>/<str:last_name> [name='sales-filtered-customer']
  - api/v1/ sales/?<str:start>/<str:end>/ [name='sales-filtered-startDate-endDate']

## Endpoints

### CUSTOMERS

### Endpoint: /api/v1/customers/ [name='customer-list']
#### Descrição
Este endpoint lista todos os clientes cadastrados no sistema.

#### Método
- GET

#### Parâmetros
Nenhum parâmetro é necessário para este endpoint.

#### Exemplo de solicitação

#### Resposta
- Código de status: 200 OK
- Corpo da resposta:
  ```json
  [
      {
          "customer_id":  "inteiro",
          "first_name": "String",
          "last_name": "String",
          "address": "String",
          "email": "String",
          "phone": "String",
          "occupation": "String",
          "date_of_birth": "YY-MM-DD",
          "created_at": timestamp
  
      },
      ...
  ]

### Endpoint: /api/v1/customers/create/ [name='customer-create']
#### Descrição
Este endpoint cria novos clientes.

#### Método
- POST

#### Parâmetros
Os parâmetros necessários para criar um novo cliente devem ser enviados no corpo da solicitação. Aqui estão os campos necessários:
- **first_name**: String - O primeiro nome do cliente.
- **last_name**: String - O sobrenome do cliente.
- **address**: String - O endereço do cliente.
- **email**: String - O endereço de e-mail do cliente.
- **phone**: String - O número de telefone do cliente.
- **occupation**: String - A ocupação do cliente.
- **date_of_birth**: YY-MM-DD - A data de nascimento do cliente.

#### Exemplo de solicitação
#### Resposta
- Código de status: 201 OK
- Corpo da resposta:
  ```json
  [
      {
          "first_name": "String",
          "last_name": "String",
          "address": "String",
          "email": "String",
          "phone": "String",
          "occupation": "String",
          "date_of_birth": "YY-MM-DD",  
      },
      ...
  ]

### Endpoint: /api/v1/customers/<int:pk>/ [name='customer-detail']
#### Descrição
Este endpoint busca um cliente pelo seu ID de cadastro.

#### Método
- GET

#### Parâmetros
- **pk**: Integer - O ID de cadastro do cliente.(1, 2, ...)

### PRODUCTS

### Endpoint: /api/v1/products/ [name='product-list']
#### Descrição
Este endpoint lista todos os produtos disponíveis.

#### Método
- GET

#### Parâmetros
Nenhum parâmetro é necessário para este endpoint.

#### Exemplo de solicitação


#### Resposta
- Código de status: 200 OK
- Corpo da resposta:
  ```json
  [
      {
          "id": 1,
          "name": "Produto 1",
          "description": "Descrição do Produto 1",
          "price": 99.99,
          "stock_quantity": 100
      },
      {
          "id": 2,
          "name": "Produto 2",
          "description": "Descrição do Produto 2",
          "price": 49.99,
          "stock_quantity": 50
      },
      ...
  ]
