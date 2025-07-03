# Formulário Vivo
O _Formulário Vivo_ disponibiliza uma API que permite acesso a um sistema de busca, cadastro e alteração de dados de equipamentos em um sistema.

# Funcionalidades
* Cadastro de equipamentos
* Remoção de equipamentos
* Alteração de equipamentos
* Busca de equipamentos
* Cadastro de usuários

Dependências necessárias para fazer a API funcionar:
* annotated-types==0.7.0
* anyio==4.9.0
* blinker==1.9.0
* click==8.1.8
* colorama==0.4.6
* dotenv==0.9.9
* et_xmlfile==2.0.0
* fastapi==0.115.14
* Flask==3.1.0
* flask-cors==6.0.0
* Flask-MySQLdb==2.0.0
* greenlet==3.2.3
* idna==3.10
* itsdangerous==2.2.0
* Jinja2==3.1.6
* MarkupSafe==3.0.2
* mysql-connector==2.2.9
* mysql-connector-python==9.2.0
* mysqlclient==2.2.7
* numpy==2.2.4
* openpyxl==3.1.5
* pandas==2.2.3
* pydantic==2.11.7
* pydantic_core==2.33.2
* PyMySQL==1.1.1
* python-dateutil==2.9.0.post0
* python-dotenv==1.1.0
* pytz==2025.2
* pywin32==310
* six==1.17.0
* sniffio==1.3.1
* SQLAlchemy==2.0.41
* starlette==0.46.2
* typing-inspection==0.4.1
* typing_extensions==4.14.0
* tzdata==2025.2
* Werkzeug==3.1.3


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

Essa definição conecta com o banco de dados e localiza qualquer caractere existente em SIP digitado no balão de busca para mostra-lo na área de resultado, permitindo uma busca que pode ser precisa caso digite um valor SIP completo presente ou ampla se digitar apenas um ou mais caracteres. Caso não tenha nenhum caractere existente como valor SIP você verá a mensagem "Erro em buscar_por_sip".
__________________________________________________________________________________________________________

def buscar_por_ddr(ddr):

Essa definição conecta com o banco de dados e localiza qualquer caractere existente em DDR digitado no balão de busca para mostra-lo na área de resultado, permitindo uma busca que pode ser precisa caso digite um valor DDR completo presente ou ampla se digitar apenas um ou mais caracteres. Caso não tenha nenhum caractere existente como valor DDR você verá a mensagem "Erro em buscar_por_ddr".
___________________________________________________________________________________________________________

def buscar_por_lp(lp):

Essa definição conecta com o banco de dados e localiza qualquer caractere existente em LP digitado no balão de busca para mostra-lo na área de resultado, permitindo uma busca que pode ser precisa caso digite um valor LP completo presente ou ampla se digitar apenas um ou mais caracteres. Caso não tenha nenhum caractere existente como valor LP você verá a mensagem "Erro em buscar_por_lp".
____________________________________________________________________________________________________________

def verificar_existencia(sip, ddr, lp):

Essa definição conecta com o banco de dados e faz uma verificação se o valor digitado nos balões de pesquisa de SIP, DDR, ou LP estão presentes no banco de dados. Caso ocorra algum erro você verá a mensagem "Erro ao verificar_existencia".
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

# Mostrando a API na prática
Aqui veremos todas as etapas do que a API pode fazer passo a passo:

Primeiro você deve baixar o Node.js, depois de instalado digite npm install no terminal ou cmd e execute o comando:

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/npm%20install.png" alt="npm install">

Segundo, após baixar os arquivos dos repositórios Formulário Vivo-Front e Formulário Vivo-Back e coloca-los em pastas separadas você deve abrir essas pastas em um editor de código, dirija-se até o arquivo requirements.txt para ver todas as bibliotecas necessárias para fazer a API funcionar e em seguida abra o terminal e digite o comando "pip install -r requirements.txt":

<img src ="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Requirements.png" alt="Requerimentos">

Esse comando ira instalar todas as biblioetacas e dependencias presentes no arquivo de texto, lembrando que isso deve ser feito em ambas as janelas, caso não o faça a API não funcionará.

Quando a API estiver funcionando nós chegamos na tela de login da API, que todos os usuários irão ver quando acessarem o link para usa-lá.

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Tela%20login.png" alt="Tela de login">

Você pode entrar usando uma conta disponibilizada por um Administrador, tendo essa conta permissão para Técnicos ou Administradores, mais a baixo veremos a diferença entra essas contas.

Começamos com uma conta com permissões de Administrador, como você pode ver essa conta tem acesso a função de pesquisa por equipamentos, mas também tem acesso as opções Registro de equipamentos e Cadastro de usuário localizado no canto direito superior da tela:

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Tela%20de%20busca%20admin.png" alt="Tela de busca admin">

Diferente de uma conta com permissão de Técnico que só tem acesso a página de pesquisa por equipamentos:

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Tela%20de%20busca%20t%C3%A9cnico.png" alt="Tela de busca técnico">

Outro privilégio que apenas administradores tem acesso é a opção de modificar ou excluir dados de equipamentos depois deles serem encontrados no banco de dados, como podemos ver no exemplo abaxio:

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Busca%20admin%20resultado.png" alt="Tela de busca admin resultado">

Agora vamos até outra página que os administradores tem acesso, a tela de Registro de equipamentos, aqui você pode colocar todas as informações de um equipamento como o nome do cliente, SIP, DDR, LP, etc. Não é necessário se preocupar em preencher todos os espaços, contanto que a área de SIP, DDR, ou LP estejam preenchidas você pode registrar qualquer equipamento, mas tome cuidado pois não é possível registrar equipamentos que tenham o mesmo SIP, DDR ou LP.

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Cadastro%20equip.png" alt="Tela de Registro de equipamentos">

Por último, temos a página de cadastro de usuários, onde o administrador poderá criar novas contas para login na API e decidir qual a permissão que os usuários irão receber, lembre-se todas as áreas devem ser preenchidas para que uma nova conta seja criada.

<img src="https://github.com/LucasPS23/Formulario-Vivo-Back/blob/main/Imagens_API/Cadastro%20usu%C3%A1rio.png" alt="Tela de Cadastro de usuários">





