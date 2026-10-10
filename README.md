# Documentação Oficial do MVP: Sistema de Gestão do Grêmio Estudantil

## 1\. Visão Geral do Projeto

O **Sistema de Gestão do Grêmio Estudantil Carlos Marighella** é uma aplicação desktop desenvolvida em Python com o objetivo de automatizar, organizar e otimizar o controle de membros do grêmio escolar. O MVP (Mínimo Produto Viável) combina uma interface gráfica moderna e intuitiva com a robustez de um banco de dados relacional local, priorizando a usabilidade (UX) e as melhores práticas de desenvolvimento modular.

---

## 2\. Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.12  
* **Interface Gráfica (GUI):** CustomTkinter (Modo Dark padrão, temas customizados)  
* **Banco de Dados:** SQLite3 (Persistência local leve e segura)  
* **Ambiente de Desenvolvimento:** Linux Mint, VS Code, Git e GitHub

---

## 3\. Arquitetura do Sistema

O sistema adota uma arquitetura limpa, separando a **regra de negócio/backend** (interações SQL e manipulação de dados) da **camada de apresentação/frontend** (janelas, abas e componentes visuais do CustomTkinter).

* **Banco de Dados (`gremio.db`):** Contém a tabela `membros` com as colunas:  
  * `id` (INTEGER, Primary Key, Auto-increment)  
  * `nome` (TEXT, Obrigatório)  
  * `cargo` (TEXT, Obrigatório)  
  * `idade` (INTEGER, Obrigatório)

---

## 4\. Módulos e Funcionalidades da Interface (`CTkTabview`)

O sistema é dividido em abas organizadas por funcionalidade:

### 4.1. Aba: Cadastrar

* **Objetivo:** Inserir novos integrantes no banco de dados.  
* **Componentes:** Campos de texto (`CTkEntry`) para Nome, Cargo e Idade, além de um botão de envio.  
* **Comportamento:** Valida os dados inseridos, executa a instrução `INSERT` no SQLite, exibe uma mensagem de sucesso customizada com feedback de cores e limpa automaticamente os campos para o próximo cadastro.

### 4.2. Aba: Membros Cadastrados (Consulta)

* **Objetivo:** Exibir a lista completa de todos os membros registrados no sistema.  
* **Componentes:** Cabeçalho fixo e um painel rolável (`CTkScrollableFrame`) utilizando o gerenciador de layout `.grid()`.  
* **Comportamento:** Utiliza o parâmetro dinâmico de troca de abas (`command` no TabView) para atualizar os dados automaticamente (`SELECT * FROM membros`) sempre que o usuário navega para esta aba, garantindo sincronia instantânea com novos cadastros ou exclusões.

### 4.3. Aba: Atualizar Membro

* **Objetivo:** Modificar dados específicos de um membro existente de forma segura.  
* **Componentes:** Campo de ID, menu suspenso (`CTkOptionMenu`) contendo as opções de alteração (*Nome*, *Cargo*, *Idade*), campo para o novo valor e botão de confirmação.  
* **Comportamento:** Busca o registro pelo ID informado, valida se o membro existe e executa a query de atualização (`UPDATE`) correspondente ao campo selecionado.

### 4.4. Aba: Deletar Membro

* **Objetivo:** Remover membros do banco de dados com uma camada extra de confirmação e experiência de usuário interativa.  
* **Componentes:** Campo de ID, menu de seleção de motivos (*"Saiu"*, *"Mudou de Cidade"*, *"Faleceu"*), rótulo de confirmação dinâmica e botão de exclusão.  
* **Comportamento:** Consulta os dados do membro antes de apagar, exibe uma frase personalizada de confirmação contextualizada com o motivo escolhido e realiza a exclusão segura via comando `DELETE` no SQLite.

---

## 5\. Como Executar o Projeto

1. **Pré-requisitos:**  
     
   * Certifique-se de ter o Python instalado em seu sistema.

   

2. **Configuração do Ambiente Virtual (venv):**  
     
   python3 \-m venv venv  
     
   source venv/bin/activate  \# No Windows: venv\\Scripts\\activate  
     
3. **Instalação de Dependências:**  
     
   pip install customtkinter  
     
4. **Execução:**  
     
   python main.py

---

*Desenvolvido por Mikael dos Santos Sena, como projeto prático de automação e programação desktop para o Grêmio Estudantil Carlos Marighella.*