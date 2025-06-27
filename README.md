# Formulário Vivo
O _Formulário Vivo_ disponibiliza uma API que permite acesso aos módulos do sistema.

Requerimentos necessários para a API funcionar:
* Flask
* flask-cors
* flask-mysqldb
* python-dotenv
* React
* HTML
* Json

# Métodos
Métodos que podem ser usados para a API:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |

# Rotas
Lista de rotas presentes na API:
* /cadastro
* /buscar/sip
* /buscar/ddr
* /buscar/lp
* /api/cadastro_usuario
* /api/login
* /atualizar/cadastro/<int:id>
* /cadastro/<int:id>



