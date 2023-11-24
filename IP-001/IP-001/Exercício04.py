# Declarando uma variável 'nome'
nome_completo = "Raíssa Simões de Angelo"

# Funcionalidades de strings e separação em 2 variáveis: 'nome' e 'sobrenome'
espaco_indice = nome_completo.find(" ")
nome = nome_completo[:espaco_indice]
sobrenome = nome_completo[espaco_indice + 1:]

# Verificando qual variável antecede a outra em ordem alfabética
ordem_alfabetica = sorted([nome, sobrenome])

# Verificando quantidade de caracteres das novas variáveis
tamanho_nome = len(nome)
tamanho_sobrenome = len(sobrenome)

# Verificando se meu nome é um palíndromo
e_palindromo = nome.lower() == nome.lower()[::-1]

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Ordem alfabética: {ordem_alfabetica[0]} -> {ordem_alfabetica[1]}")
print(f"Tamanho do nome: {tamanho_nome} caracteres")
print(f"Tamanho do sobrenome: {tamanho_sobrenome} caracteres")
print(f"Seu nome é um palíndromo? {e_palindromo}")
