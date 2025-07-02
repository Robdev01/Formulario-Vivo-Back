# Formulário Vivo
O _Formulário Vivo_ disponibiliza uma API que permite acesso aos módulos do sistema.

# Funcionalidades
* Cadastro de equipamentos
* Remoção de equipamentos
* Alteração de equipamentos
* Busca de equipamentos
* Cadastro de usuários

Dependências necessárias para fazer a API funcionar:
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
# /cadastro
Rota usada para cadastrar informações do equipamento como sip, ddr e lp (disponível apenas para administradores)
# /buscar/sip
Rota usada para procurar por um valor de sip específico
# /buscar/ddr
Rota usada para procurar por um valor de ddr específico
# /buscar/lp
Rota usada para procurar por um valor de lp específico
# /api/cadastro_usuario
Rota usada para cadastrar usuários que utilizarão a API, podendo conceder permissão de administrador ou técnico para eles (disponível apenas para administradores)
# /api/login
Rota usada para acessar a API, necessário ter um login para utilizar os recursos dela
# /atualizar/cadastro/<int:id>
Rota usada para alterar os dados de um equipamento selecionado como sip, ddr ou lp (disponível apenas para administradores)
# /cadastro/<int:id>
Rota usada para deletar um equipamento selecionado do banco de dados (disponível apenas para administradores)

# Controller
Essa lista contém todas as definições usadas dentro do Controller e como elas interagem para fazer a API funcionar:

def atualizar_cliente(id, data):

Essa definição conecta com o banco de dados e localiza o equipamento através de seu id, você pode alterar as informações nos campos desse equipamento como desejar, pode até deixar eles em branco se prefirir. Caso ocorra algum erro você verá a mensagem "Erro ao atualizar cliente".
________________________________________________________________________________________________________

def deletar_cliente(id):

Essa definição conecta com o banco de dados e localiza o equipamento através de seu id, você pode usar essa definição para excluir o registro do equipamento do banco de dados, cuidado pois uma vez feito o registro não pode ser recuperado. Caso ocorra algum erro você verá a mensagem "Erro ao deletar cliente".
_________________________________________________________________________________________________________

def buscar_por_sip(sip):

Essa definição conecta com o banco de dados e localiza qualquer caractere existente em sip digitado no balão de busca para mostra-lo na área de resultado, permitindo uma busca que pode ser precisa caso digite um valor sip completo presente ou ampla se digitar apenas um ou mais caracteres. Caso não tenha nenhum caractere existente como valor sip você verá a mensagem "Erro em buscar_por_sip".
__________________________________________________________________________________________________________

def buscar_por_ddr(ddr):

Essa definição conecta com o banco de dados e localiza qualquer caractere existente em ddr digitado no balão de busca para mostra-lo na área de resultado, permitindo uma busca que pode ser precisa caso digite um valor ddr completo presente ou ampla se digitar apenas um ou mais caracteres. Caso não tenha nenhum caractere existente como valor ddr você verá a mensagem "Erro em buscar_por_ddr".
___________________________________________________________________________________________________________

def buscar_por_lp(lp):

Essa definição conecta com o banco de dados e localiza qualquer caractere existente em lp digitado no balão de busca para mostra-lo na área de resultado, permitindo uma busca que pode ser precisa caso digite um valor lp completo presente ou ampla se digitar apenas um ou mais caracteres. Caso não tenha nenhum caractere existente como valor lp você verá a mensagem "Erro em buscar_por_lp".
____________________________________________________________________________________________________________

def verificar_existencia(sip, ddr, lp):

Essa definição conecta com o banco de dados e faz uma verificação se o valor digitado nos balões de pesquisa de sip, ddr, ou lp estão presentes no banco de dados. Caso ocorra algum erro você verá a mensagem "Erro ao verificar_existencia".
____________________________________________________________________________________________________________

def inserir_cliente(data):

Essa definição conecta com o banco de dados e permitira que você insira os valores desejados no banco de dados em relação a um equipamento, como nome do cliente, sip, ddr, lp, etc. Caso ocorra um erro você verá a mensagem "Erro ao inserir cliente".
____________________________________________________________________________________________________________

def cadastrar_usuarios(data):

Essa definição conecta com o banco de dados e permitira que você insira os valores desejados no banco de dados em relação a uma conta de login, como usuário, login, senha e permissão. Caso ocorra algum erro você verá a mensagem "Erro ao inserir usuário".
_____________________________________________________________________________________________________________

def autenticar_usuario(login, senha):

Essa definição conecta com o banco de dados e procura os dados de usuário através de login e senha, caso eles sejam encontrados os resultados nome, login e permissão serão apresentados mas caso eles não sejam encontrados você verá a mensagem "Erro em autenticar_usuario".
_____________________________________________________________________________________________________________

def verificar_login_existente(login):

Essa definição conecta com o banco de dados e verifica se o login usado existe dentro do banco de dados, caso ele não seja encontrado você verá a mensagem "Erro em verificar_login_existente".
_____________________________________________________________________________________________________________

# Mostrando API na prática
Aqui veremos todas as etapas do que a API pode fazer passo a passo:

Primeiro temos a tela de login, que todos os usuários irão ver quando acessarem o link para usa-lá.

<img src="C:\Users\40418693\Pictures\Screenshots\Tela login.png" alt="Tela de login">
