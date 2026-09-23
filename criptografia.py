"""
Projeto: Algoritmos de Criptografia, Hashing e Segurança Digital em Python
Descrição: Estudo prático cobrindo Cifra de Substituição, Funções Hash,
           Ataques de Dicionário (Senhas Comuns) e Ataques de Força Bruta Exaustivos.
"""

import itertools

# =====================================================================
# MÓDULO 1: CIFRA DE SUBSTITUIÇÃO (REVERSÍVEL)
# =====================================================================

DICIONARIO_QWERTY = "qwertyuiopasdfghjklzxcvbnm"

def codifica_substituicao(senha: str) -> str:
    """
    Criptografa uma senha substituindo caracteres minúsculos ('a'-'z')
    pelo seu correspondente no dicionário QWERTY baseando-se no índice ASCII (0 a 25).
    """
    senha_criptografada = ""
    for letra in senha:
        if "a" <= letra <= "z":
            # Calcula a posição relativa no alfabeto (0 a 25)
            posicao = ord(letra) - ord("a")
            senha_criptografada += DICIONARIO_QWERTY[posicao]
        else:
            senha_criptografada += letra
            
    return senha_criptografada


# =====================================================================
# MÓDULO 2: FUNÇÃO HASH (UNIDIRECIONAL)
# =====================================================================

def calcula_hash(senha: str) -> int:
    """
    Gera um valor numérico inteiro (Hash) a partir da soma dos códigos ASCII
    de cada caractere presente na senha.
    """
    valor_hash = 0
    for letra in senha:
        valor_hash += ord(letra)
    return valor_hash


# =====================================================================
# MÓDULO 3: ATAQUE POR DICIONÁRIO (SENHAS COMUNS/VAZADAS)
# =====================================================================

# Lista de senhas populares / vazadas frequentemente testadas em ataques
SENHAS_COMUNS = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "12345678",
    "111111",
    "12345",
    "columbia",
    "senha",
    "iloveyou"
]

def simula_ataque_dicionario(hash_alvo: int) -> bool:
    """
    Simula um ataque testando o hash cadastrado contra os hashes de uma 
    lista de senhas populares utilizando a análise combinatória do itertools.
    """
    # 1. Gera a lista de hashes das senhas comuns
    hashes_comuns = []
    for senha in SENHAS_COMUNS:
        hashes_comuns.append(calcula_hash(senha))

    # 2. Cria pares de comparação com itertools.product
    combinacoes = list(itertools.product([hash_alvo], hashes_comuns))

    # 3. Compara o hash da senha cadastrada com cada hash comum
    for hash_cadastrado, hash_teste in combinacoes:
        if hash_cadastrado == hash_teste:
            # Encontra a senha correspondente na lista
            indice = hashes_comuns.index(hash_teste)
            senha_encontrada = SENHAS_COMUNS[indice]
            print(f"[!] SUCESSO (Dicionário): Senha comum encontrada! -> '{senha_encontrada}' (Hash: {hash_teste})")
            return True

    print("[-] FALHA (Dicionário): A senha não faz parte da lista de senhas comuns.")
    return False


# =====================================================================
# MÓDULO 4: ATAQUE DE FORÇA BRUTA COMPLETO (EXAUSTIVO)
# =====================================================================

def simula_forca_bruta_completa(hash_alvo: int, tamanho_max: int, dicionario_caracteres: str) -> bool:
    """
    Testa TODAS as combinações possíveis de caracteres de um determinado tamanho
    usando itertools.product com o argumento repeat.
    """
    print(f"[*] Iniciando Força Bruta Completa (Tamanho: {tamanho_max} caracteres)...")
    
    # Gera todas as combinações de tamanho 'tamanho_max'
    for combinacao in itertools.product(dicionario_caracteres, repeat=tamanho_max):
        # Converte a tupla de caracteres em string para calcular o hash
        tentativa_texto = "".join(combinacao)
        
        if calcula_hash(tentativa_texto) == hash_alvo:
            print(f"[!] SUCESSO (Força Bruta): Senha quebrada! -> '{tentativa_texto}' (Hash: {hash_alvo})")
            return True

    print("[-] FALHA (Força Bruta): Nenhuma combinação correspondeu ao hash alvo.")
    return False


# =====================================================================
# EXECUÇÃO E DEMONSTRAÇÃO GERAL DO PROJETO
# =====================================================================

def main():
    print("=========================================================")
    print("      DEMONSTRAÇÃO DE SEGURANÇA DIGITAL E SEGURANÇA      ")
    print("=========================================================\n")

    # --- 1. Cifra de Substituição ---
    print("--- 1. Cifra de Substituição ---")
    senha_exemplo = "marcelo"
    print(f"Original: {senha_exemplo} | Cifrada: {codifica_substituicao(senha_exemplo)}\n")

    # --- 2. Função Hash ---
    print("--- 2. Função Hash ASCII ---")
    hash_exemplo = calcula_hash(senha_exemplo)
    print(f"Senha: {senha_exemplo} | Hash Calculado: {hash_exemplo}\n")

    # --- 3. Ataque por Dicionário ---
    print("--- 3. Simulação de Ataque por Dicionário (Senhas Comuns) ---")
    senha_fraca = "123456"
    hash_fraco = calcula_hash(senha_fraca)
    print(f"Testando a senha vulnerável '{senha_fraca}'...")
    simula_ataque_dicionario(hash_fraco)
    print()

    # --- 4. Ataque de Força Bruta Completo ---
    print("--- 4. Simulação de Ataque de Força Bruta Completo ---")
    senha_alvo = "mar"
    hash_alvo = calcula_hash(senha_alvo)
    
    # Conjunto de caracteres a serem testados
    dicionario_caracteres = "abcdefghijklmnopqrstuvwxyzABC123!@#$"
    
    print(f"Alvo: Senha de {len(senha_alvo)} caracteres ('{senha_alvo}')")
    simula_forca_bruta_completa(
        hash_alvo=hash_alvo, 
        tamanho_max=len(senha_alvo), 
        dicionario_caracteres=dicionario_caracteres
    )

if __name__ == "__main__":
    main()
