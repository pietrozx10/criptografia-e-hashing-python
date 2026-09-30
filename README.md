🔐 Projeto de Criptografia

Projeto desenvolvido em Python para demonstrar conceitos básicos de criptografia e segurança da informação.

📌 Sobre o projeto

Este programa permite que o usuário escreva uma mensagem e utilize uma chave para:

Criptografar uma mensagem;

Descriptografar uma mensagem;

Manter informações protegidas durante o processo.

O projeto tem finalidade educacional e demonstra de forma simples como uma mensagem pode ser transformada em um formato que dificulta sua leitura sem a chave correta.

🛠️ Tecnologias

Python 3

Biblioteca cryptography

📥 Instalação

Instale a biblioteca necessária utilizando:

pip install cryptography

▶️ Como executar

Execute o arquivo:

python criptografia.py


O programa apresentará um menu com opções para criptografar ou descriptografar uma mensagem.

🔐 Funcionamento

O programa utiliza a biblioteca cryptography e o algoritmo Fernet, que fornece criptografia simétrica.

Na criptografia simétrica, a mesma chave é utilizada para proteger e posteriormente recuperar a mensagem.

Exemplo

Mensagem original:

Olá, este é meu projeto!


Depois da criptografia, a mensagem será transformada em um conteúdo codificado.

Com a chave correta, é possível recuperar a mensagem original.

⚠️ Segurança

A chave de criptografia deve ser mantida em segurança.

Não publique chaves reais no GitHub.

Para projetos reais, recomenda-se utilizar variáveis de ambiente ou sistemas de gerenciamento de segredos.

🎓 Objetivo

O objetivo deste projeto é demonstrar conceitos básicos de:

Criptografia;

Segurança de código;

Proteção de informações;

Gerenciamento de chaves;

Programação em Python.

📚 Observação

Este projeto é educacional e não deve ser utilizado como único mecanismo de proteção para informações sensíveis em sistemas reais.
