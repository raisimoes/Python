# --------------------------------------------
# Operadores aritméticos
a = 7.0
b = 3.0

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
modulo = a % b

# Operadores aritméticos compostos
a += 3.0 # a = a + 3.0
b *= 4.0 # b = b * 4.0

# --------------------------------------------
# Maior potência de 2 representável
maior_potencia_de_2 = float('inf')
while not (maior_potencia_de_2 * 2).isinf():
    maior_potencia_de_2 *= 2

# Menor potência de 2 representável
menor_potencia_de_2 = 1.0
while (menor_potencia_de_2 / 2) != 0.0:
    menor_potencia_de_2 /= 2

print(f"Maior potência de 2 representável: {maior_potencia_de_2}")
print (f"Menor potência de 2 representável: {menor_potencia_de_2}")

# --------------------------------------------
# Imutabilidade de variáveis numéricas
x = 5.32
y = x
x += 1.0

print(x) # 6.32
print(y) # não sofreu alteração

# --------------------------------------------
# Métodos disponíveis para variáveis de ponto flutuante
x = 5.32
print(dir(x))