# 🔐 Criptografia e Hashing em Python

Este repositório foi criado para estudar e demonstrar a diferença prática entre **Criptografia por Substituição** (cifra reversível) e **Funções Hash** (transformação unidirecional), utilizando a linguagem Python e a manipulação da **Tabela ASCII**.

---

## 📌 Funcionalidades do Projeto

### 1. Cifra de Substituição (`codifica_substituicao`)
- **Conceito:** Substitui cada caractere da mensagem original por outro equivalente com base em um mapa de teclado QWERTY.
- **Funcionamento:** Utiliza a função `ord()` para mapear o código ASCII de caracteres minúsculos (`a`-`z`) em posições de `0` a `25`.
- **Tratamento de Exceções:** Mantém caracteres que não são letras minúsculas (maiúsculas, números e símbolos) inalterados, evitando erros de índice (`IndexError`).

### 2. Função Hash ASCII (`calcula_hash_ascii`)
- **Conceito:** Converte qualquer texto em uma representação numérica inteira através do somatório dos valores ASCII de seus caracteres.
- **Irreversibilidade:** Diferente da cifra de substituição, não existe uma fórmula matemática para "desfazer" a soma e obter o texto original a partir do número.
- **Colisão de Hash:** Demonstra que entradas diferentes (como `olecram` e `oledrbk`) podem resultar no mesmo valor (`739`), o que confirma a unidirecionalidade do processo.

---

## 🚀 Como Executar o Código

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/criptografia-e-hashing-python.git](https://github.com/SEU-USUARIO/criptografia-e-hashing-python.git)
   cd criptografia-e-hashing-python
