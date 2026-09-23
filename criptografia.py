"""
Projeto: Algoritmos de Criptografia e Hashing em Python
Descrição: Estudo prático de Cifra de Substituição (criptografia reversível) 
           e Funções Hash (transformação unidirecional).
"""

# =====================================================================
# MÓDULO 1: CIFRA DE SUBSTITUIÇÃO (REVERSÍVEL)
# =====================================================================

# Dicionário de substituição baseado no layout QWERTY
DICIONARIO_QWERTY = "qwertyuiopasdfghjklzxcvbnm"

def codifica_substituicao(senha: str) -> str:
    """
    Criptografa uma senha substituindo letras minúsculas ('a'-'z') 
    com base no dicionário QWERTY.
    
    Caracteres fora do intervalo (maiúsculas, números e símbolos) 
    são mantidos inalterados para evitar erros de índice.
    """
    senha_criptografada = ""
    for letra in senha:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a")  # Mapeia ASCII para índice 0-25
            senha_criptografada += DICIONARIO_QWERTY[posicao]
        else:
            senha_criptografada += letra
            
    return senha_criptografada


# =====================================================================
# MÓDULO 2: FUNÇÃO HASH (UNIDIRECIONAL E IRREVERSÍVEL)
# =====================================================================

def calcula_hash_ascii(senha: str) -> int:
    """
    Gera um valor numérico inteiro (Hash) a partir da soma dos códigos ASCII
    de cada caractere presente na senha.
    
    Suporta letras (maiúsculas e minúsculas), números e símbolos.
    """
    valor_hash = 0
    for letra in senha:
        valor_hash += ord(letra)
    return valor_hash


# =====================================================================
# EXECUÇÃO E TESTES
# =====================================================================

def main():
    print("=====================================================")
    print("      DEMONSTRAÇÃO DE CRIPTOGRAFIA E HASHING        ")
    print("=====================================================\n")

    # --- Teste do Módulo 1 ---
    print("--- 1. Cifra de Substituição ---")
    senhas_teste = ["marcelo", "Marcelo123", "python!2026"]
    
    for s in senhas_teste:
        cifrada = codifica_substituicao(s)
        print(f"Original: {s:<15} | Cifrada: {cifrada}")
    
    print("\n-----------------------------------------------------\n")

    # --- Teste do Módulo 2 ---
    print("--- 2. Função Hash ASCII (Unidirecional) ---")
    senhas_hash = ["marcelo123", "marcelo123!", "python"]
    
    for s in senhas_hash:
        h = calcula_hash_ascii(s)
        print(f"Senha: {s:<15} | Hash Calculado: {h}")

    print("\n--- Demonstração de Colisão em Função Hash ---")
    h1 = calcula_hash_ascii("olecram")
    h2 = calcula_hash_ascii("oledrbk")
    print(f"Hash de 'olecram': {h1}")
    print(f"Hash de 'oledrbk': {h2}")
    print("Nota: Entradas diferentes gerando o mesmo hash comprovam a irreversibilidade!")


if __name__ == "__main__":
    main()
