# Código feito com Python ver.3.13.1 (geradsenhas.py)**pyton

import random # type: ignore
import string # type: ignore

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    """
    Função para gerar uma senha aleatória:

    :param comprimento: Comprimento da senha a ser gerada (padrão é 12).
    :param incluir_maiusculas: Incluir letras maiúsculas na senha (padrão é True).
    :param incluir_numeros: Incluir números na senha (padrão é True).
    :param incluir_simbolos: Incluir caracteres especiais na senha (padrão é True).
    :return: Senha gerada.
    """
    
    caracteres = string.ascii_lowercase  # Letras minúsculas (a-z)
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase  # Letras maiúsculas (A-Z)
    
    if incluir_numeros:
        caracteres += string.digits  # Números (0-9)
    
    if incluir_simbolos:
        caracteres += string.punctuation  # Caracteres especiais
    
    # Gerando a senha...
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    
    return senha

def main():
    print("Gerador de Senhas Aleatórias")

    # Configurações do gerador:
    comprimento = int(input("Digite o comprimento da senha: "))
    
    # Verificar se o comprimento da senha está dentro do limite (máximo 15).
    if comprimento > 15:
        print('Senha é grande demais para ser gerada! O comprimento máximo é 15.')
        return  # Encerra a função se o comprimento for maior que 15.

    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    
    # Gerar e exibir a senha:
    senha_gerada = gerar_senha(comprimento=comprimento, incluir_maiusculas=incluir_maiusculas, 
                               incluir_numeros=incluir_numeros, incluir_simbolos=incluir_simbolos)
    print(f"Senha gerada: {senha_gerada}")

if __name__ == "__main__":
    main()
