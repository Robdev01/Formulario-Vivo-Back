# Formulário Vivo - Backend

Este repositório contém o backend da aplicação **Formulário Vivo**, desenvolvido com Flask. Ele é responsável por gerenciar as rotas, controlar a lógica de negócio e interagir com os dados do formulário.

---

## Estrutura do Projeto

```
Formulario-Vivo-Back/
├── app.py               # Arquivo principal para execução da aplicação Flask
├── routes.py            # Define as rotas da aplicação
├── controller.py        # Contém a lógica de controle
├── models.py            # Define as estruturas de dados (Modelos)
├── Procedimento.txt     # Possivelmente usado como documentação de fluxo
├── __init__.py          # Inicializa o pacote Flask
├── requiments.txt       # Lista de dependências (corrigir para requirements.txt)
```

---

## Como executar

1. **Crie o ambiente virtual:**

```bash
python -m venv .venv
```

2. **Ative o ambiente:**

- Windows:
```bash
.venv\Scripts\activate
```
- Linux/macOS:
```bash
source .venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requiments.txt
```

4. **Execute o servidor Flask:**

```bash
python app.py
```

---

## Tecnologias Utilizadas

- Python 3.x
- Flask
- MySQL (conector)
- Estrutura MVC (Model-View-Controller)

---

## Observações

- Certifique-se de que o banco de dados esteja configurado e acessível antes de rodar a aplicação.
- O arquivo `Procedimento.txt` pode conter instruções ou observações sobre o uso do sistema.

---

## Autor

Desenvolvido por Robson Calheira.
