# Sistema de Gestão do Grêmio Estudantil Carlos Marighella

## 1. Visão Geral

O **Sistema de Gestão do Grêmio Estudantil Carlos Marighella** é uma aplicação desktop em Python para cadastrar, consultar, atualizar e remover os membros do grêmio escolar. O acesso é protegido por **login e registro de usuários**, e todos os dados ficam salvos localmente em um banco SQLite.

Esta versão do MVP traz interface moderna com CustomTkinter (modo escuro), autenticação de usuários e código organizado em módulos separados.

---

## 2. Tecnologias

| Item | Descrição |
|---|---|
| Linguagem | Python 3.12 |
| Interface gráfica | CustomTkinter (tema escuro, cor azul) |
| Banco de dados | SQLite3 (arquivo local `gremio.db`) |
| Ambiente de desenvolvimento | Linux Mint, VS Code, Git e GitHub |

---

## 3. Estrutura de Arquivos

```
.
├── main.py              # Ponto de entrada: janela de login/registro e inicialização do sistema
├── janela_principal.py  # Janela principal com as abas de gerenciamento de membros
├── crud.py              # Funções de acesso ao banco (membros e autenticação)
├── database.py          # Conexão com o SQLite e criação das tabelas
├── gremio.db            # Banco de dados (criado automaticamente na primeira execução)
└── README.md            # Esta documentação
```

---

## 4. Arquitetura

O sistema separa a **camada de dados** (SQL) da **camada de apresentação** (interface):

* **`database.py`** abre a conexão com `gremio.db` e cria as tabelas, caso ainda não existam.
* **`crud.py`** concentra todas as operações SQL e é importado pelas telas.
* **`main.py`** cria a janela principal oculta (`withdraw()`), monta todo o seu conteúdo e exibe a janela de login por cima (`CTkToplevel`, modal com `grab_set()`). Quando o login é válido, a janela de login é fechada e a principal é exibida (`deiconify()`).
* **`janela_principal.py`** contém a função `montar_janela_principal(janela)`, que constrói as abas do sistema.

### 4.1. Banco de dados

**Tabela `membros`**

| Coluna | Tipo | Observação |
|---|---|---|
| `id` | INTEGER | Chave primária, autoincremento |
| `nome` | TEXT | Obrigatório |
| `cargo` | TEXT | Obrigatório |
| `idade` | INTEGER | Obrigatório |

**Tabela `usuarios`**

| Coluna | Tipo | Observação |
|---|---|---|
| `id` | INTEGER | Chave primária, autoincremento |
| `usuario` | TEXT | Obrigatório |
| `senha` | TEXT | Obrigatório |

### 4.2. Funções do `crud.py`

**Membros**

| Função | O que faz |
|---|---|
| `cadastrar_membro(nome, cargo, idade)` | Insere um novo membro (`INSERT`) |
| `atualizar_membro(coluna, dado_novo, id)` | Atualiza uma coluna de um membro (`UPDATE`) |
| `deletar_membro(id)` | Remove um membro (`DELETE`) |
| `buscar_dados_membros(id)` | Retorna `(nome, cargo, idade)` de um membro, ou `None` |
| `gerar_lista_membros()` | Retorna todos os membros (`SELECT *`) |

**Autenticação**

| Função | O que faz |
|---|---|
| `registrar_usuario(usuario, senha)` | Insere um novo usuário |
| `verificar_usuario(usuario, senha)` | Retorna o registro se usuário e senha conferem, senão `None` |

---

## 5. Fluxo de Acesso

Ao abrir o sistema aparece a janela **Login do Sistema**, com duas abas:

### 5.1. Aba Login
* Campos de **Usuário** e **Senha** (a senha fica oculta com `*`).
* Bloqueia o envio se algum campo estiver vazio ("Preencha todos os campos!").
* Se as credenciais forem válidas, abre a janela principal; caso contrário exibe "Usuário ou Senha Inválido. Registre-se!".

### 5.2. Aba Registrar-se
* Campos de **Usuário**, **Senha** e **Confirme a Senha**.
* Valida campos vazios e se as duas senhas são iguais.
* Informa quando o usuário já está cadastrado; caso contrário cria a conta e entra direto no sistema.

---

## 6. Janela Principal (`CTkTabview`)

A janela principal (500x550) é dividida em quatro abas.

### 6.1. Aba Cadastrar
* **Objetivo:** inserir novos membros.
* **Componentes:** campos de Nome, Cargo e Idade e botão **Cadastrar**.
* **Comportamento:** verifica se todos os campos foram preenchidos, grava no banco, mostra mensagem de sucesso em verde com o primeiro nome do membro e limpa os campos. Se faltar informação, mostra aviso em vermelho.

### 6.2. Aba Membros Cadastrados
* **Objetivo:** listar todos os membros.
* **Componentes:** cabeçalho fixo (ID, Nome, Cargo, Idade) e painel rolável (`CTkScrollableFrame`) com layout `.grid()`.
* **Comportamento:** a lista é recarregada automaticamente toda vez que o usuário entra na aba (parâmetro `command` do TabView), refletindo cadastros, atualizações e exclusões recentes.

### 6.3. Aba Atualizar Membro
* **Objetivo:** alterar nome, cargo ou idade de um membro existente.
* **Componentes:** campo de ID, menu suspenso (Nome, Cargo, Idade), campo do novo valor e botão **Atualizar**. O texto do campo muda conforme a opção escolhida.
* **Comportamento:**
  * Rejeita opção inválida, valor vazio e ID inexistente.
  * Para idade, exige número inteiro não negativo.
  * Mostra uma mensagem com o estado anterior e outra, em verde, confirmando o novo estado.

### 6.4. Aba Deletar Membro
* **Objetivo:** remover um membro com confirmação contextualizada.
* **Componentes:** campo de ID, menu de motivo ("Saiu", "Mudou de Cidade", "Faleceu"), rótulo de confirmação e botão **Deletar**.
* **Comportamento:** ao escolher o motivo, o sistema busca o membro e exibe uma frase de confirmação com seus dados. Ao clicar em **Deletar**, o registro é removido e aparece a mensagem de sucesso.

---

## 7. Como Executar

1. **Pré-requisito:** Python 3 instalado.

2. **Criar e ativar o ambiente virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # No Windows: venv\Scripts\activate
   ```

3. **Instalar as dependências:**

   ```bash
   pip install customtkinter
   ```

4. **Executar:**

   ```bash
   python main.py
   ```

Na primeira execução, o banco `gremio.db` e as tabelas são criados automaticamente. Use a aba **Registrar-se** para criar o primeiro usuário.

---

## 8. Melhorias Futuras

* Armazenar senhas com hash (por exemplo, `bcrypt` ou `hashlib`) em vez de texto puro.
* Impedir usuários duplicados pelo nome (restrição `UNIQUE` na coluna `usuario`).
* Confirmar a exclusão antes de executar e tratar ID vazio ou inválido nas abas de atualizar e deletar.
* Validar a idade também na aba Cadastrar.
* Busca e filtro na lista de membros.

---

*Desenvolvido por Mikael dos Santos Sena, como projeto prático de automação e programação desktop para o Grêmio Estudantil Carlos Marighella.*
