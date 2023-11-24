# Analisando o que será impresso em cada linha
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::-1])
# Resultado: [9, 8, 7, 6, 5, 4, 3, 2, 1]
# Ou seja, '[::-1]' pede para o programa inverter a lista

# --------------------------------------------
print(L[-1::])
# Resultado: [9]
# Ou seja, '[-1]' significa o último elemento da lista

# --------------------------------------------
print(L[:-1:])
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8]
# Ou seja, '[:-1:] remove o último elemento da lista

# --------------------------------------------
print(L[::-2])
# Resultado: [9, 7, 5, 3, 1]
# Ou seja, '[::-2]' inverte a lista e pega cada segundo elemento

# --------------------------------------------
print(L[-2::])
# Resultado: [8, 9]
# Ou seja, '[-2::]' pega os dois últimos elementos

# --------------------------------------------
print(L[:-2:])
# Resultado: [1, 2, 3, 4, 5, 6, 7]
# Ou seja, '[:-2:]' exclui os dois últimos elemntos da lista
