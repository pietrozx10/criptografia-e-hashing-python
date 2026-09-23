# 🔐 Estudo Prático de Criptografia, Hashing e Segurança Digital

Este repositório reúne conceitos fundamentais de **Criptografia por Substituição**, **Funções Hash Unidirecionais** e simulações práticas de **Ataques de Força Bruta** (por dicionário e exaustivo) desenvolvidos em Python.

---

## 📌 Conteúdo do Projeto

### 1. Cifra de Substituição (`codifica_substituicao`)
* Mapeia letras minúsculas (`a`-`z`) utilizando seus valores ASCII convertidos para índices de `0` a `25` (`ord(letra) - ord("a")`).
* Subtitui os caracteres por uma chave customizada baseada no layout QWERTY.

### 2. Função Hash (`calcula_hash`)
* Converte um texto de entrada em um valor numérico através da soma dos códigos ASCII de seus caracteres.
* Apresenta o conceito de irreversibilidade em funções de hash.

### 3. Ataque por Dicionário (`simula_ataque_dicionario`)
* Simula a validação de um hash cadastrado contra uma lista de **senhas populares e vazadas** (`SENHAS_COMUNS`).
* Utiliza a biblioteca `itertools.product` para demonstrar como computadores conseguem identificar senhas fracas instantaneamente.

### 4. Ataque de Força Bruta Completo (`simula_forca_bruta_completa`)
* Demonstra como quebrar senhas que não estão em dicionários, testando **todas as combinações possíveis de caracteres**.
* Utiliza `itertools.product(..., repeat=tamanho)` e concatenação com `"".join()`.
* Evidencia o **crescimento exponencial** do tempo de processamento conforme o tamanho da senha aumenta.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3
* **Módulo Nativo:** `itertools` (para análise combinatória e produto cartesiano)
* **Conceitos:** Tabela ASCII, Funções Hash, Análise Combinatória, Estruturas de Repetição.

---

## 💡 Lições de Segurança Digital

1. **Evite senhas comuns e vazadas:** Senhas como `"123456"` ou `"password"` são descobertas em milissegundos por ataques de dicionário.
2. **Priorize o comprimento da senha:** Quanto mais caracteres a senha tiver, exponencialmente maior será a quantidade de combinações necessárias, tornando inviável o ataque por força bruta.
3. **Não reutilize senhas:** Caso uma senha vazará em um serviço, ela será testada automaticamente em outros sistemas.

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone [https://github.com/seu-usuario/criptografia-python.git](https://github.com/seu-usuario/criptografia-python.git)

# Acesse a pasta
cd criptografia-python

# Executa o projeto
python main.py
