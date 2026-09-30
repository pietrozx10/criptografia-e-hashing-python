from cryptography.fernet import Fernet

def gerar_chave():
"""Gera uma nova chave de criptografia."""
return Fernet.generate_key()

def criptografar(mensagem, chave):
"""Criptografa uma mensagem usando a chave fornecida."""
fernet = Fernet(chave)
mensagem_criptografada = fernet.encrypt(mensagem.encode())
return mensagem_criptografada

def descriptografar(mensagem, chave):
"""Descriptografa uma mensagem usando a chave fornecida."""
fernet = Fernet(chave)
mensagem_original = fernet.decrypt(mensagem).decode()
return mensagem_original

def main():
print("=== PROGRAMA DE CRIPTOGRAFIA ===")
print("1 - Criptografar mensagem")
print("2 - Descriptografar mensagem")
print("3 - Sair")

chave = gerar_chave()

while True:
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        mensagem = input("Digite a mensagem: ")

        mensagem_criptografada = criptografar(
            mensagem,
            chave
        )

        print("\nMensagem criptografada:")
        print(mensagem_criptografada.decode())

        print("\nChave utilizada:")
        print(chave.decode())

    elif opcao == "2":
        mensagem = input(
            "Cole a mensagem criptografada: "
        )

        chave_usuario = input(
            "Digite a chave de descriptografia: "
        )

        try:
            mensagem_original = descriptografar(
                mensagem.encode(),
                chave_usuario.encode()
            )

            print("\nMensagem original:")
            print(mensagem_original)

        except Exception:
            print(
                "\nErro: mensagem ou chave inválida."
            )

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")

if name == "main":
main()
