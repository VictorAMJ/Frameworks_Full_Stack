'''
Atividade 1

Em python, desenvolva uma função chamada contator que recebe uma string e retorna
um dicionário contendo a contagem das ocorrências de cada palavra presente na string.
As palavras devem ser consideradas em minúsculas e separadas por espaços, descon"
siderando qualquer pontuação.

Exemplo:
contator("Esse exercício é um exercício fácil ou difícil")
Retorno:
{'esse': 1, 'exercício': 2, 'é': 1, 'um': 1, 'fácil': 1, 'ou': 1, 'difícil': 1}
Observações:
• A função deve ignorar a diferença entre letras maiúsculas e minúsculas.
• A contagem deve incluir todas as palavras, mesmo que apareçam mais de uma vez.
'''

def contador(frase):
    palavras = frase.split()
    dicionario = {}

    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

palavrinha = input('Digite uma frase: ')
print(contador(palavrinha))






